# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 456)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/128x128/obj_hal9000.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblRegistered = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblRegistered.setFont(font)
        self.lblRegistered.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRegistered.setObjectName("lblRegistered")
        self.verticalLayout.addWidget(self.lblRegistered)
        self.listHistory = QtWidgets.QListWidget(self.layoutWidget)
        self.listHistory.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listHistory.setObjectName("listHistory")
        self.verticalLayout.addWidget(self.listHistory)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutInfo = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.layoutInfo.setContentsMargins(-1, -1, -1, 2)
        self.layoutInfo.setSpacing(0)
        self.layoutInfo.setObjectName("layoutInfo")
        self.lblCurrent = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrent.setFont(font)
        self.lblCurrent.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrent.setObjectName("lblCurrent")
        self.layoutInfo.addWidget(self.lblCurrent)
        self.layoutCurrent = QtWidgets.QFormLayout()
        self.layoutCurrent.setVerticalSpacing(2)
        self.layoutCurrent.setObjectName("layoutCurrent")
        self.lblCurrentAction = QtWidgets.QLabel(self.layoutWidget1)
        self.lblCurrentAction.setObjectName("lblCurrentAction")
        self.layoutCurrent.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblCurrentAction)
        self.lblStart = QtWidgets.QLabel(self.layoutWidget1)
        self.lblStart.setObjectName("lblStart")
        self.layoutCurrent.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblStart)
        self.dteStart = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dteStart.sizePolicy().hasHeightForWidth())
        self.dteStart.setSizePolicy(sizePolicy)
        self.dteStart.setCalendarPopup(True)
        self.dteStart.setObjectName("dteStart")
        self.layoutCurrent.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dteStart)
        self.lblDuration = QtWidgets.QLabel(self.layoutWidget1)
        self.lblDuration.setObjectName("lblDuration")
        self.layoutCurrent.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblDuration)
        self.layoutDuration = QtWidgets.QHBoxLayout()
        self.layoutDuration.setObjectName("layoutDuration")
        self.lcdDuration = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.lcdDuration.setSmallDecimalPoint(False)
        self.lcdDuration.setDigitCount(8)
        self.lcdDuration.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdDuration.setObjectName("lcdDuration")
        self.layoutDuration.addWidget(self.lcdDuration)
        self.lblEndText = QtWidgets.QLabel(self.layoutWidget1)
        self.lblEndText.setObjectName("lblEndText")
        self.layoutDuration.addWidget(self.lblEndText)
        self.tbForceAdd = QtWidgets.QToolButton(self.layoutWidget1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbForceAdd.setIcon(icon1)
        self.tbForceAdd.setObjectName("tbForceAdd")
        self.layoutDuration.addWidget(self.tbForceAdd)
        self.layoutDuration.setStretch(1, 1)
        self.layoutCurrent.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.layoutDuration)
        self.lblComment = QtWidgets.QLabel(self.layoutWidget1)
        self.lblComment.setObjectName("lblComment")
        self.layoutCurrent.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.cbbActivities = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbbActivities.sizePolicy().hasHeightForWidth())
        self.cbbActivities.setSizePolicy(sizePolicy)
        self.cbbActivities.setEditable(True)
        self.cbbActivities.setObjectName("cbbActivities")
        self.layoutCurrent.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cbbActivities)
        self.edtComment = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtComment.sizePolicy().hasHeightForWidth())
        self.edtComment.setSizePolicy(sizePolicy)
        self.edtComment.setMaximumSize(QtCore.QSize(16777215, 120))
        self.edtComment.setObjectName("edtComment")
        self.layoutCurrent.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edtComment)
        self.layoutInfo.addLayout(self.layoutCurrent)
        self.frmSelected = QtWidgets.QFrame(self.layoutWidget1)
        self.frmSelected.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmSelected.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmSelected.setLineWidth(3)
        self.frmSelected.setMidLineWidth(1)
        self.frmSelected.setObjectName("frmSelected")
        self.layoutSelected = QtWidgets.QVBoxLayout(self.frmSelected)
        self.layoutSelected.setObjectName("layoutSelected")
        self.lblSelected = QtWidgets.QLabel(self.frmSelected)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSelected.setFont(font)
        self.lblSelected.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSelected.setObjectName("lblSelected")
        self.layoutSelected.addWidget(self.lblSelected)
        self.txtSelected = QtWidgets.QTextBrowser(self.frmSelected)
        self.txtSelected.setObjectName("txtSelected")
        self.layoutSelected.addWidget(self.txtSelected)
        self.layoutInfo.addWidget(self.frmSelected)
        self.layoutInfo.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menu_Liste = QtWidgets.QMenu(self.menubar)
        self.menu_Liste.setObjectName("menu_Liste")
        self.menu_Aide = QtWidgets.QMenu(self.menubar)
        self.menu_Aide.setObjectName("menu_Aide")
        MainWindow.setMenuBar(self.menubar)
        self.tbMain = QtWidgets.QToolBar(MainWindow)
        self.tbMain.setObjectName("tbMain")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tbMain)
        self.tbList = QtWidgets.QToolBar(MainWindow)
        self.tbList.setObjectName("tbList")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tbList)
        self.tbCurrent = QtWidgets.QToolBar(MainWindow)
        self.tbCurrent.setObjectName("tbCurrent")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tbCurrent)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRegister = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegister.setIcon(icon3)
        self.actionRegister.setObjectName("actionRegister")
        self.actionCancel = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCancel.setIcon(icon4)
        self.actionCancel.setObjectName("actionCancel")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon5)
        self.actionRemove.setObjectName("actionRemove")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon6)
        self.actionSave.setObjectName("actionSave")
        self.actionSwapActivity = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSwapActivity.setIcon(icon7)
        self.actionSwapActivity.setObjectName("actionSwapActivity")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon8)
        self.actionEdit.setObjectName("actionEdit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExtract = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/icons/32x32/action_cal_timespent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExtract.setIcon(icon9)
        self.actionExtract.setObjectName("actionExtract")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuAction.addAction(self.actionRegister)
        self.menuAction.addAction(self.actionCancel)
        self.menuAction.addAction(self.actionSwapActivity)
        self.menu_Liste.addAction(self.actionRemove)
        self.menu_Liste.addAction(self.actionEdit)
        self.menu_Liste.addAction(self.actionSwapActivity)
        self.menu_Liste.addSeparator()
        self.menu_Liste.addAction(self.actionExtract)
        self.menu_Aide.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Liste.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menu_Aide.menuAction())
        self.tbMain.addAction(self.actionQuit)
        self.tbMain.addAction(self.actionSave)
        self.tbList.addAction(self.actionRemove)
        self.tbList.addAction(self.actionEdit)
        self.tbList.addAction(self.actionSwapActivity)
        self.tbList.addAction(self.actionExtract)
        self.tbCurrent.addAction(self.actionRegister)
        self.tbCurrent.addAction(self.actionCancel)
        self.tbCurrent.addAction(self.actionSwapActivity)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cbbActivities, self.dteStart)
        MainWindow.setTabOrder(self.dteStart, self.tbForceAdd)
        MainWindow.setTabOrder(self.tbForceAdd, self.edtComment)
        MainWindow.setTabOrder(self.edtComment, self.txtSelected)
        MainWindow.setTabOrder(self.txtSelected, self.listHistory)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PBResgisterActivity"))
        self.lblRegistered.setText(_translate("MainWindow", "Plages enregistrées"))
        self.lblCurrent.setText(_translate("MainWindow", "Activité en cours"))
        self.lblCurrentAction.setText(_translate("MainWindow", "Action en cours:"))
        self.lblStart.setText(_translate("MainWindow", "Heure début:"))
        self.dteStart.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd HH:mm:ss"))
        self.lblDuration.setText(_translate("MainWindow", "Durée:"))
        self.lblEndText.setText(_translate("MainWindow", "TextLabel"))
        self.tbForceAdd.setToolTip(_translate("MainWindow", "Ajout d\'une période en forçant la durée (sera saisie)"))
        self.lblComment.setText(_translate("MainWindow", "Commentaire:"))
        self.lblSelected.setText(_translate("MainWindow", "Pas de sélection"))
        self.txtSelected.setToolTip(_translate("MainWindow", "Affiche des informations sur les plages enregistrées sélectionnées"))
        self.menuFile.setTitle(_translate("MainWindow", "&Fichier"))
        self.menuAction.setTitle(_translate("MainWindow", "&Plage"))
        self.menu_Liste.setTitle(_translate("MainWindow", "&Liste"))
        self.menu_Aide.setTitle(_translate("MainWindow", "&Aide"))
        self.tbMain.setWindowTitle(_translate("MainWindow", "Général"))
        self.tbList.setWindowTitle(_translate("MainWindow", "Liste"))
        self.tbCurrent.setWindowTitle(_translate("MainWindow", "En cours"))
        self.actionQuit.setText(_translate("MainWindow", "&Quitter"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Termine le programme"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Termine le programme et enregistre la liste"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionRegister.setText(_translate("MainWindow", "&Enregistrer plage"))
        self.actionRegister.setToolTip(_translate("MainWindow", "Enregistre la plage de temps"))
        self.actionRegister.setStatusTip(_translate("MainWindow", "Enregistre l\'action en cours dans la liste"))
        self.actionRegister.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionCancel.setText(_translate("MainWindow", "&Annuler plage"))
        self.actionCancel.setIconText(_translate("MainWindow", "Annuler"))
        self.actionCancel.setToolTip(_translate("MainWindow", "Annule la  plage de temps"))
        self.actionCancel.setStatusTip(_translate("MainWindow", "Annule l\'action en cours et repart à zéro."))
        self.actionRemove.setText(_translate("MainWindow", "&Retirer plage"))
        self.actionRemove.setToolTip(_translate("MainWindow", "Retire les plages sélectionnées"))
        self.actionRemove.setStatusTip(_translate("MainWindow", "Supprime les lignes sélectionnées de la liste"))
        self.actionSave.setText(_translate("MainWindow", "&Enregistrer"))
        self.actionSave.setToolTip(_translate("MainWindow", "Enregistre la liste des plages d\'activité maintenant.\n"
"Sinon, elle est enregistrée lors de la sortie du programme."))
        self.actionSave.setStatusTip(_translate("MainWindow", "Enregistre la liste des plages d\'activité maintenant. Sinon, elle est enregistrée lors de la sortie du programme."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSwapActivity.setText(_translate("MainWindow", "&Basculer tâche"))
        self.actionSwapActivity.setToolTip(_translate("MainWindow", "Termine l\'activité en cours (la sauvegarde) et passe à l\'activité sélectionnée"))
        self.actionSwapActivity.setStatusTip(_translate("MainWindow", "Sauvegarde dans la liste l\'activité en cours et démarre une nouvelle"))
        self.actionSwapActivity.setShortcut(_translate("MainWindow", "F8"))
        self.actionEdit.setText(_translate("MainWindow", "&Modifier plage"))
        self.actionEdit.setToolTip(_translate("MainWindow", "Modifie la plage sélectionnée (commentaire uniquement)"))
        self.actionEdit.setStatusTip(_translate("MainWindow", "Modifie la plage sélectionnée dans la liste"))
        self.actionAbout.setText(_translate("MainWindow", "&À propos..."))
        self.actionAbout.setShortcut(_translate("MainWindow", "F1"))
        self.actionExtract.setText(_translate("MainWindow", "&Extractions"))
        self.actionExtract.setToolTip(_translate("MainWindow", "Extractions du temps passé sur les activités"))
        self.actionExtract.setShortcut(_translate("MainWindow", "F12"))

from . import resources_rc
