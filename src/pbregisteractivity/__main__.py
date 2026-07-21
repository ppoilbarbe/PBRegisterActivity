#!/usr/bin/env python3

"""
Main program for PBRegisterActivity
"""

import argparse
import platform
import sys

import PySide6
from PySide6.QtCore import QLibraryInfo, QLocale, QTranslator, qVersion
from PySide6.QtWidgets import QApplication

from pbregisteractivity.activity import activities
from pbregisteractivity.mainwindow import MainWindow, version
from pbregisteractivity.parameters import parameters
from pbregisteractivity.platform import SingleInstance, SingleInstanceException, apply
from pbregisteractivity.resources import icon
from pbregisteractivity.utils import handle_gui_exception


def version_string() -> str:
    return (
        f"{parameters.application_name} {version}\n"
        f"Python : {platform.python_version()}\n"
        f"Qt : {qVersion()}\n"
        f"PySide6 : {PySide6.__version__}"
    )


class _VersionAction(argparse.Action):
    """Like argparse's built-in 'version' action, but prints the raw
    multi-line string as-is instead of rewrapping it through HelpFormatter
    (which collapses embedded newlines into spaces)."""

    def __init__(self, option_strings, dest=argparse.SUPPRESS, help=None):
        super().__init__(option_strings=option_strings, dest=dest, nargs=0, help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        print(version_string())
        parser.exit()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=parameters.application_name)
    parser.add_argument(
        "--version", action=_VersionAction, help="Affiche la version et quitte"
    )
    parser.add_argument(
        "--install",
        choices=["app", "autostart", "all", "none"],
        help=(
            "Enregistre l'application dans le système (app : menu ; "
            "autostart : démarrage automatique ; all : les deux) ou "
            "supprime cet enregistrement (none), puis quitte"
        ),
    )
    return parser.parse_args(argv)


_INSTALL_MESSAGES = {
    "app": "Application enregistrée dans le menu du système.",
    "autostart": "Démarrage automatique activé.",
    "all": (
        "Application enregistrée dans le menu du système et "
        "démarrage automatique activé."
    ),
    "none": "Enregistrement système supprimé (menu et démarrage automatique).",
}


def run_install(mode: str) -> None:
    apply(mode)
    print(_INSTALL_MESSAGES[mode])


def _load_bundled_fonts(app: QApplication) -> None:  # pragma: no cover
    """Register bundled fonts into Qt's font database (frozen builds only).

    In a PyInstaller onefile build, fontconfig uses paths hardcoded at build
    time that don't exist on the target machine.  QFontDatabase.addApplicationFont
    bypasses fontconfig entirely and guarantees that the bundled fonts (Ubuntu,
    DejaVu, …) are available regardless of the host fontconfig configuration.
    """
    if not getattr(sys, "frozen", False):
        return
    from pathlib import Path

    from PySide6.QtGui import QFont, QFontDatabase

    fonts_dir = Path(sys._MEIPASS) / "fonts"  # type: ignore[attr-defined]
    if not fonts_dir.is_dir():
        return

    loaded: set[str] = set()
    for ttf in sorted(fonts_dir.glob("*.ttf")):
        fid = QFontDatabase.addApplicationFont(str(ttf))
        if fid >= 0:
            loaded.update(QFontDatabase.applicationFontFamilies(fid))

    # Set Ubuntu as the default application font so the bundle renders
    # consistently on any machine, regardless of whether fontconfig finds
    # the system config.  The bundled libfontconfig.so has its default config
    # path hardcoded to the build machine's conda prefix, which does not exist
    # on target machines, so font selection cannot rely on fontconfig.
    if "Ubuntu" in loaded:
        current = app.font()
        app.setFont(
            QFont("Ubuntu", current.pointSize() if current.pointSize() > 0 else 10)
        )


def translate_stock_widgets(app: QApplication) -> None:
    locale_name = QLocale.system().name()
    qt_name = f"qt_{locale_name}"
    translator = QTranslator()
    translator.load(
        qt_name, QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    )
    app.installTranslator(translator)


def main():
    args = parse_args(sys.argv[1:])
    if args.install is not None:
        run_install(args.install)
        return

    try:
        locked = SingleInstance(parameters.unique_instance_lock_file)
    except SingleInstanceException:
        sys.exit(1)

    activities.load(parameters.activity_file)

    app = QApplication(sys.argv)
    _load_bundled_fonts(app)
    app.setWindowIcon(icon("pbregisteractivity.png", size=128))
    translate_stock_widgets(app)
    mw = MainWindow()
    mw.main()
    sys.excepthook = handle_gui_exception
    exitcode = app.exec()
    del locked
    sys.exit(exitcode)


if __name__ == "__main__":
    main()
