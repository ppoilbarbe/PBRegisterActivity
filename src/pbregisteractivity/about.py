"""
Dialogue Version
"""

import platform

import PySide6
from PySide6.QtCore import qVersion
from PySide6.QtWidgets import QDialog

from .ui_about import Ui_About


# noinspection PyAbstractClass
class About(QDialog, Ui_About):
    def __init__(self, version):
        super().__init__()
        self.setupUi(self)
        self.lblVersion.setText(version)
        self.lblPythonVersion.setText(platform.python_version())
        self.lblQtVersion.setText(qVersion())
        self.lblPySide6Version.setText(PySide6.__version__)
