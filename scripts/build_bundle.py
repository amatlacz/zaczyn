#!/usr/bin/env python3
"""Build native and chat editions from one core; no agent, installation, or publishing."""
import hashlib
import json
from pathlib import Path
import posixpath
import re
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SKILLS = ('zaczyn-setup', 'zaczyn-work', 'zaczyn-review', 'zaczyn-grow', 'zaczyn-orchestrate')
EXPECTED = set(PUBLIC_SKILLS)
HOSTS = ('claude-project', 'codex', 'antigravity', 'kiro', 'vscode-copilot')
# Skills shipped as one self-contained file for apps that cannot install a folder.
SINGLE_SKILLS = ('zaczyn-setup', 'zaczyn-work', 'zaczyn-review', 'zaczyn-grow')
# Characters, measured without the build stamp. Microsoft recommends keeping a Copilot Chat SKILL.md under
# about 20,000. Review, work, and grow stay below that; setup is about 22,000 because it carries the discovery,
# customization, and template references it needs. Cowork accepts up to 1 MB. The limit stops further growth.
SINGLE_LIMIT = 24000
BUNDLE_SOURCES = ['.claude-plugin/plugin.json', 'VERSION', 'LICENSE', 'START.md',
                  'core', 'adapters', 'docs/field-guide', 'docs/migration.md',
                  'docs/verification.md', 'examples/attendance-summary', 'examples/guided-setup']
LINK = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
SPEC_KEYS = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
SKILL_NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
UNSAFE_START = tuple('\'"!&*?|>%@`{}[],#-:')


def check_skill_file(text, folder, label):
    """Agent Skills frontmatter rules that strict hosts enforce, checked without a YAML library."""
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('Missing frontmatter: ' + label)
    header, body = text[4:].split('\n---\n', 1)
    keys = [line.split(':', 1)[0] for line in header.splitlines() if line and not line[0].isspace()]
    if len(keys) != len(set(keys)) or set(keys) - SPEC_KEYS:
        raise ValueError('Frontmatter keys must be unique Agent Skills fields: ' + label)
    name = re.search(r'^name: (.*)$', header, re.M)
    if not name or not SKILL_NAME.fullmatch(name.group(1)) or len(name.group(1)) > 64 or name.group(1) != folder:
        raise ValueError('Skill name must be lowercase words joined by hyphens and match its folder: ' + label)
    description = re.search(r'^description: (.*)$', header, re.M)
    value = description.group(1) if description else ''
    if not 1 <= len(value) <= 1024:
        raise ValueError('Skill description must be 1-1024 characters: ' + label)
    if (value.startswith(UNSAFE_START) or value.rstrip().endswith(':') or re.search(r':\s|\s#', value)
            or '<' in value or '>' in value):
        raise ValueError('Skill description is not a safe one-line YAML value: ' + label)
    compatibility = re.search(r'^compatibility: (.*)$', header, re.M)
    if compatibility and not 1 <= len(compatibility.group(1)) <= 500:
        raise ValueError('Skill compatibility must be 1-500 characters: ' + label)
    metadata = re.search(r'^metadata:(.*)\n?((?:[ \t]+.*\n?)*)', header, re.M)
    if metadata and (metadata.group(1).strip() or not metadata.group(2).strip()
                     or not all(re.fullmatch(r'[ \t]+[A-Za-z0-9_-]+: \S.*', line)
                                for line in metadata.group(2).splitlines() if line.strip())):
        raise ValueError('Skill metadata must be a mapping of string values: ' + label)
    if len(body.splitlines()) > 500:
        raise ValueError('Skill body exceeds 500 lines: ' + label)


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
            compiled = destination.name == 'ZACZYN.md' or (destination.parent == root.resolve() and destination.name.startswith('zaczyn-'))
            if compiled and parsed.fragment:
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
        raise ValueError('Bundle skills differ from declared public skills')
    for path in skills:
        check_skill_file(path.read_text(encoding='utf-8'), path.parent.name, str(path))
    check_links(root)
    return version


def native_payload():
    payload = {}
    for source in BUNDLE_SOURCES:
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


def closure(native, skill, runtime, keep):
    """Follow resource links from one skill. keep(source, resolved) decides which links stay links;
    others become plain text. Returns the visited sources in discovery order and a link rewriter."""
    entry = 'core/skills/' + skill + '/SKILL.md'
    order, pending, seen = [], [entry], set()
    while pending:
        source = pending.pop(0)
        if source in seen:
            continue
        seen.add(source)
        if source not in native:
            raise ValueError('Missing native resource: ' + source)
        order.append(source)
        for _, link in LINK.findall(native[source].decode()):
            resolved = resolve(source, link, runtime)
            if resolved and keep(source, resolved):
                pending.append(resolved)
    return order


def resolve(source, link, runtime):
    parsed = urlsplit(link.strip('<>'))
    if parsed.scheme or parsed.netloc:
        return None
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parsed.path))) if parsed.path else source
    # Portable core's adapter index resolves to the selected host only.
    return runtime if resolved == 'adapters/README.md' else resolved


def keeps_link(skill, single=False):
    def keep(source, resolved):
        # The orchestration guide is needed only by the orchestration skill.
        if resolved == 'adapters/orchestration.md':
            return skill == 'zaczyn-orchestrate'
        # A single file mentions other skills by name instead of embedding them.
        if single and resolved.endswith('/SKILL.md') and resolved != 'core/skills/' + skill + '/SKILL.md':
            return False
        return True
    return keep


def rewrite_links(body, source, runtime, keep, target_of):
    def rewrite(match):
        label, link = match.groups()
        resolved = resolve(source, link, runtime)
        if resolved is None:
            return match.group(0)
        if not keep(source, resolved):
            return label
        parsed = urlsplit(link.strip('<>'))
        return '[' + label + '](' + target_of(resolved, parsed) + ')'
    return LINK.sub(rewrite, body)


def strip_frontmatter(body):
    return body.split('---', 2)[2].lstrip() if body.startswith('---\n') else body


def skill_payload(native, skill):
    """Relocate one skill's link closure into a flat installable folder: SKILL.md plus references/<name>.md."""
    entry = 'core/skills/' + skill + '/SKILL.md'
    runtime = 'adapters/native/runtime.md'
    keep = keeps_link(skill)

    def destination(source):
        if source == entry:
            return 'SKILL.md'
        if source == runtime:
            return 'references/host.md'
        if source == 'adapters/orchestration.md':
            return 'references/orchestration.md'
        if not source.startswith('core/'):
            raise ValueError('Unbundled native reference: ' + source)
        parts = source.split('/')
        if parts[-1] == 'SKILL.md':
            return 'references/' + parts[-2] + '.md'
        if parts[1] == 'assets':
            return 'references/' + parts[-1][:-3] + '-template.md'
        return 'references/' + parts[-1]

    result, owners = {}, {}
    for source in closure(native, skill, runtime, keep):
        target = destination(source)
        if owners.setdefault(target, source) != source:
            raise ValueError('Two resources flatten to %s: %s, %s' % (target, owners[target], source))

        def target_of(resolved, parsed, target=target):
            relative = posixpath.relpath(destination(resolved), posixpath.dirname(target) or '.')
            return relative + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')

        body = native[source].decode()
        if source != entry and source.endswith('/SKILL.md'):
            body = strip_frontmatter(body)
        result[target] = rewrite_links(body, source, runtime, keep, target_of).encode()
    result['VERSION'] = native['VERSION']
    return result


def demote(body):
    """Push Markdown headings one level down, outside fenced code."""
    lines, fenced = [], False
    for line in body.splitlines():
        if line.startswith('```'):
            fenced = not fenced
        if not fenced and re.match(r'#{1,5} ', line):
            line = '#' + line
        lines.append(line)
    return '\n'.join(lines)


def compiled_section(name, body):
    """A reference section for a compiled edition: templates verbatim in a fence, other text demoted."""
    if name.startswith('core/assets/'):
        return '## ' + section_title(name, body) + '\n\nCopy this template and fill it in; keep its headings.\n\n````markdown\n' + body.rstrip() + '\n````'
    return demote(strip_frontmatter(body))


def outside_fences(text):
    lines, fenced = [], False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced = not fenced
            continue
        if not fenced:
            lines.append(line)
    return lines


def section_title(name, body):
    if name.startswith('core/assets/'):
        return 'Template: ' + name.rsplit('/', 1)[1]
    return next(line.lstrip('# ') for line in body.splitlines() if line.startswith('# '))


def single_payload(native, version):
    """One self-contained Markdown skill per selected skill, with in-file anchors."""
    runtime = 'adapters/single-file/runtime.md'
    result = {'README.md': native['adapters/single-file/README.md'].replace(b'../../docs/verification.md', b'verification.md'),
              'verification.md': native['docs/verification.md'],
              'VERSION': version.encode() + b'\n', 'LICENSE': native['LICENSE']}
    for skill in SINGLE_SKILLS:
        entry = 'core/skills/' + skill + '/SKILL.md'
        keep = keeps_link(skill, single=True)
        order = closure(native, skill, runtime, keep)
        if runtime not in order:
            order.append(runtime)

        def target_of(resolved, parsed):
            if parsed.fragment:
                raise ValueError('Map section-specific links explicitly before compiling: ' + resolved)
            return '#' + section_id(resolved)

        header, body = native[entry].decode()[4:].split('\n---\n', 1)
        fields = [line for line in header.splitlines() if line.startswith(('name: ', 'description: '))]
        parts = ['---', *fields, '---', '', rewrite_links(body.lstrip(), entry, runtime, keep, target_of).rstrip(),
                 '', '---', '', '*Zaczyn ' + version + ', single-file edition. The sections below are this skill\'s references.*']
        for source in order[1:]:
            text = compiled_section(source, rewrite_links(native[source].decode(), source, runtime, keep, target_of))
            parts += ['', '<a id="' + section_id(source) + '"></a>', '', text.rstrip()]
        document = '\n'.join(parts) + '\n'
        if len(document) - len(version) > SINGLE_LIMIT:
            raise ValueError('%s single file has %d characters; limit %d' % (skill, len(document) - len(version), SINGLE_LIMIT))
        result[skill + '.md'] = document.encode()
    return result


def check_single_tree(root):
    for skill in SINGLE_SKILLS:
        path = root / (skill + '.md')
        check_skill_file(path.read_text(encoding='utf-8'), skill, str(path))
    if list(root.rglob('SKILL.md')) or list(root.rglob('AGENTS.md')):
        raise ValueError('Single-file edition must not contain active skill or context files')
    check_links(root)


def library_skills():
    return sorted(p.parent.name for p in (ROOT / 'library').glob('*/SKILL.md'))


def library_payload(native, version):
    """Optional standalone skills; read separately so core editions never depend on them."""
    readme = (ROOT / 'library/README.md').read_bytes()
    readme = readme.replace(b'../docs/verification.md', b'verification.md')
    readme = readme.replace(b'../CONTRIBUTING.md', b'https://github.com/amatlacz/zaczyn/blob/main/CONTRIBUTING.md')
    result = {'README.md': readme, 'verification.md': native['docs/verification.md'],
              'VERSION': version.encode() + b'\n', 'LICENSE': native['LICENSE']}
    for skill in library_skills():
        for path in sorted((ROOT / 'library' / skill).rglob('*')):
            if path.is_file():
                result[skill + '/' + path.relative_to(ROOT / 'library' / skill).as_posix()] = path.read_bytes()
    return result


def check_library_tree(root):
    entries = sorted(root.glob('*/SKILL.md'))
    if not entries or set(root.rglob('SKILL.md')) != set(entries):
        raise ValueError('Library skills must be top-level folders with one SKILL.md each')
    for entry in entries:
        text = entry.read_text(encoding='utf-8')
        check_skill_file(text, entry.parent.name, str(entry))
        if entry.parent.name.startswith('zaczyn-'):
            raise ValueError('Library skills do not use the base prefix: ' + entry.parent.name)
        local = [target for _, target in LINK.findall(text) if not urlsplit(target).scheme]
        if local:
            raise ValueError('Library skills must be self-contained: %s -> %s' % (entry, local[0]))
    check_links(root)


def host_payload(native, host, version=None):
    stamped = native['VERSION'] if version is None else version.encode() + b'\n'
    guide = native['adapters/' + host + '/README.md']
    guide = guide.replace(b'../../docs/verification.md', b'verification.md')
    guide = guide.replace(b'../orchestration.md', b'orchestration.md')
    result = {'README.md': guide,
              'VERSION': stamped, 'LICENSE': native['LICENSE'],
              'verification.md': native['docs/verification.md'],
              'orchestration.md': native['adapters/orchestration.md']}
    for skill in sorted(EXPECTED):
        for path, content in skill_payload(native, skill).items():
            result['skills/' + skill + '/' + path] = stamped if path == 'VERSION' else content
    return result


def check_host_tree(root):
    entries = sorted((root / 'skills').glob('*/SKILL.md'))
    if {p.parent.name for p in entries} != EXPECTED:
        raise ValueError('Native export skills differ from declared public skills')
    if set(root.rglob('SKILL.md')) != set(entries):
        raise ValueError('Supporting procedures became discoverable skills')
    if list(root.rglob('AGENTS.md')) or list(root.rglob('AGENTS.override.md')):
        raise ValueError('A bundled template would become active workspace context')
    for entry in entries:
        check_skill_file(entry.read_text(encoding='utf-8'), entry.parent.name, str(entry))
        nested = [p for p in entry.parent.rglob('*') if p.is_file() and len(p.relative_to(entry.parent).parts) > 2]
        if nested:
            raise ValueError('Skill references must be one level deep: ' + str(nested[0]))
        if (entry.parent / 'VERSION').read_bytes() != (root / 'VERSION').read_bytes():
            raise ValueError('Mixed exported skill versions')
        # A host can import just this folder; no sibling or checkout dependency.
        check_links(entry.parent)
    check_links(root)


def chat_payload(native, version, stamp=None):
    runtime = 'adapters/chatgpt/runtime.md'
    ordered = [runtime, 'core/references/workspace.md']
    ordered += ['core/skills/'+name+'/SKILL.md' for name in PUBLIC_SKILLS]
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
    lines = ['# Zaczyn — chat reference', '', 'Version: '+(stamp or version),
             'Generated from the portable core and chat runtime. Source digest: `'+digest+'`.',
             'Keep this shipped reference separate from your personal AGENTS/PROJECT documents. Templates below are examples to fill, not already saved user context.',
             '', '## Contents']
    for name in ordered:
        lines.append('- ['+section_title(name, native[name].decode())+'](#'+section_id(name)+')')
    for name in ordered:
        body = compiled_section(name, LINK.sub(lambda m: rewrite(name,m), native[name].decode()))
        lines += ['', '<a id="'+section_id(name)+'"></a>', '', body]
    result = {
        'ZACZYN.md': ('\n'.join(lines)+'\n').encode(),
        'PROJECT-INSTRUCTIONS.txt': native['adapters/chatgpt/PROJECT-INSTRUCTIONS.txt'],
        'START.md': native['adapters/chatgpt/README.md'].replace(b'../../docs/verification.md',b'verification.md').replace(b'../orchestration.md',b'orchestration.md'),
        'verification.md': native['docs/verification.md'],
        'orchestration.md': native['adapters/orchestration.md'],
        'VERSION': native['VERSION'] if stamp is None else stamp.encode() + b'\n', 'LICENSE': native['LICENSE'],
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


def build_stamp(version):
    """Version plus source commit, so an installed copy shows which build it came from."""
    try:
        commit = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', '--short=12', 'HEAD'],
                                capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(['git', '-C', str(ROOT), 'status', '--porcelain', '--untracked-files=all', '--', *BUNDLE_SOURCES, 'library'],
                               capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return version + '+unknown'
    return version + '+g' + commit + ('.dirty' if dirty else '')


def build():
    version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?',version):raise ValueError('Unsafe semantic version')
    stamp=build_stamp(version)
    native=native_payload()
    chat=chat_payload(native,version,stamp)
    editions={'plugin':(native,'zaczyn-'+version+'.zip',check_tree),
              'chat':(chat,'zaczyn-chat-'+version+'.zip',check_links),
              'single':(single_payload(native,stamp),'zaczyn-single-'+version+'.zip',check_single_tree),
              'library':(library_payload(native,stamp),'zaczyn-library-'+version+'.zip',check_library_tree)}
    for host in HOSTS:
        editions[host]=(host_payload(native,host,stamp),'zaczyn-'+host+'-'+version+'.zip',check_host_tree)
    catalog={'version':version,'build':stamp,'skills':[],'artifacts':[]}
    for skill in PUBLIC_SKILLS:
        header=native['core/skills/'+skill+'/SKILL.md'].decode().split('---',2)[1]
        catalog['skills'].append({'name':skill,'description':re.search(r'^description: (.*)$',header,re.M).group(1),
                                  'single_file':skill in SINGLE_SKILLS})
    catalog['library']=[]
    for skill in library_skills():
        header=(ROOT/'library'/skill/'SKILL.md').read_text(encoding='utf-8').split('---',2)[1]
        catalog['library'].append({'name':skill,'description':re.search(r'^description: (.*)$',header,re.M).group(1)})
    for edition,(payload,name,checker) in editions.items():
        write_zip(payload,ROOT/'dist'/name,checker)
        data=(ROOT/'dist'/name).read_bytes()
        catalog['artifacts'].append({'edition':edition,'file':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    (ROOT/'dist'/'catalog.json').write_text(json.dumps(catalog,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('Checked all extracted editions, independent skill references, manifests, and checksums. This is structure validation, not a host or novice test.')


if __name__=='__main__':
    build()
