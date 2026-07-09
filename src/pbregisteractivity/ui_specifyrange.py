from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtWidgets import (
    QComboBox,
    QDateTimeEdit,
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

from .resources import pixmap


class Ui_SpecifyRange:
    def setupUi(self, SpecifyRange):
        if not SpecifyRange.objectName():
            SpecifyRange.setObjectName("SpecifyRange")
        SpecifyRange.resize(500, 300)
        SpecifyRange.setMinimumSize(QSize(500, 300))
        self.layoutDialog = QVBoxLayout(SpecifyRange)
        self.layoutDialog.setObjectName("layoutDialog")
        self.lblTitle = QLabel(SpecifyRange)
        self.lblTitle.setObjectName("lblTitle")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setFrameShape(QFrame.Panel)
        self.lblTitle.setFrameShadow(QFrame.Raised)
        self.lblTitle.setTextFormat(Qt.PlainText)
        self.lblTitle.setAlignment(Qt.AlignCenter)

        self.layoutDialog.addWidget(self.lblTitle)

        self.layoutInput = QFormLayout()
        self.layoutInput.setObjectName("layoutInput")
        self.lblName = QLabel(SpecifyRange)
        self.lblName.setObjectName("lblName")

        self.layoutInput.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblName)

        self.lblStart = QLabel(SpecifyRange)
        self.lblStart.setObjectName("lblStart")

        self.layoutInput.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblStart)

        self.layoutStart = QHBoxLayout()
        self.layoutStart.setObjectName("layoutStart")
        self.layoutStart.setContentsMargins(-1, 0, -1, -1)
        self.dteStart = QDateTimeEdit(SpecifyRange)
        self.dteStart.setObjectName("dteStart")
        self.dteStart.setCurrentSection(QDateTimeEdit.YearSection)
        self.dteStart.setCalendarPopup(True)

        self.layoutStart.addWidget(self.dteStart)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutStart.addItem(self.horizontalSpacer_2)

        self.layoutInput.setLayout(1, QFormLayout.ItemRole.FieldRole, self.layoutStart)

        self.lblEnd = QLabel(SpecifyRange)
        self.lblEnd.setObjectName("lblEnd")

        self.layoutInput.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblEnd)

        self.layoutEnd = QHBoxLayout()
        self.layoutEnd.setObjectName("layoutEnd")
        self.dteEnd = QDateTimeEdit(SpecifyRange)
        self.dteEnd.setObjectName("dteEnd")
        self.dteEnd.setCurrentSection(QDateTimeEdit.YearSection)
        self.dteEnd.setCalendarPopup(True)

        self.layoutEnd.addWidget(self.dteEnd)

        self.lblEndWarning = QLabel(SpecifyRange)
        self.lblEndWarning.setObjectName("lblEndWarning")
        self.lblEndWarning.setMaximumSize(QSize(24, 24))
        self.lblEndWarning.setPixmap(pixmap("warning.svg"))
        self.lblEndWarning.setScaledContents(True)

        self.layoutEnd.addWidget(self.lblEndWarning)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutEnd.addItem(self.horizontalSpacer_3)

        self.layoutInput.setLayout(2, QFormLayout.ItemRole.FieldRole, self.layoutEnd)

        self.lblDuration = QLabel(SpecifyRange)
        self.lblDuration.setObjectName("lblDuration")

        self.layoutInput.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblDuration)

        self.layoutDuration = QHBoxLayout()
        self.layoutDuration.setObjectName("layoutDuration")
        self.sbDayDuration = QSpinBox(SpecifyRange)
        self.sbDayDuration.setObjectName("sbDayDuration")
        self.sbDayDuration.setMaximum(10)

        self.layoutDuration.addWidget(self.sbDayDuration)

        self.timeDuration = QTimeEdit(SpecifyRange)
        self.timeDuration.setObjectName("timeDuration")

        self.layoutDuration.addWidget(self.timeDuration)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutDuration.addItem(self.horizontalSpacer)

        self.layoutDuration.setStretch(0, 1)
        self.layoutDuration.setStretch(1, 1)
        self.layoutDuration.setStretch(2, 2)

        self.layoutInput.setLayout(
            3, QFormLayout.ItemRole.FieldRole, self.layoutDuration
        )

        self.lblComment = QLabel(SpecifyRange)
        self.lblComment.setObjectName("lblComment")

        self.layoutInput.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblComment)

        self.edtComment = QPlainTextEdit(SpecifyRange)
        self.edtComment.setObjectName("edtComment")

        self.layoutInput.setWidget(4, QFormLayout.ItemRole.FieldRole, self.edtComment)

        self.cbbName = QComboBox(SpecifyRange)
        self.cbbName.setObjectName("cbbName")
        self.cbbName.setEditable(True)

        self.layoutInput.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cbbName)

        self.layoutDialog.addLayout(self.layoutInput)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.layoutDialog.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(SpecifyRange)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.layoutDialog.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.sbDayDuration, self.timeDuration)
        QWidget.setTabOrder(self.timeDuration, self.edtComment)

        self.retranslateUi(SpecifyRange)
        self.buttonBox.accepted.connect(SpecifyRange.accept)
        self.buttonBox.rejected.connect(SpecifyRange.reject)

        QMetaObject.connectSlotsByName(SpecifyRange)

    # setupUi

    def retranslateUi(self, SpecifyRange):
        SpecifyRange.setWindowTitle(
            QCoreApplication.translate("SpecifyRange", "Dialog", None)
        )
        self.lblTitle.setText(
            QCoreApplication.translate("SpecifyRange", "TextLabel", None)
        )
        self.lblName.setText(QCoreApplication.translate("SpecifyRange", "Nom:", None))
        self.lblStart.setText(
            QCoreApplication.translate("SpecifyRange", "Heure d\u00e9but:", None)
        )
        self.dteStart.setDisplayFormat(
            QCoreApplication.translate("SpecifyRange", "yyyy-MM-dd HH:mm:ss", None)
        )
        self.lblEnd.setText(
            QCoreApplication.translate("SpecifyRange", "Heure fin:", None)
        )
        self.dteEnd.setDisplayFormat(
            QCoreApplication.translate("SpecifyRange", "yyyy-MM-dd HH:mm:ss", None)
        )
        # if QT_CONFIG(tooltip)
        self.lblEndWarning.setToolTip(
            QCoreApplication.translate(
                "SpecifyRange", "Date/heure de fin incorrecte", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lblDuration.setText(
            QCoreApplication.translate("SpecifyRange", "Dur\u00e9e:", None)
        )
        # if QT_CONFIG(tooltip)
        self.sbDayDuration.setToolTip(
            QCoreApplication.translate(
                "SpecifyRange", "Nombre de jours de 24h (max=10)", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.sbDayDuration.setSuffix(
            QCoreApplication.translate("SpecifyRange", "j", None)
        )
        self.timeDuration.setDisplayFormat(
            QCoreApplication.translate("SpecifyRange", "HH:mm:ss", None)
        )
        self.lblComment.setText(
            QCoreApplication.translate("SpecifyRange", "Commentaire:", None)
        )
        # if QT_CONFIG(tooltip)
        self.cbbName.setToolTip(
            QCoreApplication.translate(
                "SpecifyRange",
                "Nom de l'activit\u00e9 \u00e0 cr\u00e9er/mettre \u00e0 jour",
                None,
            )
        )


# endif // QT_CONFIG(tooltip)
# retranslateUi
