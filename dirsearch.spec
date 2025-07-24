# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['dirsearch.py'],
    pathex=[],
    binaries=[],
    datas=[('__init__.py', '.'), ('config.ini', '.'), ('dict.txt', '.'), ('options.ini', '.'), ('requirements.txt', '.'), ('setup.cfg', '.'), ('setup.py', '.'), ('db', 'db'), ('lib', 'lib'), ('static', 'static'), ('tests', 'tests')],
    hiddenimports=['optparse', 'PySocks', 'jinja2', 'defusedxml', 'OpenSSL', 'requests', 'requests_ntlm', 'colorama', 'ntlm_auth', 'bs4', 'mysql.connector', 'psycopg', 'defusedcsv', 'defusedcsv.csv', 'requests_toolbelt', 'requests_toolbelt.adapters.socket_options', 'setuptools', 'httpx', 'httpx_ntlm'],
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
    name='dirsearch',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
