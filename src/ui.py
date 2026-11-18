from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from src.preview import PreviewArea
from src.controls import ControlPanel

ANALOG_STYLE = """
    QMainWindow { background-color: #1a1a1a; }
    QWidget { color: #c0c0c0; font-family: 'Courier New', monospace; }
    QLineEdit { background-color: #262626; border: none; border-bottom: 1px solid #444; color: #e0e0e0; }
    QPushButton { background-color: transparent; border: 1px solid #555; padding: 5px; color: #aaa; }
    QPushButton:hover { border: 1px solid #eee; color: #eee; }
    QLabel { border: 1px solid #333; background: #111; }
    QGroupBox { border: 1px solid #333; margin-top: 10px; padding: 10px; font-weight: bold; }
"""

class AppUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("REAPER_Icon_Creator")
        self.resize(1400, 700)
        
        self.central = QWidget()
        self.setCentralWidget(self.central)
        main_layout = QVBoxLayout(self.central)

        # Body (Split)
        body_layout = QHBoxLayout()
        self.preview_area = PreviewArea()
        self.controls = ControlPanel(controller)
        
        # Keep compatibility with existing main.py
        self.toolbar = self.controls
        
        body_layout.addWidget(self.preview_area, stretch=2)
        body_layout.addWidget(self.controls, stretch=1)
        
        main_layout.addLayout(body_layout)
        self.setStyleSheet(ANALOG_STYLE)

