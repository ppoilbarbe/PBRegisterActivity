from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QFont,
    QPixmap,
)
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)

from .resources import DIR as RESOURCES_DIR


class Ui_About:
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName("About")
        About.resize(278, 236)
        self.layoutAbout = QVBoxLayout(About)
        self.layoutAbout.setObjectName("layoutAbout")
        self.layoutContent = QHBoxLayout()
        self.layoutContent.setObjectName("layoutContent")
        self.layoutIcon = QVBoxLayout()
        self.layoutIcon.setObjectName("layoutIcon")
        self.lblProgramIcon = QLabel(About)
        self.lblProgramIcon.setObjectName("lblProgramIcon")
        self.lblProgramIcon.setMaximumSize(QSize(64, 64))
        self.lblProgramIcon.setPixmap(
            QPixmap(str(RESOURCES_DIR / "pbregisteractivity.png"))
        )
        self.lblProgramIcon.setScaledContents(True)
        self.lblProgramIcon.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.layoutIcon.addWidget(self.lblProgramIcon)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.layoutIcon.addItem(self.verticalSpacer_3)

        self.layoutContent.addLayout(self.layoutIcon)

        self.frmText = QFrame(About)
        self.frmText.setObjectName("frmText")
        self.frmText.setFrameShape(QFrame.Panel)
        self.frmText.setFrameShadow(QFrame.Raised)
        self.frmText.setLineWidth(3)
        self.layoutText = QVBoxLayout(self.frmText)
        self.layoutText.setObjectName("layoutText")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.layoutText.addItem(self.verticalSpacer)

        self.lblVersion = QLabel(self.frmText)
        self.lblVersion.setObjectName("lblVersion")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVersion.sizePolicy().hasHeightForWidth())
        self.lblVersion.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(Qt.AlignCenter)

        self.layoutText.addWidget(self.lblVersion)

        self.lblAuthor = QLabel(self.frmText)
        self.lblAuthor.setObjectName("lblAuthor")
        sizePolicy.setHeightForWidth(self.lblAuthor.sizePolicy().hasHeightForWidth())
        self.lblAuthor.setSizePolicy(sizePolicy)

        self.layoutText.addWidget(self.lblAuthor)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.lblPythonVersionLbl = QLabel(self.frmText)
        self.lblPythonVersionLbl.setObjectName("lblPythonVersionLbl")

        self.formLayout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.lblPythonVersionLbl
        )

        self.lblPythonVersion = QLabel(self.frmText)
        self.lblPythonVersion.setObjectName("lblPythonVersion")

        self.formLayout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.lblPythonVersion
        )

        self.lblQtVersionLbl = QLabel(self.frmText)
        self.lblQtVersionLbl.setObjectName("lblQtVersionLbl")

        self.formLayout.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.lblQtVersionLbl
        )

        self.lblQtVersion = QLabel(self.frmText)
        self.lblQtVersion.setObjectName("lblQtVersion")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lblQtVersion)

        self.lblPySide6VersionLbl = QLabel(self.frmText)
        self.lblPySide6VersionLbl.setObjectName("lblPySide6VersionLbl")

        self.formLayout.setWidget(
            3, QFormLayout.ItemRole.LabelRole, self.lblPySide6VersionLbl
        )

        self.lblPySide6Version = QLabel(self.frmText)
        self.lblPySide6Version.setObjectName("lblPySide6Version")

        self.formLayout.setWidget(
            3, QFormLayout.ItemRole.FieldRole, self.lblPySide6Version
        )

        self.layoutText.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.layoutText.addItem(self.verticalSpacer_2)

        self.layoutContent.addWidget(self.frmText)

        self.layoutAbout.addLayout(self.layoutContent)

        self.buttonBox = QDialogButtonBox(About)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.layoutAbout.addWidget(self.buttonBox)

        self.retranslateUi(About)
        self.buttonBox.accepted.connect(About.accept)
        self.buttonBox.rejected.connect(About.reject)

        QMetaObject.connectSlotsByName(About)

    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(
            QCoreApplication.translate("About", "\u00c0 propos.", None)
        )
        self.lblVersion.setText(QCoreApplication.translate("About", "Version", None))
        self.lblAuthor.setText(
            QCoreApplication.translate(
                "About",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600;">Ph. Poilbarbe</span><br/>\u00a9 2017-2026</p></body></html>',
                None,
            )
        )
        self.lblPythonVersionLbl.setText(
            QCoreApplication.translate(
                "About",
                '<html><head/><body><p><span style=" font-style:italic;">Version python:</span></p></body></html>',
                None,
            )
        )
        self.lblPythonVersion.setText(
            QCoreApplication.translate("About", "TextLabel", None)
        )
        self.lblQtVersionLbl.setText(
            QCoreApplication.translate(
                "About",
                '<html><head/><body><p><span style=" font-style:italic;">Version Qt:</span></p></body></html>',
                None,
            )
        )
        self.lblQtVersion.setText(
            QCoreApplication.translate("About", "TextLabel", None)
        )
        self.lblPySide6VersionLbl.setText(
            QCoreApplication.translate(
                "About",
                '<html><head/><body><p><span style=" font-style:italic;">Version PySide6:</span></p></body></html>',
                None,
            )
        )
        self.lblPySide6Version.setText(
            QCoreApplication.translate("About", "TextLabel", None)
        )

    # retranslateUi
