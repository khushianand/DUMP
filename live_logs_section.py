"""Live logs section for the PyQt GUI."""

from __future__ import annotations

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import QHBoxLayout, QHeaderView, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from ui_support import AssetManager, Palette, card, primary_button


class LiveLogsSection(QWidget):
    """Searchable live log table with theme-aware decoration and row colors."""

    def __init__(self, assets: AssetManager, palette: Palette, theme: str) -> None:
        super().__init__()
        self.assets = assets
        self.palette = palette
        self.theme = theme
        self.log_table = QTableWidget(0, 3)
        self.decoration_art: QLabel | None = None
        self._build()

    def _build(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        logs_card = card()
        card_layout = QVBoxLayout(logs_card)
        card_layout.setContentsMargins(16, 10, 16, 12)

        top = QHBoxLayout()
        title = QLabel("●  Live Logs")
        title.setObjectName("LogTitle")
        top.addWidget(title)
        top.addStretch(1)
        self.decoration_art = self.assets.asset_label(self.assets.decoration_asset_path(self.theme), QSize(150, 46), "")
        self.decoration_art.setObjectName("LogDecoration")
        top.addWidget(self.decoration_art)
        top.addWidget(primary_button("▣  Open Output File"))
        card_layout.addLayout(top)

        search = QLineEdit("Search logs...")
        search.setMaximumWidth(260)
        card_layout.addWidget(search)
        self.log_table.setHorizontalHeaderLabels(["Time", "Level", "Message"])
        self.log_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.log_table.verticalHeader().setVisible(False)
        self.log_table.setAlternatingRowColors(True)
        card_layout.addWidget(self.log_table, stretch=1)
        layout.addWidget(logs_card)

        for row in [
            ("15:05:01", "INFO", "Application initialized successfully"),
            ("15:05:02", "INFO", "Theme switched to Light"),
            ("15:05:03", "SUCCESS", "Configuration loaded successfully"),
            ("15:05:04", "WARNING", "No input file selected. Please choose a raw file to continue."),
            ("15:05:05", "INFO", "Ready to run assessment"),
            ("15:05:06", "ERROR", "Sample error log message (example)"),
        ]:
            self.add_log(*row)

    def add_log(self, time_text: str, level: str, message: str) -> None:
        row = self.log_table.rowCount()
        self.log_table.insertRow(row)
        level_colors, row_backgrounds = self._log_colors()
        for col, value in enumerate([time_text, level, message]):
            item = QTableWidgetItem(value)
            item.setForeground(QColor(level_colors.get(level, self.palette.text) if col == 1 else self.palette.text))
            item.setBackground(QColor(row_backgrounds.get(level, self.palette.log_bg)))
            if col == 1:
                item.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
            self.log_table.setItem(row, col, item)
        self.log_table.scrollToBottom()

    def refresh_theme(self, palette: Palette, theme: str) -> None:
        self.palette = palette
        self.theme = theme
        if self.decoration_art is not None:
            self.assets.set_label_asset(self.decoration_art, self.assets.decoration_asset_path(theme), QSize(150, 46), "")
        self.recolor_log_rows()

    def recolor_log_rows(self) -> None:
        level_colors, row_backgrounds = self._log_colors()
        for row in range(self.log_table.rowCount()):
            level_item = self.log_table.item(row, 1)
            level = level_item.text() if level_item else ""
            for col in range(self.log_table.columnCount()):
                item = self.log_table.item(row, col)
                if not item:
                    continue
                item.setForeground(QColor(level_colors.get(level, self.palette.text) if col == 1 else self.palette.text))
                item.setBackground(QColor(row_backgrounds.get(level, self.palette.log_bg)))

    def _log_colors(self) -> tuple[dict[str, str], dict[str, str]]:
        return (
            {
                "INFO": self.palette.button_blue,
                "SUCCESS": self.palette.success_badge,
                "WARNING": self.palette.warning,
                "ERROR": self.palette.red,
            },
            {
                "INFO": self.palette.log_info,
                "SUCCESS": self.palette.log_success,
                "WARNING": self.palette.log_warning,
                "ERROR": self.palette.log_error,
            },
        )
