# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for PBRegisterActivity.

The output name embeds the version and the target platform:

  Linux   → dist/pbregisteractivity-<version>-linux-x86_64
  Windows → dist/pbregisteractivity-<version>-windows-x86_64.exe
  macOS   → dist/pbregisteractivity-<version>-macos-arm64

Build with:  make dist
"""

import os
import platform
import sys
import tomllib
from pathlib import Path

from PyInstaller.utils.hooks import copy_metadata

# ---------------------------------------------------------------------------
# Version — from PBREGISTERACTIVITY_VERSION env var (set by `make dist` via
# tools/git_version.sh), falling back to pyproject.toml for direct
# `pyinstaller pbregisteractivity.spec` invocations.
# ---------------------------------------------------------------------------

_version = os.environ.get("PBREGISTERACTIVITY_VERSION")
if not _version:
    with open("pyproject.toml", "rb") as _f:
        _version = tomllib.load(_f)["project"]["version"]

# ---------------------------------------------------------------------------
# Platform tag  (OS-arch, e.g. linux-x86_64, windows-x86_64, macos-arm64)
# ---------------------------------------------------------------------------

_machine = platform.machine().lower()
_arch = {
    "x86_64":  "x86_64",
    "amd64":   "x86_64",
    "arm64":   "arm64",
    "aarch64": "arm64",
}.get(_machine, _machine)

if sys.platform == "linux":
    _os = "linux"
elif sys.platform == "win32":
    _os = "windows"
elif sys.platform == "darwin":
    _os = "macos"
else:
    _os = sys.platform

_artifact_name = f"pbregisteractivity-{_version}-{_os}-{_arch}"

# ---------------------------------------------------------------------------
# Data files to bundle
# ---------------------------------------------------------------------------

_datas = [
    (
        "src/pbregisteractivity/resources",
        "pbregisteractivity/resources",
    ),
    *copy_metadata("pbregisteractivity"),
]

# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

a = Analysis(
    ["src/pbregisteractivity/__main__.py"],
    pathex=["src"],
    datas=_datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=["tkinter"],
    noarchive=False,
)

pyz = PYZ(a.pure)

# ---------------------------------------------------------------------------
# Platform-specific packaging
# ---------------------------------------------------------------------------

if sys.platform == "darwin":
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name=_artifact_name,
        console=False,
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.datas,
        name=_artifact_name,
    )
    BUNDLE(
        coll,
        name=f"{_artifact_name}.app",
        bundle_identifier="net.cardolan.pbregisteractivity",
        info_plist={
            "NSHighResolutionCapable": True,
            "CFBundleShortVersionString": _version,
            "CFBundleName": "PBRegisterActivity",
        },
    )

else:
    # Linux / Windows: fichier unique autonome.
    EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        name=_artifact_name,
        console=False,
    )
