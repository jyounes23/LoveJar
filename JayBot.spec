# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['jaybotv2.py'],
    pathex=[],
    binaries=[],
    datas=[('jar_image.jpeg', '.'), ('logo.jpg', '.'), ('messages', 'messages')],
    hiddenimports=['PIL', 'numpy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='JayBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='universal2',
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='JayBot.app',
    icon=None,
    bundle_identifier=None,
)
