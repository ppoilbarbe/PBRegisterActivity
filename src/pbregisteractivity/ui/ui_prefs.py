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
        Prefs.resize(262, 117)
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
        self.lblMisc = QtWidgets.QLabel(Prefs)
        self.lblMisc.setObjectName("lblMisc")
        self.layoutData.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblMisc)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinMisc = QtWidgets.QSpinBox(Prefs)
        self.spinMisc.setMaximum(1440)
        self.spinMisc.setSingleStep(15)
        self.spinMisc.setObjectName("spinMisc")
        self.horizontalLayout.addWidget(self.spinMisc)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.layoutData.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
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
        self.spinDayDuration.setSuffix(_translate("Prefs", "h"))
        self.lblMisc.setText(_translate("Prefs", "Divers si durée:"))
        self.spinMisc.setToolTip(_translate("Prefs", "Durée en dessous de laquelle une activité\n"
"est regroupée en tant que \"Divers\".\n"
"Si 0, il n\'y a pas de regroupement."))
        self.spinMisc.setSuffix(_translate("Prefs", "min"))
        self.spinMisc.setPrefix(_translate("Prefs", "< "))

from . import resources_rc
