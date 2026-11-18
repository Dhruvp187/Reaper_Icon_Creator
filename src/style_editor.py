from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QColorDialog, 
                             QLabel, QFrame, QGroupBox, QSpinBox, QSlider)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class StyleEditor(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.current_state = "default"
        
        layout = QVBoxLayout(self)
        
        # State Buttons
        btn_layout = QHBoxLayout()
        self.btn_default = QPushButton("Default")
        self.btn_hover = QPushButton("Hover")
        self.btn_active = QPushButton("Active")
        for btn in [self.btn_default, self.btn_hover, self.btn_active]:
            btn.setCheckable(True)
            btn.setStyleSheet("QPushButton:checked { background-color: #d78300; color: white; border: 1px solid #ff9900; }")
            btn.clicked.connect(self.set_state)
            btn_layout.addWidget(btn)
        self.btn_default.setChecked(True)
        layout.addLayout(btn_layout)
        
        # Color Preview helper
        def create_preview_box():
            box = QFrame()
            box.setFixedSize(20, 20)
            box.setStyleSheet("background-color: transparent; border: 1px solid #555;")
            return box
        
        # Background
        bg_group = QGroupBox("Background")
        bg_layout = QVBoxLayout(bg_group)
        bg_row = QHBoxLayout()
        self.bg_btn = QPushButton("Select_Color")
        self.bg_preview = create_preview_box()
        self.bg_btn.clicked.connect(self.pick_bg)
        bg_row.addWidget(self.bg_preview)
        bg_row.addWidget(self.bg_btn)
        bg_layout.addLayout(bg_row)
        self.apply_bg_btn = QPushButton("Apply_Background")
        self.apply_bg_btn.clicked.connect(self.apply_style_bg)
        bg_layout.addWidget(self.apply_bg_btn)
        layout.addWidget(bg_group)
        
        # Border
        border_group = QGroupBox("Border")
        border_layout = QVBoxLayout(border_group)
        
        dims_row = QHBoxLayout()
        thickness_group = QGroupBox("Thickness")
        thickness_layout = QVBoxLayout(thickness_group)
        self.border_thick = QSpinBox()
        thickness_layout.addWidget(self.border_thick)
        dims_row.addWidget(thickness_group)
        
        radius_group = QGroupBox("Radius")
        radius_layout = QVBoxLayout(radius_group)
        self.border_radius = QSpinBox()
        radius_layout.addWidget(self.border_radius)
        dims_row.addWidget(radius_group)
        
        border_layout.addLayout(dims_row)
        
        color_row = QHBoxLayout()
        self.border_btn = QPushButton("Select_Color")
        self.border_preview = create_preview_box()
        self.border_btn.clicked.connect(self.pick_border)
        color_row.addWidget(self.border_preview)
        color_row.addWidget(self.border_btn)
        border_layout.addLayout(color_row)
        
        self.apply_border_btn = QPushButton("Apply_Border")
        self.apply_border_btn.clicked.connect(lambda: self.apply_style("border"))
        border_layout.addWidget(self.apply_border_btn)
        layout.addWidget(border_group)
        
        # Tint
        tint_group = QGroupBox("Tint")
        tint_layout = QVBoxLayout(tint_group)
        
        intensity_group = QGroupBox("Intensity")
        intensity_layout = QVBoxLayout(intensity_group)
        self.tint_slider = QSlider(Qt.Horizontal)
        self.tint_slider.setRange(0, 100)
        intensity_layout.addWidget(self.tint_slider)
        tint_layout.addWidget(intensity_group)
        
        color_row = QHBoxLayout()
        self.tint_btn = QPushButton("Select_Color")
        self.tint_preview = create_preview_box()
        self.tint_btn.clicked.connect(self.pick_tint)
        color_row.addWidget(self.tint_preview)
        color_row.addWidget(self.tint_btn)
        tint_layout.addLayout(color_row)
        
        self.apply_tint_btn = QPushButton("Apply_Tint")
        self.apply_tint_btn.clicked.connect(lambda: self.apply_style("tint"))
        tint_layout.addWidget(self.apply_tint_btn)
        layout.addWidget(tint_group)

    def set_state(self):
        sender = self.sender()
        self.current_state = sender.text().lower()
        for btn in [self.btn_default, self.btn_hover, self.btn_active]:
            btn.setChecked(btn == sender)

    def pick_bg(self):
        self.bg_color = QColorDialog.getColor(QColor(255, 255, 255), self, options=QColorDialog.ShowAlphaChannel)
        if self.bg_color.isValid():
            self.bg_preview.setStyleSheet(f"background-color: {self.bg_color.name()}; border: 1px solid #555;")

    def pick_border(self):
        self.border_color = QColorDialog.getColor(QColor(0, 0, 0), self, options=QColorDialog.ShowAlphaChannel)
        if self.border_color.isValid():
            self.border_preview.setStyleSheet(f"background-color: {self.border_color.name()}; border: 1px solid #555;")

    def pick_tint(self):
        self.tint_color = QColorDialog.getColor(QColor(255, 255, 255), self, options=QColorDialog.ShowAlphaChannel)
        if self.tint_color.isValid():
            self.tint_preview.setStyleSheet(f"background-color: {self.tint_color.name()}; border: 1px solid #555;")

    def apply_style(self, style_type):
        state_settings = self.controller.styles[self.current_state].copy()
        
        if style_type == "border":
            state_settings["border"] = {
                "color": self.border_color.getRgb() if hasattr(self, 'border_color') else (0,0,0,255),
                "thickness": self.border_thick.value(),
                "radius": self.border_radius.value()
            }
        elif style_type == "tint":
            state_settings["tint"] = {
                "color": self.tint_color.getRgb() if hasattr(self, 'tint_color') else (255,255,255,255),
                "intensity": self.tint_slider.value()/100.0
            }
        
        self.controller.update_state_style(self.current_state, state_settings)

    def apply_style_bg(self):
        state_settings = self.controller.styles[self.current_state].copy()
        state_settings["bg"] = self.bg_color.getRgb() if hasattr(self, 'bg_color') else None
        self.controller.update_state_style(self.current_state, state_settings)
