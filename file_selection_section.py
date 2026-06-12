"""Operation mode and file selection sections."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QButtonGroup, QComboBox, QGridLayout, QLabel, QLineEdit, QRadioButton, QWidget

from ui_support import card, primary_button


class OperationBar(QWidget):
    """Operation mode radios and utility buttons."""

    def __init__(self, on_theme_clicked, on_export_logs, on_reset_logs) -> None:
        super().__init__()
        self.mode_group = QButtonGroup(self)
        self._build(on_theme_clicked, on_export_logs, on_reset_logs)

    def _build(self, on_theme_clicked, on_export_logs, on_reset_logs) -> None:
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        bar = card()
        bar_layout = QGridLayout(bar)
        bar_layout.setContentsMargins(18, 12, 18, 12)
        bar_layout.addWidget(QLabel("Operation Mode:"), 0, 0)
        for col, mode in enumerate(["Inputs", "Parse", "Compare", "Enrich", "Write"], start=1):
            radio = QRadioButton(mode)
            radio.setChecked(mode == "Inputs")
            self.mode_group.addButton(radio)
            bar_layout.addWidget(radio, 0, col)
        bar_layout.addWidget(primary_button("⚙  Theme", on_theme_clicked), 1, 0)
        bar_layout.addWidget(primary_button("▣  Export Logs", on_export_logs), 1, 1)
        reset = primary_button("⟳  Reset", on_reset_logs)
        reset.setObjectName("DangerButton")
        bar_layout.addWidget(reset, 1, 2)
        bar_layout.setColumnStretch(6, 1)
        layout.addWidget(bar)


class FileSelectionSection(QWidget):
    """Report form section with file inputs, sheet selector, and run button."""

    def __init__(self, raw_file: QLineEdit, output_file: QLineEdit, sheet_combo: QComboBox, on_raw_browse, on_output_browse, on_run) -> None:
        super().__init__()
        self.raw_file = raw_file
        self.output_file = output_file
        self.sheet_combo = sheet_combo
        self.tab_labels: list[QLabel] = []
        self._build(on_raw_browse, on_output_browse, on_run)

    def _build(self, on_raw_browse, on_output_browse, on_run) -> None:
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        form = card()
        form_layout = QGridLayout(form)
        form_layout.setContentsMargins(28, 16, 28, 16)
        form_layout.setHorizontalSpacing(12)

        for col, tab in enumerate(["▣  Make Report", "▣  Generate Tracking", "◉  Add VAMS Data", "☷  Show Summary"]):
            tab_label = QLabel(tab)
            tab_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tab_labels.append(tab_label)
            form_layout.addWidget(tab_label, 0, col)

        self._file_row(form_layout, 1, "▧  Raw File", self.raw_file, on_raw_browse)
        form_layout.addWidget(QLabel("▦  Raw Sheet"), 3, 0)
        self.sheet_combo.addItems(["Select sheet", "Sheet1", "Vulnerabilities", "Assets"])
        form_layout.addWidget(self.sheet_combo, 4, 0, 1, 2)
        self._file_row(form_layout, 5, "▧  Output File", self.output_file, on_output_browse)
        run = primary_button("▷  Run Assessment", on_run)
        run.setObjectName("RunButton")
        form_layout.addWidget(run, 7, 3, alignment=Qt.AlignmentFlag.AlignRight)
        for col in range(4):
            form_layout.setColumnStretch(col, 1)
        layout.addWidget(form)

    def _file_row(self, layout: QGridLayout, row: int, label: str, field: QLineEdit, handler) -> None:
        field.setMinimumHeight(34)
        layout.addWidget(QLabel(label), row, 0, 1, 4)
        layout.addWidget(field, row + 1, 0, 1, 3)
        layout.addWidget(primary_button("▣  Browse", handler), row + 1, 3)

    def refresh_theme(self, palette) -> None:
        for index, label in enumerate(self.tab_labels):
            color = palette.blue if index == 0 else palette.text
            label.setStyleSheet(f"color:{color}; font-weight:700; padding:8px 28px;")
