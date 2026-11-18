from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QColorDialog, QLabel, QFrame, QComboBox, QSlider
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class TintEditor(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        layout = QVBoxLayout(self)
        
        # State Selector
        self.state_combo = QComboBox()
        self.state_combo.addItems(["Default", "Hover", "Active"])
        layout.addWidget(QLabel("Apply_to_State:"))
        layout.addWidget(self.state_combo)
        
        # Color
        self.color_btn = QPushButton("Pick_Tint_Color")
        self.current_color = QColor("#FFFFFF")
        self.color_btn.clicked.connect(self.pick_color)
        layout.addWidget(self.color_btn)
        
        # Intensity
        layout.addWidget(QLabel("Intensity:"))
        self.intensity_slider = QSlider(Qt.Horizontal)
        self.intensity_slider.setRange(0, 100)
        self.intensity_slider.setValue(50)
        layout.addWidget(self.intensity_slider)
        
        self.apply_btn = QPushButton("Apply_Tint")
        self.apply_btn.clicked.connect(self.apply_tint)
        layout.addWidget(self.apply_btn)
        
    def pick_color(self):
        color = QColorDialog.getColor(self.current_color)
        if color.isValid():
            self.current_color = color
            
    def apply_tint(self):
        state = self.state_combo.currentText().lower()
        settings = {
            "color": self.current_color.getRgb(),
            "intensity": self.intensity_slider.value() / 100.0
        }
        self.controller.set_tint_settings(state, settings)
