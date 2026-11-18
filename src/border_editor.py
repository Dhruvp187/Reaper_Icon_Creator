from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QColorDialog, QLabel, QFrame, QComboBox, QSpinBox
from PySide6.QtGui import QColor

class BorderEditor(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        layout = QVBoxLayout(self)
        
        # State Selector
        self.state_combo = QComboBox()
        self.state_combo.addItems(["Default", "Hover", "Active"])
        layout.addWidget(QLabel("Apply_to_State:"))
        layout.addWidget(self.state_combo)
        
        # Thickness
        self.thickness_spin = QSpinBox()
        self.thickness_spin.setRange(0, 20)
        layout.addWidget(QLabel("Thickness:"))
        layout.addWidget(self.thickness_spin)
        
        # Roundness
        self.radius_spin = QSpinBox()
        self.radius_spin.setRange(0, 50)
        layout.addWidget(QLabel("Corner_Radius:"))
        layout.addWidget(self.radius_spin)
        
        # Color
        self.color_btn = QPushButton("Pick_Border_Color")
        self.current_color = QColor("#000000")
        self.color_btn.clicked.connect(self.pick_color)
        layout.addWidget(self.color_btn)
        
        self.apply_btn = QPushButton("Apply_Border")
        self.apply_btn.clicked.connect(self.apply_border)
        layout.addWidget(self.apply_btn)
        
    def pick_color(self):
        color = QColorDialog.getColor(self.current_color)
        if color.isValid():
            self.current_color = color
            
    def apply_border(self):
        state = self.state_combo.currentText().lower()
        settings = {
            "color": self.current_color.name(),
            "thickness": self.thickness_spin.value(),
            "radius": self.radius_spin.value()
        }
        self.controller.set_border_settings(state, settings)
