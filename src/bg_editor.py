from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QColorDialog, QLabel, QFrame, QComboBox
from PySide6.QtGui import QColor

class BackgroundEditor(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.current_color = QColor("#FFFFFF")
        
        layout = QVBoxLayout(self)
        
        # State Selector
        self.state_combo = QComboBox()
        self.state_combo.addItems(["Default", "Hover", "Active"])
        layout.addWidget(QLabel("Apply_to_State:"))
        layout.addWidget(self.state_combo)
        
        btn_layout = QHBoxLayout()
        self.color_btn = QPushButton("Pick_Color")
        self.apply_btn = QPushButton("Apply")
        
        self.preview_box = QFrame()
        self.preview_box.setFixedSize(30, 30)
        self.preview_box.setStyleSheet(f"background-color: {self.current_color.name()}; border: 1px solid black;")
        
        self.color_btn.clicked.connect(self.pick_color)
        self.apply_btn.clicked.connect(self.apply_color)
        
        btn_layout.addWidget(self.color_btn)
        btn_layout.addWidget(self.preview_box)
        btn_layout.addWidget(self.apply_btn)
        
        layout.addLayout(btn_layout)
        
    def pick_color(self):
        color = QColorDialog.getColor(self.current_color)
        if color.isValid():
            self.current_color = color
            self.preview_box.setStyleSheet(f"background-color: {self.current_color.name()}; border: 1px solid black;")
            
    def apply_color(self):
        state = self.state_combo.currentText().lower()
        self.controller.set_background_color(state, self.current_color.name())
