#!/usr/bin/env python3
"""Build the ready-to-use host probe files in probe/ from the probe sources.

Edit only the source folders probe/zaczyn-probe*/ and probe/zaczyn-probe-single.md,
then run this script; scripts/check_bundle.py fails if derived files drift.
"""
from io import BytesIO
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / 'probe'
SKILLS = ('zaczyn-probe-basic', 'zaczyn-probe-zip', 'zaczyn-probe-ref', 'zaczyn-probe')
VSCODE = {'vscode-agents': '.agents', 'vscode-github': '.github'}
DERIVED = ('upload', *VSCODE)
STAMP = (2026, 1, 1, 0, 0, 0)


def skill_files(skill='zaczyn-probe'):
    root = PROBE / skill
    return {p.relative_to(root).as_posix(): p.read_bytes()
            for p in sorted(root.rglob('*')) if p.is_file()}


def zip_bytes(files):
    """ZIP with SKILL.md at the root, directory entries and regular-file modes, like OS archivers."""
    folders = sorted({'/'.join(name.split('/')[:i]) + '/'
                      for name in files for i in range(1, name.count('/') + 1)})
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        for folder in folders:
            info = zipfile.ZipInfo(folder, date_time=STAMP)
            info.create_system = 3
            info.external_attr = (0o40755 << 16) | 0x10
            archive.writestr(info, b'')
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=STAMP)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def expected():
    """Return {path relative to probe/: bytes} for every derived file."""
    derived = {
        'upload/1-basic/SKILL.md': (PROBE / 'zaczyn-probe-basic/SKILL.md').read_bytes(),
        'upload/2-zip/zaczyn-probe-zip.zip': zip_bytes(skill_files('zaczyn-probe-zip')),
        'upload/3-reference/zaczyn-probe-ref.zip': zip_bytes(skill_files('zaczyn-probe-ref')),
        'upload/4-full/zaczyn-probe.zip': zip_bytes(skill_files('zaczyn-probe')),
        'upload/5-single/zaczyn-probe-single.md': (PROBE / 'zaczyn-probe-single.md').read_bytes(),
    }
    for folder, dot in VSCODE.items():
        for name, data in skill_files().items():
            derived['%s/%s/skills/zaczyn-probe/%s' % (folder, dot, name)] = data
    return derived


def build():
    for folder in DERIVED:
        shutil.rmtree(PROBE / folder, ignore_errors=True)
    for name, data in expected().items():
        target = PROBE / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


if __name__ == '__main__':
    build()
    print('Built probe files in', PROBE)
