# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_prefs.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Prefs(object):
    def setupUi(self, Prefs):
        Prefs.setObjectName("Prefs")
        Prefs.resize(208, 115)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Prefs.setWindowIcon(icon)
        self.layoutPrefs = QtWidgets.QVBoxLayout(Prefs)
        self.layoutPrefs.setObjectName("layoutPrefs")
        self.layoutData = QtWidgets.QFormLayout()
        self.layoutData.setObjectName("layoutData")
        self.lblDayDuration = QtWidgets.QLabel(Prefs)
        self.lblDayDuration.setObjectName("lblDayDuration")
        self.layoutData.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblDayDuration)
        self.layoutDayDuration = QtWidgets.QHBoxLayout()
        self.layoutDayDuration.setObjectName("layoutDayDuration")
        self.spinDayDuration = QtWidgets.QSpinBox(Prefs)
        self.spinDayDuration.setMinimum(1)
        self.spinDayDuration.setMaximum(24)
        self.spinDayDuration.setObjectName("spinDayDuration")
        self.layoutDayDuration.addWidget(self.spinDayDuration)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutDayDuration.addItem(spacerItem)
        self.layoutData.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.layoutDayDuration)
        self.layoutPrefs.addLayout(self.layoutData)
        self.buttonBox = QtWidgets.QDialogButtonBox(Prefs)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutPrefs.addWidget(self.buttonBox)

        self.retranslateUi(Prefs)
        self.buttonBox.accepted.connect(Prefs.accept)
        self.buttonBox.rejected.connect(Prefs.reject)
        QtCore.QMetaObject.connectSlotsByName(Prefs)

    def retranslateUi(self, Prefs):
        _translate = QtCore.QCoreApplication.translate
        Prefs.setWindowTitle(_translate("Prefs", "Préférences"))
        self.lblDayDuration.setText(_translate("Prefs", "Durée du jour:"))
        self.spinDayDuration.setToolTip(_translate("Prefs", "Durée du jour de travail en heures"))

from . import resources_rc
