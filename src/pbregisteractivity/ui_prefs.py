from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QIcon,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QVBoxLayout,
)

from .resources import DIR as RESOURCES_DIR


class Ui_Prefs:
    def setupUi(self, Prefs):
        if not Prefs.objectName():
            Prefs.setObjectName("Prefs")
        Prefs.resize(388, 187)
        icon = QIcon()
        icon.addFile(
            str(RESOURCES_DIR / "action_preferences.png"),
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        Prefs.setWindowIcon(icon)
        self.layoutPrefs = QVBoxLayout(Prefs)
        self.layoutPrefs.setObjectName("layoutPrefs")
        self.layoutData = QFormLayout()
        self.layoutData.setObjectName("layoutData")
        self.lblDayDuration = QLabel(Prefs)
        self.lblDayDuration.setObjectName("lblDayDuration")

        self.layoutData.setWidget(
            0, QFormLayout.ItemRole.LabelRole, self.lblDayDuration
        )

        self.layoutDayDuration = QHBoxLayout()
        self.layoutDayDuration.setObjectName("layoutDayDuration")
        self.spinDayDuration = QDoubleSpinBox(Prefs)
        self.spinDayDuration.setObjectName("spinDayDuration")
        self.spinDayDuration.setMaximum(24.000000000000000)
        self.spinDayDuration.setSingleStep(0.250000000000000)
        self.spinDayDuration.setValue(0.000000000000000)

        self.layoutDayDuration.addWidget(self.spinDayDuration)

        self.hsDayDuration = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutDayDuration.addItem(self.hsDayDuration)

        self.layoutData.setLayout(
            0, QFormLayout.ItemRole.FieldRole, self.layoutDayDuration
        )

        self.lblMisc = QLabel(Prefs)
        self.lblMisc.setObjectName("lblMisc")

        self.layoutData.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblMisc)

        self.layoutMisc = QHBoxLayout()
        self.layoutMisc.setObjectName("layoutMisc")
        self.spinMisc = QSpinBox(Prefs)
        self.spinMisc.setObjectName("spinMisc")
        self.spinMisc.setMaximum(1440)
        self.spinMisc.setSingleStep(15)

        self.layoutMisc.addWidget(self.spinMisc)

        self.hsMisc = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutMisc.addItem(self.hsMisc)

        self.layoutData.setLayout(1, QFormLayout.ItemRole.FieldRole, self.layoutMisc)

        self.lblMinimizeTo = QLabel(Prefs)
        self.lblMinimizeTo.setObjectName("lblMinimizeTo")

        self.layoutData.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblMinimizeTo)

        self.layoutMinimizeTo = QHBoxLayout()
        self.layoutMinimizeTo.setSpacing(3)
        self.layoutMinimizeTo.setObjectName("layoutMinimizeTo")
        self.cbToTray = QCheckBox(Prefs)
        self.cbToTray.setObjectName("cbToTray")

        self.layoutMinimizeTo.addWidget(self.cbToTray)

        self.lblReload1 = QLabel(Prefs)
        self.lblReload1.setObjectName("lblReload1")

        self.layoutMinimizeTo.addWidget(self.lblReload1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutMinimizeTo.addItem(self.horizontalSpacer)

        self.layoutData.setLayout(
            2, QFormLayout.ItemRole.FieldRole, self.layoutMinimizeTo
        )

        self.lblAutoSave = QLabel(Prefs)
        self.lblAutoSave.setObjectName("lblAutoSave")

        self.layoutData.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblAutoSave)

        self.layoutAutoSave = QHBoxLayout()
        self.layoutAutoSave.setObjectName("layoutAutoSave")
        self.cbAutoSave = QCheckBox(Prefs)
        self.cbAutoSave.setObjectName("cbAutoSave")

        self.layoutAutoSave.addWidget(self.cbAutoSave)

        self.layoutData.setLayout(
            3, QFormLayout.ItemRole.FieldRole, self.layoutAutoSave
        )

        self.layoutPrefs.addLayout(self.layoutData)

        self.lblReload = QLabel(Prefs)
        self.lblReload.setObjectName("lblReload")

        self.layoutPrefs.addWidget(self.lblReload)

        self.buttonBox = QDialogButtonBox(Prefs)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.layoutPrefs.addWidget(self.buttonBox)

        self.retranslateUi(Prefs)
        self.buttonBox.accepted.connect(Prefs.accept)
        self.buttonBox.rejected.connect(Prefs.reject)

        QMetaObject.connectSlotsByName(Prefs)

    # setupUi

    def retranslateUi(self, Prefs):
        Prefs.setWindowTitle(
            QCoreApplication.translate("Prefs", "Pr\u00e9f\u00e9rences", None)
        )
        self.lblDayDuration.setText(
            QCoreApplication.translate("Prefs", "Dur\u00e9e du jour:", None)
        )
        # if QT_CONFIG(tooltip)
        self.spinDayDuration.setToolTip(
            QCoreApplication.translate(
                "Prefs", "Dur\u00e9e du jour de travail en heures", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.spinDayDuration.setSuffix(QCoreApplication.translate("Prefs", "h", None))
        self.lblMisc.setText(
            QCoreApplication.translate("Prefs", "Divers si dur\u00e9e:", None)
        )
        # if QT_CONFIG(tooltip)
        self.spinMisc.setToolTip(
            QCoreApplication.translate(
                "Prefs",
                "Dur\u00e9e en dessous de laquelle une activit\u00e9\n"
                'est regroup\u00e9e en tant que "Divers".\n'
                "Si 0, il n'y a pas de regroupement.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.spinMisc.setSuffix(QCoreApplication.translate("Prefs", "min", None))
        self.spinMisc.setPrefix(QCoreApplication.translate("Prefs", "< ", None))
        self.lblMinimizeTo.setText(
            QCoreApplication.translate("Prefs", "Minimiser en:", None)
        )
        # if QT_CONFIG(tooltip)
        self.cbToTray.setToolTip(
            QCoreApplication.translate(
                "Prefs",
                "<html><head/><body><p>Minimisation de l'application en zone de notification plut\u00f4t que dans la barre des t\u00e2ches</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.cbToTray.setText(
            QCoreApplication.translate(
                "Prefs", "Zone de notification (Qt5.6 et plus)", None
            )
        )
        self.lblReload1.setText(
            QCoreApplication.translate(
                "Prefs",
                '<html><head/><body><p><span style=" font-weight:600; color:#ff1414; vertical-align:super;">*</span></p></body></html>',
                None,
            )
        )
        self.lblAutoSave.setText(
            QCoreApplication.translate("Prefs", "Sauvegarde auto:", None)
        )
        # if QT_CONFIG(tooltip)
        self.cbAutoSave.setToolTip(
            QCoreApplication.translate(
                "Prefs",
                "<html><head/><body><p>Lorsque le programme se termine, sauvegarde automatiquement la p\u00e9riode de temps en cours de comptage. Si aucun nom n'a \u00e9t\u00e9 donn\u00e9, cr\u00e9e un nom par d\u00e9faut.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.cbAutoSave.setText(
            QCoreApplication.translate("Prefs", "Si plus de 10 min", None)
        )
        self.lblReload.setText(
            QCoreApplication.translate(
                "Prefs",
                '<html><head/><body><p><span style=" font-weight:600; color:#ff1414;">* N\u00e9cessite un red\u00e9marrage</span></p></body></html>',
                None,
            )
        )

    # retranslateUi
