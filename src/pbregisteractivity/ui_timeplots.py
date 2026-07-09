from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QDateEdit,
    QDialogButtonBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QSizePolicy,
    QSpacerItem,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from .resources import icon

_TOOLBAR_ICON_SIZE = QSize(32, 32)


class Ui_TimePlots:
    def setupUi(self, TimePlots):
        if not TimePlots.objectName():
            TimePlots.setObjectName("TimePlots")
        TimePlots.resize(738, 436)
        TimePlots.setWindowIcon(icon("calendar-time-spent.svg"))
        self.layoutTimePlots = QVBoxLayout(TimePlots)
        self.layoutTimePlots.setObjectName("layoutTimePlots")
        self.layoutActions = QHBoxLayout()
        self.layoutActions.setObjectName("layoutActions")
        self.btnTimeLines = QToolButton(TimePlots)
        self.btnTimeLines.setObjectName("btnTimeLines")
        self.btnTimeLines.setIcon(icon("calendar-timeline.svg"))
        self.btnTimeLines.setIconSize(_TOOLBAR_ICON_SIZE)
        self.btnTimeLines.setCheckable(True)
        self.btnTimeLines.setAutoExclusive(True)

        self.layoutActions.addWidget(self.btnTimeLines)

        self.btnPieChart = QToolButton(TimePlots)
        self.btnPieChart.setObjectName("btnPieChart")
        self.btnPieChart.setIcon(icon("piechart.svg"))
        self.btnPieChart.setIconSize(_TOOLBAR_ICON_SIZE)
        self.btnPieChart.setCheckable(True)
        self.btnPieChart.setAutoExclusive(True)

        self.layoutActions.addWidget(self.btnPieChart)

        self.btnTextOutput = QToolButton(TimePlots)
        self.btnTextOutput.setObjectName("btnTextOutput")
        self.btnTextOutput.setIcon(icon("calendar-journal.svg"))
        self.btnTextOutput.setIconSize(_TOOLBAR_ICON_SIZE)
        self.btnTextOutput.setCheckable(True)
        self.btnTextOutput.setAutoExclusive(True)

        self.layoutActions.addWidget(self.btnTextOutput)

        self.horizontalSpacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutActions.addItem(self.horizontalSpacer)

        self.btnPrevWeek = QToolButton(TimePlots)
        self.btnPrevWeek.setObjectName("btnPrevWeek")
        self.btnPrevWeek.setIcon(icon("previous.svg"))
        self.btnPrevWeek.setIconSize(_TOOLBAR_ICON_SIZE)

        self.layoutActions.addWidget(self.btnPrevWeek)

        self.btnWorkWeek = QToolButton(TimePlots)
        self.btnWorkWeek.setObjectName("btnWorkWeek")
        self.btnWorkWeek.setIcon(icon("calendar-work-week.svg"))
        self.btnWorkWeek.setIconSize(_TOOLBAR_ICON_SIZE)

        self.layoutActions.addWidget(self.btnWorkWeek)

        self.btnNextWeek = QToolButton(TimePlots)
        self.btnNextWeek.setObjectName("btnNextWeek")
        self.btnNextWeek.setIcon(icon("next.svg"))
        self.btnNextWeek.setIconSize(_TOOLBAR_ICON_SIZE)

        self.layoutActions.addWidget(self.btnNextWeek)

        self.btnToday = QToolButton(TimePlots)
        self.btnToday.setObjectName("btnToday")
        self.btnToday.setIcon(icon("calendar-day.svg"))
        self.btnToday.setIconSize(_TOOLBAR_ICON_SIZE)

        self.layoutActions.addWidget(self.btnToday)

        self.lblStart = QLabel(TimePlots)
        self.lblStart.setObjectName("lblStart")

        self.layoutActions.addWidget(self.lblStart)

        self.deStart = QDateEdit(TimePlots)
        self.deStart.setObjectName("deStart")
        self.deStart.setCalendarPopup(True)
        self.deStart.setDate(QDate(7999, 12, 29))

        self.layoutActions.addWidget(self.deStart)

        self.lblEnd = QLabel(TimePlots)
        self.lblEnd.setObjectName("lblEnd")

        self.layoutActions.addWidget(self.lblEnd)

        self.deEnd = QDateEdit(TimePlots)
        self.deEnd.setObjectName("deEnd")
        self.deEnd.setCalendarPopup(True)

        self.layoutActions.addWidget(self.deEnd)

        self.layoutTimePlots.addLayout(self.layoutActions)

        self.layoutDraw = QVBoxLayout()
        self.layoutDraw.setSpacing(0)
        self.layoutDraw.setObjectName("layoutDraw")
        self.layoutInfo = QHBoxLayout()
        self.layoutInfo.setObjectName("layoutInfo")
        self.lblDurations = QLabel(TimePlots)
        self.lblDurations.setObjectName("lblDurations")

        self.layoutInfo.addWidget(self.lblDurations)

        self.hsInfo = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.layoutInfo.addItem(self.hsInfo)

        self.layoutDraw.addLayout(self.layoutInfo)

        self.frmTextOutput = QFrame(TimePlots)
        self.frmTextOutput.setObjectName("frmTextOutput")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(
            self.frmTextOutput.sizePolicy().hasHeightForWidth()
        )
        self.frmTextOutput.setSizePolicy(sizePolicy)
        self.frmTextOutput.setFrameShape(QFrame.StyledPanel)
        self.frmTextOutput.setFrameShadow(QFrame.Raised)
        self.layoutTextOutput = QVBoxLayout(self.frmTextOutput)
        self.layoutTextOutput.setObjectName("layoutTextOutput")
        self.layoutHtml = QHBoxLayout()
        self.layoutHtml.setObjectName("layoutHtml")
        self.lblHtml = QLabel(self.frmTextOutput)
        self.lblHtml.setObjectName("lblHtml")

        self.layoutHtml.addWidget(self.lblHtml)

        self.btnHtmlSave = QToolButton(self.frmTextOutput)
        self.btnHtmlSave.setObjectName("btnHtmlSave")
        self.btnHtmlSave.setIcon(icon("save.svg"))

        self.layoutHtml.addWidget(self.btnHtmlSave)

        self.layoutTextOutput.addLayout(self.layoutHtml)

        self.edtHtml = QTextEdit(self.frmTextOutput)
        self.edtHtml.setObjectName("edtHtml")

        self.layoutTextOutput.addWidget(self.edtHtml)

        self.layoutCsv = QHBoxLayout()
        self.layoutCsv.setObjectName("layoutCsv")
        self.lblCsv = QLabel(self.frmTextOutput)
        self.lblCsv.setObjectName("lblCsv")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblCsv.sizePolicy().hasHeightForWidth())
        self.lblCsv.setSizePolicy(sizePolicy1)

        self.layoutCsv.addWidget(self.lblCsv)

        self.cbCsvFull = QCheckBox(self.frmTextOutput)
        self.cbCsvFull.setObjectName("cbCsvFull")

        self.layoutCsv.addWidget(self.cbCsvFull)

        self.btnCsvSave = QToolButton(self.frmTextOutput)
        self.btnCsvSave.setObjectName("btnCsvSave")
        self.btnCsvSave.setIcon(icon("save.svg"))

        self.layoutCsv.addWidget(self.btnCsvSave)

        self.layoutTextOutput.addLayout(self.layoutCsv)

        self.edtCsv = QPlainTextEdit(self.frmTextOutput)
        self.edtCsv.setObjectName("edtCsv")

        self.layoutTextOutput.addWidget(self.edtCsv)

        self.layoutDraw.addWidget(self.frmTextOutput)

        self.frmTimeLines = QFrame(TimePlots)
        self.frmTimeLines.setObjectName("frmTimeLines")
        sizePolicy.setHeightForWidth(self.frmTimeLines.sizePolicy().hasHeightForWidth())
        self.frmTimeLines.setSizePolicy(sizePolicy)
        self.frmTimeLines.setFrameShape(QFrame.StyledPanel)
        self.frmTimeLines.setFrameShadow(QFrame.Raised)
        self.layoutTimeLines = QVBoxLayout(self.frmTimeLines)
        self.layoutTimeLines.setObjectName("layoutTimeLines")
        self.layoutTimeLines.setContentsMargins(4, 4, 4, 4)

        self.layoutDraw.addWidget(self.frmTimeLines)

        self.frmPieChart = QFrame(TimePlots)
        self.frmPieChart.setObjectName("frmPieChart")
        self.frmPieChart.setFrameShape(QFrame.StyledPanel)
        self.frmPieChart.setFrameShadow(QFrame.Raised)
        self.layoutPieChart = QVBoxLayout(self.frmPieChart)
        self.layoutPieChart.setObjectName("layoutPieChart")
        self.layoutPieChart.setContentsMargins(4, 4, 4, 4)

        self.layoutDraw.addWidget(self.frmPieChart)

        self.verticalSpacer = QSpacerItem(
            20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.layoutDraw.addItem(self.verticalSpacer)

        self.layoutDraw.setStretch(1, 1)
        self.layoutDraw.setStretch(2, 1)
        self.layoutDraw.setStretch(3, 1)

        self.layoutTimePlots.addLayout(self.layoutDraw)

        self.buttonBox = QDialogButtonBox(TimePlots)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.layoutTimePlots.addWidget(self.buttonBox)

        self.layoutTimePlots.setStretch(1, 1)
        QWidget.setTabOrder(self.deStart, self.deEnd)
        QWidget.setTabOrder(self.deEnd, self.btnHtmlSave)
        QWidget.setTabOrder(self.btnHtmlSave, self.edtHtml)
        QWidget.setTabOrder(self.edtHtml, self.cbCsvFull)
        QWidget.setTabOrder(self.cbCsvFull, self.btnCsvSave)
        QWidget.setTabOrder(self.btnCsvSave, self.edtCsv)
        QWidget.setTabOrder(self.edtCsv, self.btnTimeLines)
        QWidget.setTabOrder(self.btnTimeLines, self.btnPieChart)
        QWidget.setTabOrder(self.btnPieChart, self.btnTextOutput)
        QWidget.setTabOrder(self.btnTextOutput, self.btnPrevWeek)
        QWidget.setTabOrder(self.btnPrevWeek, self.btnWorkWeek)
        QWidget.setTabOrder(self.btnWorkWeek, self.btnToday)

        self.retranslateUi(TimePlots)
        self.buttonBox.accepted.connect(TimePlots.accept)
        self.buttonBox.rejected.connect(TimePlots.reject)

        QMetaObject.connectSlotsByName(TimePlots)

    # setupUi

    def retranslateUi(self, TimePlots):
        TimePlots.setWindowTitle(
            QCoreApplication.translate("TimePlots", "Diagrammes", None)
        )
        # if QT_CONFIG(tooltip)
        self.btnTimeLines.setToolTip(
            QCoreApplication.translate("TimePlots", "Visualisation temporelle", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.btnPieChart.setToolTip(
            QCoreApplication.translate("TimePlots", "Visualisation dur\u00e9es", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.btnTextOutput.setToolTip(
            QCoreApplication.translate(
                "TimePlots",
                "Visualisation dur\u00e9es sous forme de texte\net exportation CSV",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.btnPrevWeek.setToolTip(
            QCoreApplication.translate("TimePlots", "Reculer d'une semaine", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.btnWorkWeek.setToolTip(
            QCoreApplication.translate(
                "TimePlots",
                "Modifie les dates pour s\u00e9lectionner la semaine courante",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.btnNextWeek.setToolTip(
            QCoreApplication.translate("TimePlots", "Avancer d'une semaine", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.btnToday.setToolTip(
            QCoreApplication.translate(
                "TimePlots",
                "Modifie les dates pour s\u00e9lectionner aujourd'hui",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lblStart.setText(
            QCoreApplication.translate("TimePlots", "D\u00e9but:", None)
        )
        # if QT_CONFIG(tooltip)
        self.deStart.setToolTip(
            QCoreApplication.translate(
                "TimePlots",
                "Date de d\u00e9but de la p\u00e9riode \u00e0 consid\u00e9rer",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.deStart.setDisplayFormat(
            QCoreApplication.translate("TimePlots", "ddd yyyy-MM-dd  ", None)
        )
        self.lblEnd.setText(QCoreApplication.translate("TimePlots", "Fin:", None))
        # if QT_CONFIG(tooltip)
        self.deEnd.setToolTip(
            QCoreApplication.translate(
                "TimePlots",
                "Date de fin de la p\u00e9riode \u00e0 consid\u00e9rer",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.deEnd.setDisplayFormat(
            QCoreApplication.translate("TimePlots", "ddd yyyy-MM-dd   ", None)
        )
        self.lblDurations.setText(
            QCoreApplication.translate("TimePlots", "Dur\u00e9e jour", None)
        )
        self.lblHtml.setText(QCoreApplication.translate("TimePlots", "En html:", None))
        # if QT_CONFIG(tooltip)
        self.btnHtmlSave.setToolTip(
            QCoreApplication.translate(
                "TimePlots", "Sauvegarde au format HTML dans un fichier", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.edtHtml.setToolTip(
            QCoreApplication.translate(
                "TimePlots", "Repr\u00e9sentation textuelle", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.lblCsv.setText(
            QCoreApplication.translate("TimePlots", "Au format CSV:", None)
        )
        self.cbCsvFull.setText(QCoreApplication.translate("TimePlots", "Complet", None))
        # if QT_CONFIG(tooltip)
        self.btnCsvSave.setToolTip(
            QCoreApplication.translate(
                "TimePlots", "Sauvegarde au format CSV dans un fichier", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.edtCsv.setToolTip("")


# endif // QT_CONFIG(tooltip)
# retranslateUi
