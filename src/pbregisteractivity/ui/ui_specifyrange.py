# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_specifyrange.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpecifyRange(object):
    def setupUi(self, SpecifyRange):
        SpecifyRange.setObjectName("SpecifyRange")
        SpecifyRange.resize(584, 262)
        self.layoutDialog = QtWidgets.QVBoxLayout(SpecifyRange)
        self.layoutDialog.setObjectName("layoutDialog")
        self.lblTitle = QtWidgets.QLabel(SpecifyRange)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblTitle.setTextFormat(QtCore.Qt.PlainText)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.layoutDialog.addWidget(self.lblTitle)
        self.layoutInput = QtWidgets.QFormLayout()
        self.layoutInput.setObjectName("layoutInput")
        self.lblStart = QtWidgets.QLabel(SpecifyRange)
        self.lblStart.setObjectName("lblStart")
        self.layoutInput.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblStart)
        self.dteStart = QtWidgets.QDateTimeEdit(SpecifyRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dteStart.sizePolicy().hasHeightForWidth())
        self.dteStart.setSizePolicy(sizePolicy)
        self.dteStart.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.dteStart.setCalendarPopup(True)
        self.dteStart.setObjectName("dteStart")
        self.layoutInput.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dteStart)
        self.lblDuration = QtWidgets.QLabel(SpecifyRange)
        self.lblDuration.setObjectName("lblDuration")
        self.layoutInput.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDuration)
        self.layoutDuration = QtWidgets.QHBoxLayout()
        self.layoutDuration.setObjectName("layoutDuration")
        self.sbDayDuration = QtWidgets.QSpinBox(SpecifyRange)
        self.sbDayDuration.setMaximum(10)
        self.sbDayDuration.setObjectName("sbDayDuration")
        self.layoutDuration.addWidget(self.sbDayDuration)
        self.timeDuration = QtWidgets.QTimeEdit(SpecifyRange)
        self.timeDuration.setObjectName("timeDuration")
        self.layoutDuration.addWidget(self.timeDuration)
        self.lblEndText = QtWidgets.QLabel(SpecifyRange)
        self.lblEndText.setObjectName("lblEndText")
        self.layoutDuration.addWidget(self.lblEndText)
        self.layoutDuration.setStretch(2, 1)
        self.layoutInput.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.layoutDuration)
        self.lblComment = QtWidgets.QLabel(SpecifyRange)
        self.lblComment.setObjectName("lblComment")
        self.layoutInput.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.edtComment = QtWidgets.QPlainTextEdit(SpecifyRange)
        self.edtComment.setObjectName("edtComment")
        self.layoutInput.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.edtComment)
        self.lblName = QtWidgets.QLabel(SpecifyRange)
        self.lblName.setObjectName("lblName")
        self.layoutInput.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.edtName = QtWidgets.QLineEdit(SpecifyRange)
        self.edtName.setObjectName("edtName")
        self.layoutInput.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edtName)
        self.layoutDialog.addLayout(self.layoutInput)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutDialog.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(SpecifyRange)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutDialog.addWidget(self.buttonBox)

        self.retranslateUi(SpecifyRange)
        self.buttonBox.accepted.connect(SpecifyRange.accept)
        self.buttonBox.rejected.connect(SpecifyRange.reject)
        QtCore.QMetaObject.connectSlotsByName(SpecifyRange)
        SpecifyRange.setTabOrder(self.edtName, self.dteStart)
        SpecifyRange.setTabOrder(self.dteStart, self.sbDayDuration)
        SpecifyRange.setTabOrder(self.sbDayDuration, self.timeDuration)
        SpecifyRange.setTabOrder(self.timeDuration, self.edtComment)

    def retranslateUi(self, SpecifyRange):
        _translate = QtCore.QCoreApplication.translate
        SpecifyRange.setWindowTitle(_translate("SpecifyRange", "Dialog"))
        self.lblTitle.setText(_translate("SpecifyRange", "TextLabel"))
        self.lblStart.setText(_translate("SpecifyRange", "Heure début:"))
        self.dteStart.setDisplayFormat(_translate("SpecifyRange", "yyyy/MM/dd HH:mm:ss"))
        self.lblDuration.setText(_translate("SpecifyRange", "Durée:"))
        self.sbDayDuration.setSuffix(_translate("SpecifyRange", "j"))
        self.timeDuration.setDisplayFormat(_translate("SpecifyRange", "HH:mm:ss"))
        self.lblEndText.setText(_translate("SpecifyRange", "TextLabel"))
        self.lblComment.setText(_translate("SpecifyRange", "Commentaire:"))
        self.lblName.setText(_translate("SpecifyRange", "Nom:"))

from . import resources_rc
