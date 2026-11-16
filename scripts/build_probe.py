#!/usr/bin/env python3
"""Build the ready-to-use host probe files in probe/ from the probe sources."""
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / 'probe'
SKILL = PROBE / 'zaczyn-probe'
FOLDERS = {'vscode-agents': '.agents', 'vscode-github': '.github'}


def skill_files():
    return {p.relative_to(SKILL).as_posix(): p.read_bytes()
            for p in sorted(SKILL.rglob('*')) if p.is_file()}


def zip_bytes(files, target):
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)


def expected():
    """Return {path relative to probe/: bytes} for every derived file except the ZIP."""
    files = skill_files()
    derived = {'single-as-SKILL/SKILL.md': (PROBE / 'zaczyn-probe-single.md').read_bytes()}
    for folder, dot in FOLDERS.items():
        for name, data in files.items():
            derived['%s/%s/skills/zaczyn-probe/%s' % (folder, dot, name)] = data
    return derived


def build():
    for folder in ['single-as-SKILL', *FOLDERS]:
        shutil.rmtree(PROBE / folder, ignore_errors=True)
    for name, data in expected().items():
        target = PROBE / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    zip_bytes(skill_files(), PROBE / 'zaczyn-probe.zip')


if __name__ == '__main__':
    build()
    print('Built probe files in', PROBE)
