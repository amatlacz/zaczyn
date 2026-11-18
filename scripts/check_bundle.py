#!/usr/bin/env python3
"""Offline packaging contract checks; no model calls or host installation."""
import hashlib
from pathlib import Path
import tempfile
import unittest

import build_bundle as bundle


class Editions(unittest.TestCase):
    def setUp(self):
        self.native = bundle.native_payload()
        self.version = self.native['VERSION'].decode().strip()

    def test_compiled_reference_is_complete_and_tracks_source(self):
        chat = bundle.chat_payload(self.native, self.version)
        text = chat['ZACZYN.md'].decode()
        for name in self.native:
            if name.startswith('core/') and name.endswith('.md'):
                self.assertEqual(text.count('<a id="' + bundle.section_id(name) + '"></a>'), 1)
        changed = dict(self.native)
        changed['core/references/customization.md'] += b'\nA unique source propagation marker.\n'
        updated = bundle.chat_payload(changed, self.version)['ZACZYN.md']
        self.assertIn(b'A unique source propagation marker.', updated)
        self.assertNotEqual(updated, chat['ZACZYN.md'])

    def test_missing_resource_is_rejected(self):
        broken = dict(self.native)
        del broken['core/references/customization.md']
        with self.assertRaisesRegex(ValueError, 'Unbundled chat reference'):
            bundle.chat_payload(broken, self.version)
        with self.assertRaisesRegex(ValueError, 'Missing native resource'):
            bundle.skill_payload(broken, 'zaczyn-setup')

    def test_host_skills_are_identical_and_independently_installable(self):
        previous = None
        for host in bundle.HOSTS:
            payload = bundle.host_payload(self.native, host)
            skills = {n: data for n, data in payload.items() if n.startswith('skills/')}
            if previous is not None:
                self.assertEqual(previous, skills)
            previous = skills
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                for name, data in payload.items():
                    target = root/name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                bundle.check_host_tree(root)
                # Removing every other skill must not strand this skill's resources.
                import shutil
                for skill in bundle.EXPECTED:
                    isolated = root/('isolated-' + skill)
                    shutil.copytree(root/'skills'/skill, isolated)
                    bundle.check_links(isolated)
                    self.assertEqual(list(isolated.rglob('SKILL.md')), [isolated/'SKILL.md'])
                    self.assertEqual(list(isolated.rglob('AGENTS.md')), [])

    def test_native_exports_follow_core_changes_and_reject_active_templates(self):
        changed = dict(self.native)
        changed['core/assets/AGENTS.md'] += b'\nA unique template propagation marker.\n'
        payload = bundle.host_payload(changed, 'codex')
        templates = [data for name, data in payload.items() if name.endswith('/AGENTS-template.md')]
        self.assertTrue(templates)
        self.assertTrue(all(b'A unique template propagation marker.' in data for data in templates))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, data in payload.items():
                target = root/name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            (root/'skills/zaczyn-setup/AGENTS.md').write_text('Accidental active template', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'active workspace context'):
                bundle.check_host_tree(root)

    def test_builds_are_reproducible_and_extracted_links_resolve(self):
        editions = [(self.native, bundle.check_tree),
                    (bundle.chat_payload(self.native, self.version), bundle.check_links)]
        editions += [(bundle.host_payload(self.native, host), bundle.check_host_tree) for host in bundle.HOSTS]
        stamp = self.version + '+gdeadbeef0000'
        editions += [(bundle.host_payload(self.native, host, stamp), bundle.check_host_tree) for host in bundle.HOSTS]
        editions += [(bundle.single_payload(self.native, stamp), bundle.check_single_tree),
                     (bundle.chat_payload(self.native, self.version, stamp), bundle.check_links)]
        stamped = bundle.host_payload(self.native, 'codex', stamp)
        self.assertTrue(all(data == (stamp + '\n').encode() for name, data in stamped.items() if name.endswith('VERSION')))
        self.assertEqual(bundle.build_stamp(self.version), bundle.build_stamp(self.version))
        for payload, checker in editions:
            with tempfile.TemporaryDirectory() as directory:
                first, second = Path(directory)/'one.zip', Path(directory)/'two.zip'
                bundle.write_zip(payload, first, checker)
                bundle.write_zip(payload, second, checker)
                self.assertEqual(first.read_bytes(), second.read_bytes())
                expected = hashlib.sha256(first.read_bytes()).hexdigest()
                self.assertEqual(first.with_suffix('.zip.sha256').read_text(encoding='utf-8'), expected+'  one.zip\n')

    def test_skill_frontmatter_rules_reject_bad_skills(self):
        good = '---\nname: demo-skill\ndescription: Does one thing. Use when asked.\n---\n\n# Demo\n'
        bundle.check_skill_file(good, 'demo-skill', 'good')
        bundle.check_skill_file(good.replace('---\n\n', 'license: MIT\nmetadata:\n  version: "1"\n---\n\n'), 'demo-skill', 'good with optional fields')
        name, keys, desc = 'name must', 'Frontmatter keys', 'description'
        bad = {
            'name differs from folder': (good.replace('name: demo-skill', 'name: other-skill'), name),
            'uppercase name': (good.replace('name: demo-skill', 'name: Demo-Skill'), name),
            'leading hyphen': (good.replace('name: demo-skill', 'name: -demo-skill'), name),
            'double hyphen': (good.replace('name: demo-skill', 'name: demo--skill'), name),
            'missing name': (good.replace('name: demo-skill\n', ''), name),
            'unknown key': (good.replace('---\n\n', 'version: 1\n---\n\n'), keys),
            'duplicate key': (good.replace('---\n\n', 'name: demo-skill\n---\n\n'), keys),
            'long description': (good.replace('Does one thing. Use when asked.', 'x' * 1025), desc),
            'empty description': (good.replace('Does one thing. Use when asked.', ''), desc),
            'colon in description': (good.replace('Use when asked.', 'Use when: asked.'), desc),
            'trailing colon': (good.replace('Use when asked.', 'Use when:'), desc),
            'tab before hash': (good.replace('Use when asked.', 'Use when asked.\t#c'), desc),
            'long compatibility': (good.replace('---\n\n', 'compatibility: ' + 'x' * 501 + '\n---\n\n'), 'compatibility'),
            'scalar metadata': (good.replace('---\n\n', 'metadata: foo\n---\n\n'), 'metadata'),
            'long body': (good + 'line\n' * 501, '500 lines'),
        }
        for label, (text, message) in bad.items():
            with self.assertRaisesRegex(ValueError, message, msg=label):
                bundle.check_skill_file(text, 'demo-skill', label)

    def test_exports_are_flat_and_ship_only_needed_guides(self):
        for skill in bundle.PUBLIC_SKILLS:
            payload = bundle.skill_payload(self.native, skill)
            self.assertTrue(all(name.count('/') <= 1 for name in payload), skill)
            self.assertEqual('references/orchestration.md' in payload, skill == 'zaczyn-orchestrate', skill)

    def test_single_files_are_self_contained(self):
        payload = bundle.single_payload(self.native, self.version)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, data in payload.items():
                (root/name).write_bytes(data)
            bundle.check_single_tree(root)
        for skill in bundle.SINGLE_SKILLS:
            text = payload[skill + '.md'].decode()
            for _, target in bundle.LINK.findall(text):
                self.assertTrue(target.startswith(('#', 'http://', 'https://')), (skill, target))
            self.assertEqual([l for l in bundle.outside_fences(text) if l.startswith('# ')], ['# ' + skill.split('-')[1].title()], skill)
        task = payload['zaczyn-work.md'].decode()
        self.assertIn('````markdown\n---\nstatus: open\n---\n\n# {{task name}}', task)
        original = bundle.SINGLE_LIMIT
        try:
            bundle.SINGLE_LIMIT = 1000
            with self.assertRaisesRegex(ValueError, 'limit'):
                bundle.single_payload(self.native, self.version)
        finally:
            bundle.SINGLE_LIMIT = original

    def test_exported_templates_are_verbatim(self):
        payload = bundle.skill_payload(self.native, 'zaczyn-work')
        self.assertEqual(payload['references/task-template.md'], self.native['core/assets/task.md'])
        chat = bundle.chat_payload(self.native, self.version)['ZACZYN.md'].decode()
        self.assertEqual([l for l in bundle.outside_fences(chat) if l.startswith('# ')], ['# Zaczyn — chat reference'])
        self.assertIn('# {{task name}}', chat)

    def test_release_links_match_version(self):
        import re
        root = Path(bundle.ROOT)
        documents = [root/'README.md', root/'START.md', root/'CONTRIBUTING.md', *sorted((root/'adapters').rglob('*.md'))]
        version = r'(\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?)'
        pattern = re.compile(r'zaczyn-[a-z-]*?' + version + r'\.zip|releases/(?:tag|download)/v' + version)
        for document in documents:
            for match in pattern.finditer(document.read_text(encoding='utf-8')):
                self.assertEqual(match.group(1) or match.group(2), self.version, document)

    def test_host_probe_files_match_their_source(self):
        import re
        import zipfile
        import build_probe as probe
        expected = probe.expected()
        on_disk = {p.relative_to(probe.PROBE).as_posix() for folder in probe.DERIVED
                   for p in (probe.PROBE/folder).rglob('*') if p.is_file()}
        self.assertEqual(on_disk, set(expected))
        for name, data in expected.items():
            self.assertEqual((probe.PROBE/name).read_bytes(), data, name)
        for skill in probe.SKILLS:
            header = (probe.PROBE/skill/'SKILL.md').read_text(encoding='utf-8').split('---')[1]
            self.assertRegex(header, r'(?m)^name: %s$' % skill)
            self.assertLessEqual(len(re.search(r'(?m)^description: (.+)$', header).group(1)), 1024)
        for name in expected:
            if name.endswith('.zip'):
                with zipfile.ZipFile(probe.PROBE/name) as archive:
                    files = {i.filename: archive.read(i) for i in archive.infolist() if not i.is_dir()}
                    self.assertTrue(all(i.external_attr >> 16 & 0o170000 in (0o100000, 0o040000)
                                        for i in archive.infolist()))
                self.assertIn('SKILL.md', files)
                self.assertEqual(Path(name).stem, re.search(r'(?m)^name: (.+)$', files['SKILL.md'].decode()).group(1))

    def test_broken_compiled_anchor_and_escaping_links_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = root/'ZACZYN.md'
            document.write_text('[missing](#absent)\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Broken compiled anchor'):
                bundle.check_links(root)
            document.write_text('[outside](../outside.md)\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Link escapes edition'):
                bundle.check_links(root)


if __name__ == '__main__':
    unittest.main()
