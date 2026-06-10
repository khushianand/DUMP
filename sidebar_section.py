"""Sidebar navigation and illustration section."""

from __future__ import annotations

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

from ui_support import AssetManager, card


class SidebarSection(QWidget):
    """Left navigation rail with theme-aware security illustration."""

    def __init__(self, assets: AssetManager, current_theme: str, on_dashboard, on_settings) -> None:
        super().__init__()
        self.assets = assets
        self.current_theme = current_theme
        self.dashboard_button: QPushButton | None = None
        self.settings_button: QPushButton | None = None
        self.sidebar_art: QLabel | None = None
        self._build(on_dashboard, on_settings)

    def _build(self, on_dashboard, on_settings) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        side = card(width=180, object_name="Sidebar")
        side_layout = QVBoxLayout(side)
        side_layout.setContentsMargins(12, 14, 12, 18)
        side_layout.setSpacing(8)

        nav_items = ["⌂  Dashboard", "▣  Make Report", "▧  Generate Tracking", "◉  Add VAMS Data", "▣  Show Summary", "☷  Logs", "⚙  Settings"]
        for index, text in enumerate(nav_items):
            button = QPushButton(("▌  " if index == 0 else "") + text)
            button.setObjectName("NavButton")
            if index == 0:
                self.dashboard_button = button
                button.clicked.connect(on_dashboard)
            elif text.endswith("Settings"):
                self.settings_button = button
                button.clicked.connect(on_settings)
            else:
                button.clicked.connect(on_dashboard)
            side_layout.addWidget(button)

        side_layout.addStretch(1)
        self.sidebar_art = self.assets.asset_label(self.assets.sidebar_asset_path(self.current_theme), QSize(150, 120), "🛡\n\nStronger today,\nSafer tomorrow.")
        self.sidebar_art.setObjectName("SideArt")
        self.sidebar_art.setAlignment(Qt.AlignmentFlag.AlignCenter)
        side_layout.addWidget(self.sidebar_art)

        caption = QLabel("Stronger today,\nSafer tomorrow.")
        caption.setObjectName("SideArtCaption")
        caption.setAlignment(Qt.AlignmentFlag.AlignCenter)
        side_layout.addWidget(caption)
        layout.addWidget(side)

    def refresh_theme(self, theme: str) -> None:
        self.current_theme = theme
        if self.sidebar_art is not None:
            self.assets.set_label_asset(self.sidebar_art, self.assets.sidebar_asset_path(theme), QSize(150, 120), "🛡\n\nStronger today,\nSafer tomorrow.")

    def set_active_nav(self, active: str) -> None:
        if self.dashboard_button:
            self._set_button_active(self.dashboard_button, active == "dashboard")
        if self.settings_button:
            self._set_button_active(self.settings_button, active == "settings")

    def _set_button_active(self, button: QPushButton, active: bool) -> None:
        button.setProperty("active", active)
        button.style().unpolish(button)
        button.style().polish(button)
