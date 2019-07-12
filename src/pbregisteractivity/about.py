# -*- coding: utf-8 -*-
"""
Dialogue Version
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import sys

from PyQt5.Qt import PYQT_VERSION_STR
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.QtWidgets import QDialog

from .ui.ui_about import Ui_About


# noinspection PyAbstractClass
class About(QDialog, Ui_About):
    def __init__(self, version):
        super().__init__()
        self.setupUi(self)
        self.lblVersion.setText(version)
        self.lblQtVersion.setText(QT_VERSION_STR)
        self.lblPythonVersion.setText(sys.version)
        self.lblPyQtVersion.setText(PYQT_VERSION_STR)
