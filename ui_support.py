"""Shared theme, asset, and widget helpers for the PyQt GUI."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QIcon, QMovie, QPixmap
from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QLabel, QPushButton, QSizePolicy


ASSETS_DIR = Path(__file__).resolve().parent / "assets"
ICON_DIR = ASSETS_DIR / "icons"
ILLUSTRATION_DIR = ASSETS_DIR / "illustrations"
GIF_DIR = ASSETS_DIR / "gifs"
SHIELD_ICON = ICON_DIR / "shield.svg"
SIDEBAR_GIF = GIF_DIR / "security-loop.gif"
SIDEBAR_ILLUSTRATION = ILLUSTRATION_DIR / "security-dashboard.svg"
SIDEBAR_LIGHT_ILLUSTRATION = ILLUSTRATION_DIR / "sidebar-light.svg"
SIDEBAR_DARK_ILLUSTRATION = ILLUSTRATION_DIR / "sidebar-dark.svg"
DOT_GRID_DECORATION = ASSETS_DIR / "decorations" / "dot-grid.svg"
WAVE_MESH_DECORATION = ASSETS_DIR / "decorations" / "wave-mesh.svg"
KPI_ICONS = {
    "file_shield": ASSETS_DIR / "kpi" / "file-shield.svg",
    "shield": ASSETS_DIR / "kpi" / "shield.svg",
    "clock": ASSETS_DIR / "kpi" / "clock.svg",
    "trending_up": ASSETS_DIR / "kpi" / "trending-up.svg",
}


@dataclass(frozen=True)
class Palette:
    bg: str
    card: str
    card_alt: str
    sidebar_bg: str
    hover_bg: str
    border: str
    card_border: str
    divider: str
    input_border: str
    input_bg: str
    text: str
    secondary_text: str
    muted: str
    disabled: str
    placeholder: str
    blue: str
    button_blue: str
    light_blue: str
    sidebar_active: str
    blue_glow: str
    green: str
    success_light: str
    status_ready: str
    success_badge: str
    purple: str
    purple_accent: str
    purple_light: str
    run_button: str
    orange: str
    warning: str
    orange_light: str
    red: str
    danger: str
    error_light: str
    log_bg: str
    log_info: str
    log_success: str
    log_warning: str
    log_error: str
    table_alt: str
    button_hover: str
    nav_hover: str
    version_bg: str


LIGHT = Palette(
    bg="#F7F9FC",
    card="#FFFFFF",
    card_alt="#F3F6FB",
    sidebar_bg="#FAFBFD",
    hover_bg="#EEF4FF",
    border="#E4EAF3",
    card_border="#DCE4EF",
    divider="#E8EDF5",
    input_border="#D7E0EC",
    input_bg="#FFFFFF",
    text="#1F2937",
    secondary_text="#4B5563",
    muted="#6B7280",
    disabled="#94A3B8",
    placeholder="#94A3B8",
    blue="#2563EB",
    button_blue="#3B82F6",
    light_blue="#60A5FA",
    sidebar_active="#EAF2FF",
    blue_glow="#DBEAFE",
    green="#22C55E",
    success_light="#DCFCE7",
    status_ready="#10B981",
    success_badge="#16A34A",
    purple="#7C3AED",
    purple_accent="#8B5CF6",
    purple_light="#F3E8FF",
    run_button="#6D28D9",
    orange="#F59E0B",
    warning="#FB923C",
    orange_light="#FEF3C7",
    red="#EF4444",
    danger="#DC2626",
    error_light="#FEE2E2",
    log_bg="#FFFFFF",
    log_info="#EFF6FF",
    log_success="#ECFDF5",
    log_warning="#FFF7ED",
    log_error="#FEF2F2",
    table_alt="#F3F6FB",
    button_hover="#2563EB",
    nav_hover="#EEF4FF",
    version_bg="#DBEAFE",
)
DARK = Palette(
    bg="#353F4A",
    card="#404A56",
    card_alt="#444E5A",
    sidebar_bg="#38424D",
    hover_bg="#394451",
    border="#5B6673",
    card_border="#4A5562",
    divider="#56606B",
    input_border="#5C6672",
    input_bg="#343D48",
    text="#F4F7FA",
    secondary_text="#C8D0D8",
    muted="#98A3AF",
    disabled="#8A949F",
    placeholder="#8A949F",
    blue="#4080D9",
    button_blue="#4A90FF",
    light_blue="#5B9DFF",
    sidebar_active="#2D5FAE",
    blue_glow="#7FB3FF",
    green="#22C55E",
    success_light="#255C41",
    status_ready="#2EE67B",
    success_badge="#2EE67B",
    purple="#7C3AED",
    purple_accent="#9B6DFF",
    purple_light="#B794F4",
    run_button="#9B6DFF",
    orange="#F59E0B",
    warning="#FFB020",
    orange_light="#FFD166",
    red="#EF4444",
    danger="#EF4444",
    error_light="#6C2B2B",
    log_bg="#303945",
    log_info="#2F4F80",
    log_success="#255C41",
    log_warning="#6A4A1F",
    log_error="#6C2B2B",
    table_alt="#394451",
    button_hover="#5B9DFF",
    nav_hover="#394451",
    version_bg="#2F4F80",
)


class AssetManager:
    """Loads static SVG/bitmap assets and optional GIF animations."""

    def __init__(self) -> None:
        self.movies: list[QMovie] = []

    def icon(self, path: Path) -> QIcon:
        return QIcon(str(path)) if path.exists() else QIcon()

    def sidebar_asset_path(self, theme: str) -> Path:
        if SIDEBAR_GIF.exists():
            return SIDEBAR_GIF
        themed_asset = SIDEBAR_DARK_ILLUSTRATION if theme == "dark" else SIDEBAR_LIGHT_ILLUSTRATION
        return themed_asset if themed_asset.exists() else SIDEBAR_ILLUSTRATION

    def decoration_asset_path(self, theme: str) -> Path:
        return WAVE_MESH_DECORATION if theme == "dark" else DOT_GRID_DECORATION

    def asset_label(self, path: Path, size: QSize, fallback_text: str) -> QLabel:
        label = QLabel()
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFixedSize(size)
        self.set_label_asset(label, path, size, fallback_text)
        return label

    def set_label_asset(self, label: QLabel, path: Path, size: QSize, fallback_text: str) -> None:
        label.clear()

        if path.exists() and path.suffix.lower() == ".gif":
            movie = QMovie(str(path))
            if movie.isValid():
                movie.setScaledSize(size)
                label.setMovie(movie)
                movie.start()
                self.movies.append(movie)
                return

        if path.exists():
            pixmap = QPixmap(str(path))
            if not pixmap.isNull():
                label.setPixmap(pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                return

        label.setText(fallback_text)


def card(width: int | None = None, object_name: str = "Card") -> QFrame:
    frame = QFrame()
    frame.setObjectName(object_name)
    if width:
        frame.setFixedWidth(width)
    frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    shadow = QGraphicsDropShadowEffect(frame)
    shadow.setBlurRadius(20)
    shadow.setOffset(0, 4)
    shadow.setColor(QColor(37, 99, 235, 20))
    frame.setGraphicsEffect(shadow)
    return frame


def primary_button(text: str, slot=None) -> QPushButton:
    button = QPushButton(text)
    button.setObjectName("PrimaryButton")
    if slot:
        button.clicked.connect(slot)
    return button


def style_sheet(p: Palette) -> str:
    danger_bg = p.error_light
    danger_border = p.danger
    return f"""
    #Root {{ background: {p.bg}; font-family: 'Segoe UI'; color: {p.text}; }}
    QWidget {{ background: {p.bg}; color: {p.text}; font-family: 'Segoe UI'; }}
    #Card {{ background: {p.card}; border: 1px solid {p.card_border}; border-radius: 10px; }}
    #Sidebar {{ background: {p.sidebar_bg}; border: 1px solid {p.card_border}; border-radius: 10px; }}
    QLabel {{ color: {p.text}; font-size: 13px; background: transparent; }}
    #Title {{ font-size: 18px; font-weight: 800; }}
    #Muted {{ color: {p.muted}; }}
    #HeaderIcon {{ color: {p.blue}; font-size: 34px; }}
    #MetricTitle {{ font-size: 12px; font-weight: 700; }}
    #LogTitle {{ color: {p.green}; font-weight: 800; }}
    #SideArt {{ color: {p.text}; font-size: 14px; padding: 6px; }}
    #SideArtCaption {{ color: {p.secondary_text}; font-size: 13px; padding-top: 6px; }}
    #LogDecoration {{ padding-right: 10px; }}
    #Version {{ background: {p.version_bg}; color: {p.blue}; border-radius: 14px; padding: 6px 22px; font-weight: 800; }}
    QPushButton#PrimaryButton {{ background: {p.button_blue}; color: white; border: 1px solid {p.button_blue}; border-radius: 7px; padding: 9px 16px; font-weight: 700; }}
    QPushButton#PrimaryButton:hover {{ background: {p.button_hover}; }}
    QPushButton#SecondaryButton {{ background: {p.card_alt}; color: {p.secondary_text}; border: 1px solid {p.border}; border-radius: 7px; padding: 9px 16px; font-weight: 700; }}
    QPushButton#SecondaryButton:hover {{ background: {p.nav_hover}; color: {p.blue}; }}
    QPushButton#ThemeButton {{ background: {p.card}; color: {p.text}; border: 1px solid {p.border}; border-radius: 7px; padding: 9px 16px; font-weight: 700; }}
    QPushButton#ThemeButton:hover {{ background: {p.hover_bg}; color: {p.blue}; }}
    QPushButton#StatusButton {{ background: {p.card}; color: {p.text}; border: 1px solid {p.status_ready}; border-radius: 7px; padding: 9px 16px; font-weight: 700; }}
    QPushButton#DangerButton {{ background: {danger_bg}; color: {p.red}; border: 1px solid {danger_border}; border-radius: 7px; padding: 9px 16px; font-weight: 700; }}
    QPushButton#RunButton {{ background: {p.run_button}; color: white; border: 0; border-radius: 7px; padding: 10px 20px; font-weight: 800; }}
    QPushButton#NavButton {{ background: transparent; color: {p.text}; border: 0; border-radius: 7px; padding: 10px 12px; text-align: left; font-weight: 700; }}
    QPushButton#NavButton:hover {{ background: {p.hover_bg}; color: {p.blue}; }}
    QPushButton#NavButton[active="true"] {{ background: {p.sidebar_active}; color: {p.blue}; }}
    QLineEdit, QComboBox {{ background: {p.input_bg}; border: 1px solid {p.input_border}; border-radius: 6px; padding: 8px 10px; color: {p.text}; }}
    QLineEdit[placeholderText] {{ color: {p.placeholder}; }}
    QComboBox QAbstractItemView {{ background: {p.card}; color: {p.text}; selection-background-color: {p.nav_hover}; border: 1px solid {p.border}; }}
    QRadioButton {{ color: {p.text}; font-weight: 600; background: transparent; }}
    QTableWidget {{ background: {p.log_bg}; alternate-background-color: {p.table_alt}; border: 1px solid {p.border}; border-radius: 8px; gridline-color: {p.border}; color: {p.text}; }}
    QHeaderView::section {{ background: {p.card_alt}; color: {p.text}; padding: 8px; border: 0; border-bottom: 1px solid {p.divider}; font-weight: 800; }}
    QScrollBar:vertical {{ background: {p.card}; width: 12px; margin: 2px; }}
    QScrollBar::handle:vertical {{ background: {p.input_border}; border-radius: 5px; min-height: 24px; }}
    """
