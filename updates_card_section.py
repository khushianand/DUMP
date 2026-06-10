"""KPI/update cards below the header."""

from __future__ import annotations

from pathlib import Path

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from ui_support import AssetManager, KPI_ICONS, LIGHT, card


class UpdatesCardSection(QWidget):
    """Four dashboard update cards: vulnerabilities, unique vulns, time, and success."""

    def __init__(self, assets: AssetManager) -> None:
        super().__init__()
        self.assets = assets
        self._build()

    def _build(self) -> None:
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setHorizontalSpacing(14)
        metrics = [
            (KPI_ICONS["file_shield"], "Vulnerabilities Processed", "0", "Total sheet count: 0", LIGHT.blue),
            (KPI_ICONS["shield"], "Unique Vulnerabilities", "0", "Unique sheet count: 0", LIGHT.green),
            (KPI_ICONS["clock"], "Processing Time", "0s", "Elapsed time: 0s", LIGHT.purple),
            (KPI_ICONS["trending_up"], "Success Rate", "0%", "Completion: 0%", LIGHT.orange),
        ]
        for col, metric in enumerate(metrics):
            layout.addWidget(self._metric_card(*metric), 0, col)
            layout.setColumnStretch(col, 1)

    def _metric_card(self, icon: Path, title: str, value: str, subtitle: str, color: str) -> QWidget:
        metric_card = card()
        layout = QHBoxLayout(metric_card)
        layout.setContentsMargins(18, 16, 18, 16)

        bubble = self.assets.asset_label(icon, QSize(48, 48), "")
        bubble.setStyleSheet(f"background:{color}; color:white; border-radius:24px; min-width:48px; min-height:48px; font-size:24px;")
        layout.addWidget(bubble)

        text = QVBoxLayout()
        label = QLabel(title)
        label.setObjectName("MetricTitle")
        number = QLabel(value)
        number.setStyleSheet(f"color:{color}; font-size:26px; font-weight:800;")
        sub = QLabel(subtitle)
        sub.setStyleSheet(f"color:{color}; font-size:11px; font-weight:700;")
        text.addWidget(label)
        text.addWidget(number)
        text.addWidget(sub)
        layout.addLayout(text, stretch=1)

        spark = QLabel("⌁⌁⌁")
        spark.setStyleSheet(f"color:{color}; font-size:22px;")
        layout.addWidget(spark)
        return metric_card
