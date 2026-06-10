"""Header section for the Vulnerability Management PyQt GUI."""

from __future__ import annotations

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget

from ui_support import AssetManager, SHIELD_ICON, card, primary_button


class HeaderSection(QWidget):
    """Top title bar with brand icon, theme control, run status, and refresh."""

    def __init__(self, assets: AssetManager, on_theme_clicked, on_reset_logs) -> None:
        super().__init__()
        self.theme_button = primary_button("☀  Theme: Light", on_theme_clicked)
        self.theme_button.setObjectName("ThemeButton")
        self._build(assets, on_reset_logs)

    def _build(self, assets: AssetManager, on_reset_logs) -> None:
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        header_card = card()
        header_layout = QHBoxLayout(header_card)
        header_layout.setContentsMargins(24, 14, 18, 14)

        icon = assets.asset_label(SHIELD_ICON, QSize(48, 48), "🛡")
        icon.setObjectName("HeaderIcon")
        header_layout.addWidget(icon)

        title_block = QVBoxLayout()
        title = QLabel("Vulnerability Management Automation Tool")
        title.setObjectName("Title")
        subtitle = QLabel("Automate vulnerability assessment & reporting with ease")
        subtitle.setObjectName("Muted")
        title_block.addWidget(title)
        title_block.addWidget(subtitle)
        header_layout.addLayout(title_block, stretch=1)

        header_layout.addWidget(self.theme_button)
        status_button = primary_button("Run Status: ● Ready")
        status_button.setObjectName("StatusButton")
        header_layout.addWidget(status_button)
        header_layout.addWidget(primary_button("⟳", on_reset_logs))
        layout.addWidget(header_card)

    def set_theme_label(self, theme: str) -> None:
        self.theme_button.setText("🌙  Theme: Dark" if theme == "dark" else "☀  Theme: Light")
