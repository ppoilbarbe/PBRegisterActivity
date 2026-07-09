from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QFont,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QListWidget,
    QMenu,
    QMenuBar,
    QPlainTextEdit,
    QSizePolicy,
    QSplitter,
    QStatusBar,
    QTextBrowser,
    QToolBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from .resources import icon


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 456)
        MainWindow.setWindowIcon(icon("pbregisteractivity.png"))
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.setIcon(icon("quit.svg"))
        self.actionRegister = QAction(MainWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.actionRegister.setIcon(icon("ok.svg"))
        self.actionCancel = QAction(MainWindow)
        self.actionCancel.setObjectName("actionCancel")
        self.actionCancel.setIcon(icon("cancel.svg"))
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionRemove.setIcon(icon("remove.svg"))
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setIcon(icon("save.svg"))
        self.actionSwapActivity = QAction(MainWindow)
        self.actionSwapActivity.setObjectName("actionSwapActivity")
        self.actionSwapActivity.setIcon(icon("refresh.svg"))
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionEdit.setIcon(icon("edit.svg"))
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setIcon(icon("help-about.svg"))
        self.actionExtract = QAction(MainWindow)
        self.actionExtract.setObjectName("actionExtract")
        self.actionExtract.setIcon(icon("calendar-time-spent.svg"))
        self.actionPrefs = QAction(MainWindow)
        self.actionPrefs.setObjectName("actionPrefs")
        self.actionPrefs.setIcon(icon("preferences-system.svg"))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutSelection = QVBoxLayout(self.layoutWidget)
        self.layoutSelection.setObjectName("layoutSelection")
        self.layoutSelection.setContentsMargins(0, 0, 0, 0)
        self.lblRegistered = QLabel(self.layoutWidget)
        self.lblRegistered.setObjectName("lblRegistered")
        font = QFont()
        font.setBold(True)
        self.lblRegistered.setFont(font)
        self.lblRegistered.setAlignment(Qt.AlignCenter)

        self.layoutSelection.addWidget(self.lblRegistered)

        self.listHistory = QListWidget(self.layoutWidget)
        self.listHistory.setObjectName("listHistory")
        self.listHistory.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.layoutSelection.addWidget(self.listHistory)

        self.layoutFilter = QHBoxLayout()
        self.layoutFilter.setObjectName("layoutFilter")
        self.lblFilter = QLabel(self.layoutWidget)
        self.lblFilter.setObjectName("lblFilter")

        self.layoutFilter.addWidget(self.lblFilter)

        self.edtFilter = QLineEdit(self.layoutWidget)
        self.edtFilter.setObjectName("edtFilter")

        self.layoutFilter.addWidget(self.edtFilter)

        self.cbFilterType = QCheckBox(self.layoutWidget)
        self.cbFilterType.setObjectName("cbFilterType")
        self.cbFilterType.setTristate(True)

        self.layoutFilter.addWidget(self.cbFilterType)

        self.layoutSelection.addLayout(self.layoutFilter)

        self.layoutSelection.setStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutInfo = QVBoxLayout(self.layoutWidget1)
        self.layoutInfo.setSpacing(0)
        self.layoutInfo.setObjectName("layoutInfo")
        self.layoutInfo.setContentsMargins(0, 0, 0, 2)
        self.lblCurrent = QLabel(self.layoutWidget1)
        self.lblCurrent.setObjectName("lblCurrent")
        self.lblCurrent.setFont(font)
        self.lblCurrent.setAlignment(Qt.AlignCenter)

        self.layoutInfo.addWidget(self.lblCurrent)

        self.layoutCurrent = QFormLayout()
        self.layoutCurrent.setObjectName("layoutCurrent")
        self.layoutCurrent.setVerticalSpacing(2)
        self.lblCurrentAction = QLabel(self.layoutWidget1)
        self.lblCurrentAction.setObjectName("lblCurrentAction")

        self.layoutCurrent.setWidget(
            0, QFormLayout.ItemRole.LabelRole, self.lblCurrentAction
        )

        self.lblStart = QLabel(self.layoutWidget1)
        self.lblStart.setObjectName("lblStart")

        self.layoutCurrent.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblStart)

        self.dteStart = QDateTimeEdit(self.layoutWidget1)
        self.dteStart.setObjectName("dteStart")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dteStart.sizePolicy().hasHeightForWidth())
        self.dteStart.setSizePolicy(sizePolicy1)
        self.dteStart.setCalendarPopup(True)

        self.layoutCurrent.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dteStart)

        self.lblDuration = QLabel(self.layoutWidget1)
        self.lblDuration.setObjectName("lblDuration")

        self.layoutCurrent.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.lblDuration
        )

        self.layoutDuration = QHBoxLayout()
        self.layoutDuration.setObjectName("layoutDuration")
        self.lcdDuration = QLCDNumber(self.layoutWidget1)
        self.lcdDuration.setObjectName("lcdDuration")
        self.lcdDuration.setSmallDecimalPoint(False)
        self.lcdDuration.setDigitCount(8)
        self.lcdDuration.setSegmentStyle(QLCDNumber.Flat)

        self.layoutDuration.addWidget(self.lcdDuration)

        self.lblEndText = QLabel(self.layoutWidget1)
        self.lblEndText.setObjectName("lblEndText")

        self.layoutDuration.addWidget(self.lblEndText)

        self.tbForceAdd = QToolButton(self.layoutWidget1)
        self.tbForceAdd.setObjectName("tbForceAdd")
        self.tbForceAdd.setIcon(icon("add.svg"))

        self.layoutDuration.addWidget(self.tbForceAdd)

        self.layoutDuration.setStretch(1, 1)

        self.layoutCurrent.setLayout(
            2, QFormLayout.ItemRole.FieldRole, self.layoutDuration
        )

        self.lblComment = QLabel(self.layoutWidget1)
        self.lblComment.setObjectName("lblComment")

        self.layoutCurrent.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblComment)

        self.cbbActivities = QComboBox(self.layoutWidget1)
        self.cbbActivities.setObjectName("cbbActivities")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.cbbActivities.sizePolicy().hasHeightForWidth()
        )
        self.cbbActivities.setSizePolicy(sizePolicy2)
        self.cbbActivities.setEditable(True)

        self.layoutCurrent.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.cbbActivities
        )

        self.edtComment = QPlainTextEdit(self.layoutWidget1)
        self.edtComment.setObjectName("edtComment")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.edtComment.sizePolicy().hasHeightForWidth())
        self.edtComment.setSizePolicy(sizePolicy3)
        self.edtComment.setMaximumSize(QSize(16777215, 120))

        self.layoutCurrent.setWidget(3, QFormLayout.ItemRole.FieldRole, self.edtComment)

        self.layoutInfo.addLayout(self.layoutCurrent)

        self.frmSelected = QFrame(self.layoutWidget1)
        self.frmSelected.setObjectName("frmSelected")
        self.frmSelected.setFrameShape(QFrame.StyledPanel)
        self.frmSelected.setFrameShadow(QFrame.Raised)
        self.frmSelected.setLineWidth(3)
        self.frmSelected.setMidLineWidth(1)
        self.layoutSelected = QVBoxLayout(self.frmSelected)
        self.layoutSelected.setObjectName("layoutSelected")
        self.lblSelected = QLabel(self.frmSelected)
        self.lblSelected.setObjectName("lblSelected")
        self.lblSelected.setFont(font)
        self.lblSelected.setAlignment(Qt.AlignCenter)

        self.layoutSelected.addWidget(self.lblSelected)

        self.txtSelected = QTextBrowser(self.frmSelected)
        self.txtSelected.setObjectName("txtSelected")

        self.layoutSelected.addWidget(self.txtSelected)

        self.layoutInfo.addWidget(self.frmSelected)

        self.layoutInfo.setStretch(2, 1)
        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menu_Liste = QMenu(self.menubar)
        self.menu_Liste.setObjectName("menu_Liste")
        self.menu_Aide = QMenu(self.menubar)
        self.menu_Aide.setObjectName("menu_Aide")
        MainWindow.setMenuBar(self.menubar)
        self.tbMain = QToolBar(MainWindow)
        self.tbMain.setObjectName("tbMain")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tbMain)
        self.tbList = QToolBar(MainWindow)
        self.tbList.setObjectName("tbList")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tbList)
        self.tbCurrent = QToolBar(MainWindow)
        self.tbCurrent.setObjectName("tbCurrent")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tbCurrent)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.cbbActivities, self.dteStart)
        QWidget.setTabOrder(self.dteStart, self.tbForceAdd)
        QWidget.setTabOrder(self.tbForceAdd, self.edtComment)
        QWidget.setTabOrder(self.edtComment, self.txtSelected)
        QWidget.setTabOrder(self.txtSelected, self.listHistory)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Liste.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menu_Aide.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrefs)
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

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "PBResgisterActivity", None)
        )
        self.actionQuit.setText(
            QCoreApplication.translate("MainWindow", "&Quitter", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(
            QCoreApplication.translate("MainWindow", "Termine le programme", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionQuit.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Termine le programme et enregistre la liste", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+Q", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionRegister.setText(
            QCoreApplication.translate("MainWindow", "&Enregistrer plage", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionRegister.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Enregistre la plage de temps", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionRegister.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Enregistre l'action en cours dans la liste", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionRegister.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionCancel.setText(
            QCoreApplication.translate("MainWindow", "&Annuler plage", None)
        )
        self.actionCancel.setIconText(
            QCoreApplication.translate("MainWindow", "Annuler", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionCancel.setToolTip(
            QCoreApplication.translate("MainWindow", "Annule la  plage de temps", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionCancel.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Annule l'action en cours et repart \u00e0 z\u00e9ro.",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.actionRemove.setText(
            QCoreApplication.translate("MainWindow", "&Retirer plage", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionRemove.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Retire les plages s\u00e9lectionn\u00e9es", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionRemove.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Supprime les lignes s\u00e9lectionn\u00e9es de la liste",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.actionSave.setText(
            QCoreApplication.translate("MainWindow", "&Enregistrer", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Enregistre la liste des plages d'activit\u00e9 maintenant.\n"
                "Sinon, elle est enregistr\u00e9e lors de la sortie du programme.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Enregistre la liste des plages d'activit\u00e9 maintenant. Sinon, elle est enregistr\u00e9e lors de la sortie du programme.",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSwapActivity.setText(
            QCoreApplication.translate("MainWindow", "&Basculer t\u00e2che", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionSwapActivity.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Termine l'activit\u00e9 en cours (la sauvegarde) et passe \u00e0 l'activit\u00e9 s\u00e9lectionn\u00e9e",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionSwapActivity.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Sauvegarde dans la liste l'activit\u00e9 en cours et d\u00e9marre une nouvelle",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSwapActivity.setShortcut(
            QCoreApplication.translate("MainWindow", "F8", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionEdit.setText(
            QCoreApplication.translate("MainWindow", "&Modifier plage", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Modifie la plage s\u00e9lectionn\u00e9e (commentaire uniquement)",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionEdit.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Modifie la plage s\u00e9lectionn\u00e9e dans la liste",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "&\u00c0 propos...", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(
            QCoreApplication.translate("MainWindow", "F1", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionExtract.setText(
            QCoreApplication.translate("MainWindow", "&Extractions", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionExtract.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Extractions du temps pass\u00e9 sur les activit\u00e9s",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionExtract.setShortcut(
            QCoreApplication.translate("MainWindow", "F12", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionPrefs.setText(
            QCoreApplication.translate("MainWindow", "&Pr\u00e9f\u00e9rences", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionPrefs.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Param\u00e8tres g\u00e9n\u00e9raux", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lblRegistered.setText(
            QCoreApplication.translate("MainWindow", "Plages enregistr\u00e9es", None)
        )
        self.lblFilter.setText(
            QCoreApplication.translate("MainWindow", "Filtre:", None)
        )
        # if QT_CONFIG(tooltip)
        self.edtFilter.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "N'affiche que les plages dont\nle nom contient le texte saisi",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.cbFilterType.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Type de filtre:</p><ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;"><li style=" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">N</span>: sur le nom</li><li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">C</span>: sur le commentaire</li><li style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">2</span>: sur les deux</li></ul></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.cbFilterType.setText(QCoreApplication.translate("MainWindow", "?", None))
        self.lblCurrent.setText(
            QCoreApplication.translate("MainWindow", "Activit\u00e9 en cours", None)
        )
        self.lblCurrentAction.setText(
            QCoreApplication.translate("MainWindow", "Action en cours:", None)
        )
        self.lblStart.setText(
            QCoreApplication.translate("MainWindow", "Heure d\u00e9but:", None)
        )
        self.dteStart.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "yyyy-MM-dd HH:mm:ss", None)
        )
        self.lblDuration.setText(
            QCoreApplication.translate("MainWindow", "Dur\u00e9e:", None)
        )
        # if QT_CONFIG(tooltip)
        self.lcdDuration.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Dur\u00e9e calcul\u00e9e entre l'heure de d\u00e9but et l'heure courante.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lblEndText.setText(
            QCoreApplication.translate("MainWindow", "TextLabel", None)
        )
        # if QT_CONFIG(tooltip)
        self.tbForceAdd.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Ajout d'une p\u00e9riode en for\u00e7ant la dur\u00e9e (sera saisie)",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lblComment.setText(
            QCoreApplication.translate("MainWindow", "Commentaire:", None)
        )
        # if QT_CONFIG(tooltip)
        self.cbbActivities.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Nom de l'action en cours d'enregistrement.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.edtComment.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Commentaire \u00e0 associer \u00e0 l'activit\u00e9", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lblSelected.setText(
            QCoreApplication.translate("MainWindow", "Pas de s\u00e9lection", None)
        )
        # if QT_CONFIG(tooltip)
        self.txtSelected.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Affiche des informations sur les plages enregistr\u00e9es s\u00e9lectionn\u00e9es",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", "&Fichier", None)
        )
        self.menuAction.setTitle(
            QCoreApplication.translate("MainWindow", "&Plage", None)
        )
        self.menu_Liste.setTitle(
            QCoreApplication.translate("MainWindow", "&Liste", None)
        )
        self.menu_Aide.setTitle(QCoreApplication.translate("MainWindow", "&Aide", None))
        self.tbMain.setWindowTitle(
            QCoreApplication.translate("MainWindow", "G\u00e9n\u00e9ral", None)
        )
        self.tbList.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Liste", None)
        )
        self.tbCurrent.setWindowTitle(
            QCoreApplication.translate("MainWindow", "En cours", None)
        )

    # retranslateUi
