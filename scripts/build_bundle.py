#!/usr/bin/env python3
"""Build native and chat editions from one core; no agent, installation, or publishing."""
import hashlib
import json
from pathlib import Path
import posixpath
import re
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'zaczyn-setup', 'zaczyn-work', 'zaczyn-review', 'zaczyn-grow'}
HOSTS = ('claude-project', 'codex', 'antigravity', 'kiro')
LINK = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def check_links(root):
    for path in root.rglob('*.md'):
        for _, target in LINK.findall(path.read_text(encoding='utf-8')):
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            try:
                destination.relative_to(root.resolve())
            except ValueError:
                raise ValueError('Link escapes edition: %s -> %s' % (path, target))
            if not destination.is_file():
                raise ValueError('Broken file link: %s -> %s' % (path, target))
            if destination.name == 'ZACZYN.md' and parsed.fragment:
                if 'id="'+parsed.fragment+'"' not in destination.read_text(encoding='utf-8'):
                    raise ValueError('Broken compiled anchor: ' + target)


def check_tree(root):
    manifest = json.loads((root / '.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    version = (root / 'VERSION').read_text(encoding='utf-8').strip()
    if manifest['name'] != 'zaczyn' or manifest['version'] != version:
        raise ValueError('Manifest name/version differs from the bundle')
    if manifest['skills'] != './core/skills/':
        raise ValueError('Unexpected skill directory')
    skills = list((root / 'core/skills').glob('*/SKILL.md'))
    if {p.parent.name for p in skills} != EXPECTED:
        raise ValueError('Bundle must contain exactly the four public skills')
    for path in skills:
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            raise ValueError('Missing frontmatter: ' + str(path))
        header = text.split('---', 2)[1]
        name = re.search(r'^name: (.+)$', header, re.M)
        if not name or name.group(1) != path.parent.name:
            raise ValueError('Skill name must match its folder: ' + str(path))
        if not re.search(r'^description: .+', header, re.M):
            raise ValueError('Missing skill description: ' + str(path))
    check_links(root)
    return version


def native_payload():
    payload = {}
    sources = ['.claude-plugin/plugin.json', 'VERSION', 'LICENSE', 'START.md',
               'core', 'adapters', 'docs/field-guide', 'docs/migration.md',
               'docs/verification.md', 'examples/attendance-summary', 'examples/guided-setup']
    for source in sources:
        path = ROOT / source
        if not path.exists():
            raise ValueError('Missing bundle source: ' + source)
        if path.is_symlink():
            raise ValueError('Source is a symlink: ' + source)
        for file in sorted(path.rglob('*')) if path.is_dir() else [path]:
            if file.is_symlink():
                raise ValueError('Bundle sources must not be symlinks: ' + str(file))
            if file.is_file():
                if file.suffix not in {'.md', '.json', '.csv', '.txt'} and file.name not in {'LICENSE', 'VERSION'}:
                    raise ValueError('Unexpected bundle file: ' + str(file))
                payload[file.relative_to(ROOT).as_posix()] = file.read_bytes()
    payload['README.md'] = payload['START.md']
    return payload


def section_id(name):
    return 'source-' + re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def skill_payload(native, skill):
    """Follow resource links and relocate their closure inside one installable skill."""
    entry = 'core/skills/' + skill + '/SKILL.md'
    runtime = 'adapters/native/runtime.md'

    def destination(source):
        if source == entry:
            return 'SKILL.md'
        if source == runtime:
            return 'references/host.md'
        if not source.startswith('core/'):
            raise ValueError('Unbundled native reference: ' + source)
        path = 'references/' + source
        if path.endswith('/SKILL.md'):
            path = path[:-len('SKILL.md')] + 'procedure.md'
        if path.endswith('/AGENTS.md'):
            path = path[:-len('AGENTS.md')] + 'AGENTS-template.md'
        return path

    pending, result, seen = [entry], {}, set()
    while pending:
        source = pending.pop()
        if source in seen:
            continue
        seen.add(source)
        if source not in native:
            raise ValueError('Missing native resource: ' + source)
        target = destination(source)

        def rewrite(match):
            label, link = match.groups()
            parsed = urlsplit(link.strip('<>'))
            if parsed.scheme or parsed.netloc:
                return match.group(0)
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parsed.path))) if parsed.path else source
            # Portable core's adapter index resolves to the selected host only.
            if resolved == 'adapters/README.md':
                resolved = runtime
            local = destination(resolved)
            pending.append(resolved)
            relative = posixpath.relpath(local, posixpath.dirname(target) or '.')
            suffix = ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')
            return '[' + label + '](' + relative + suffix + ')'

        body = native[source].decode()
        if source != entry and source.endswith('/SKILL.md'):
            body = body.split('---', 2)[2].lstrip()
        result[target] = LINK.sub(rewrite, body).encode()
    result['VERSION'] = native['VERSION']
    return result


def host_payload(native, host):
    result = {'README.md': native['adapters/' + host + '/README.md'].replace(b'../../docs/verification.md', b'verification.md'),
              'VERSION': native['VERSION'], 'LICENSE': native['LICENSE'],
              'verification.md': native['docs/verification.md']}
    for skill in sorted(EXPECTED):
        for path, content in skill_payload(native, skill).items():
            result['skills/' + skill + '/' + path] = content
    return result


def check_host_tree(root):
    entries = sorted((root / 'skills').glob('*/SKILL.md'))
    if {p.parent.name for p in entries} != EXPECTED:
        raise ValueError('Native export must have exactly four skill entries')
    if set(root.rglob('SKILL.md')) != set(entries):
        raise ValueError('Supporting procedures became discoverable skills')
    if list(root.rglob('AGENTS.md')) or list(root.rglob('AGENTS.override.md')):
        raise ValueError('A bundled template would become active workspace context')
    for entry in entries:
        header = entry.read_text(encoding='utf-8').split('---', 2)
        if len(header) != 3 or not re.search(r'^name: ' + re.escape(entry.parent.name) + r'$', header[1], re.M):
            raise ValueError('Bad exported skill name: ' + str(entry))
        if not re.search(r'^description: .+', header[1], re.M):
            raise ValueError('Missing exported description: ' + str(entry))
        if (entry.parent / 'VERSION').read_bytes() != (root / 'VERSION').read_bytes():
            raise ValueError('Mixed exported skill versions')
        # A host can import just this folder; no sibling or checkout dependency.
        check_links(entry.parent)
    check_links(root)


def chat_payload(native, version):
    runtime = 'adapters/chatgpt/runtime.md'
    ordered = [runtime, 'core/references/workspace.md']
    ordered += ['core/skills/'+name+'/SKILL.md' for name in ['zaczyn-setup','zaczyn-work','zaczyn-review','zaczyn-grow']]
    ordered += sorted(n for n in native if n.startswith('core/') and n.endswith('.md') and n not in ordered)
    def rewrite(source, match):
        label, target = match.groups()
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            return match.group(0)
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parsed.path))) if parsed.path else source
        # Host discovery/saving instructions in the core resolve to this edition's runtime.
        if resolved.startswith('adapters/'):
            resolved = runtime
        if resolved not in ordered:
            raise ValueError('Unbundled chat reference: %s -> %s' % (source, target))
        if parsed.fragment:
            raise ValueError('Map section-specific core links explicitly before compiling: ' + target)
        return '['+label+'](#'+section_id(resolved)+')'
    digest = hashlib.sha256(b''.join(n.encode()+b'\0'+native[n] for n in ordered)).hexdigest()
    lines = ['# Zaczyn — chat reference', '', 'Version: '+version,
             'Generated from the portable core and chat runtime. Source digest: `'+digest+'`.',
             'Keep this shipped reference separate from your personal AGENTS/PROJECT documents. Templates below are examples to fill, not already saved user context.',
             '', '## Contents']
    for name in ordered:
        title = next(line.lstrip('# ') for line in native[name].decode().splitlines() if line.startswith('# '))
        lines.append('- ['+title+'](#'+section_id(name)+')')
    for name in ordered:
        body = native[name].decode()
        if body.startswith('---\n'):
            body = body.split('---',2)[2].lstrip()
        body = LINK.sub(lambda m: rewrite(name,m), body)
        lines += ['', '<a id="'+section_id(name)+'"></a>', '', body]
    result = {
        'ZACZYN.md': ('\n'.join(lines)+'\n').encode(),
        'PROJECT-INSTRUCTIONS.txt': native['adapters/chatgpt/PROJECT-INSTRUCTIONS.txt'],
        'START.md': native['adapters/chatgpt/README.md'].replace(b'../../docs/verification.md',b'verification.md'),
        'verification.md': native['docs/verification.md'],
        'VERSION': native['VERSION'], 'LICENSE': native['LICENSE'],
    }
    return result


def write_zip(payload, destination, checker):
    with tempfile.TemporaryDirectory(prefix='zaczyn-build-') as temporary:
        staged = Path(temporary)/'staged'
        for relative, content in payload.items():
            p=staged/relative;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(content)
        checker(staged)
        archive_path=Path(temporary)/destination.name
        with zipfile.ZipFile(archive_path,'w',compression=zipfile.ZIP_DEFLATED) as archive:
            for relative,content in sorted(payload.items()):
                info=zipfile.ZipInfo(relative,(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
                archive.writestr(info,content)
        extracted=Path(temporary)/'extracted'
        with zipfile.ZipFile(archive_path) as archive:
            if archive.testzip() is not None:raise ValueError('Archive CRC failure')
            archive.extractall(extracted)
        checker(extracted)
        if any((extracted/n).read_bytes()!=b for n,b in payload.items()):raise ValueError('Extraction changed contents')
        destination.parent.mkdir(exist_ok=True)
        destination.write_bytes(archive_path.read_bytes())
    digest=hashlib.sha256(destination.read_bytes()).hexdigest()
    destination.with_suffix('.zip.sha256').write_text(digest+'  '+destination.name+'\n', encoding='utf-8')
    print('Built %s: %d files, %d bytes; SHA256 %s' % (destination.name,len(payload),destination.stat().st_size,digest))


def build():
    version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?',version):raise ValueError('Unsafe semantic version')
    native=native_payload()
    chat=chat_payload(native,version)
    write_zip(native,ROOT/'dist'/('zaczyn-'+version+'.zip'),check_tree)
    write_zip(chat,ROOT/'dist'/('zaczyn-chat-'+version+'.zip'),check_links)
    for host in HOSTS:
        write_zip(host_payload(native, host), ROOT/'dist'/('zaczyn-'+host+'-'+version+'.zip'), check_host_tree)
    print('Checked all extracted editions, independent skill references, manifests, and checksums. This is structure validation, not a host or novice test.')


if __name__=='__main__':
    build()
