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
        Prefs.resize(376, 159)
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
        self.lblMinimizeTo = QtWidgets.QLabel(Prefs)
        self.lblMinimizeTo.setObjectName("lblMinimizeTo")
        self.layoutData.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblMinimizeTo)
        self.layoutMinimizeTo = QtWidgets.QHBoxLayout()
        self.layoutMinimizeTo.setSpacing(3)
        self.layoutMinimizeTo.setObjectName("layoutMinimizeTo")
        self.cbToTray = QtWidgets.QCheckBox(Prefs)
        self.cbToTray.setObjectName("cbToTray")
        self.layoutMinimizeTo.addWidget(self.cbToTray)
        self.lblReload1 = QtWidgets.QLabel(Prefs)
        self.lblReload1.setObjectName("lblReload1")
        self.layoutMinimizeTo.addWidget(self.lblReload1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutMinimizeTo.addItem(spacerItem2)
        self.layoutData.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.layoutMinimizeTo)
        self.layoutPrefs.addLayout(self.layoutData)
        self.lblReload = QtWidgets.QLabel(Prefs)
        self.lblReload.setObjectName("lblReload")
        self.layoutPrefs.addWidget(self.lblReload)
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
        self.lblMinimizeTo.setText(_translate("Prefs", "Minimiser en:"))
        self.cbToTray.setText(_translate("Prefs", "Zone de notification (Qt5.6 et plus)"))
        self.lblReload1.setText(_translate("Prefs", "<html><head/><body><p><span style=\" font-weight:600; color:#ff1414; vertical-align:super;\">*</span></p></body></html>"))
        self.lblReload.setText(_translate("Prefs", "<html><head/><body><p><span style=\" font-weight:600; color:#ff1414;\">* Nécessite un redémarrage</span></p></body></html>"))

from . import resources_rc
