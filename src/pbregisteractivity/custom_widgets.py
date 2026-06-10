"""
Enregistre l'activité
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QListWidgetItem

from .activity import Activity


class QActivityListWidgetItem(QListWidgetItem):
    def __init__(self, value: Activity):
        super().__init__()
        start = value.start.strftime("%Y/%m/%d %H:%M:%S")
        end = value.end.strftime("%Y/%m/%d %H:%M:%S")
        duration = str(value.end - value.start)
        txt = f"{value.name} ({start} - {duration})"
        self.setText(txt)
        txt = f"Début: {start}<br>Fin: {end}<br>Durée: {duration}"
        self.setToolTip(txt)
        txt = f"{value.name} - Début: {start}; Fin: {end}; Durée: {duration}"
        if value.is_automatic:
            self.setBackground(QColor(Qt.GlobalColor.darkRed))
            self.setForeground(QColor(Qt.GlobalColor.yellow))
        self.setStatusTip(txt)
        self.setData(Qt.ItemDataRole.UserRole, value)

    def value(self):
        return self.data(Qt.ItemDataRole.UserRole)
