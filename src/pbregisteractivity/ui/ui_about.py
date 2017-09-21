# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(222, 162)
        self.layoutAbout = QtWidgets.QVBoxLayout(About)
        self.layoutAbout.setObjectName("layoutAbout")
        self.layoutContent = QtWidgets.QHBoxLayout()
        self.layoutContent.setObjectName("layoutContent")
        self.layoutIcon = QtWidgets.QVBoxLayout()
        self.layoutIcon.setObjectName("layoutIcon")
        self.lblProgramIcon = QtWidgets.QLabel(About)
        self.lblProgramIcon.setMaximumSize(QtCore.QSize(64, 64))
        self.lblProgramIcon.setPixmap(QtGui.QPixmap(":/images/icons/128x128/obj_hal9000.png"))
        self.lblProgramIcon.setScaledContents(True)
        self.lblProgramIcon.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblProgramIcon.setObjectName("lblProgramIcon")
        self.layoutIcon.addWidget(self.lblProgramIcon)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutIcon.addItem(spacerItem)
        self.layoutContent.addLayout(self.layoutIcon)
        self.frmText = QtWidgets.QFrame(About)
        self.frmText.setFrameShape(QtWidgets.QFrame.Panel)
        self.frmText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmText.setLineWidth(3)
        self.frmText.setObjectName("frmText")
        self.layoutText = QtWidgets.QVBoxLayout(self.frmText)
        self.layoutText.setObjectName("layoutText")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutText.addItem(spacerItem1)
        self.lblVersion = QtWidgets.QLabel(self.frmText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVersion.sizePolicy().hasHeightForWidth())
        self.lblVersion.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName("lblVersion")
        self.layoutText.addWidget(self.lblVersion)
        self.lblAuthor = QtWidgets.QLabel(self.frmText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAuthor.sizePolicy().hasHeightForWidth())
        self.lblAuthor.setSizePolicy(sizePolicy)
        self.lblAuthor.setObjectName("lblAuthor")
        self.layoutText.addWidget(self.lblAuthor)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layoutText.addItem(spacerItem2)
        self.layoutContent.addWidget(self.frmText)
        self.layoutAbout.addLayout(self.layoutContent)
        self.buttonBox = QtWidgets.QDialogButtonBox(About)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutAbout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        self.buttonBox.accepted.connect(About.accept)
        self.buttonBox.rejected.connect(About.reject)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "À propos."))
        self.lblVersion.setText(_translate("About", "Version"))
        self.lblAuthor.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Ph. Poilbarbe</span><br/>© 2017</p></body></html>"))

from . import resources_rc
