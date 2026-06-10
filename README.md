# Vulnerability Management PyQt GUI

This repository contains a **PyQt6-only** desktop GUI implementation inspired by the provided Vulnerability Management Excel Automation screenshot.

## Install dependencies

```bash
python -m pip install PyQt6
```

Or install from the included requirements file:

```bash
python -m pip install -r requirements.txt
```

## Light theme palette

The default Light theme uses a soft SaaS-style palette: background `#F7F9FC`, cards `#FFFFFF`, primary text `#1F2937`, borders `#E4EAF3`, primary blue `#2563EB`, success green `#22C55E`, purple accent `#7C3AED`, and orange accent `#F59E0B`.

## Dark theme palette

The Dark theme uses a premium slate-grey cybersecurity palette: background `#353F4A`, cards `#404A56`, sidebar `#38424D`, panels `#444E5A`, border `#5B6673`, primary text `#F4F7FA`, secondary text `#C8D0D8`, muted text `#98A3AF`, disabled text `#8A949F`, blue accent `#4A90FF`, green accent `#2EE67B`, purple accent `#9B6DFF`, purple glow `#B794F4`, orange accent `#FFB020`, and orange glow `#FFD166`.

## Run the application

```bash
python vulnerability_gui_pyqt.py
```

The PyQt app includes the dashboard header, side navigation, metric cards, operation mode controls, report input fields, browse buttons, run action, live logs table, footer status area, and Light/Dark theme switching from both the header theme button and the Settings panel.
