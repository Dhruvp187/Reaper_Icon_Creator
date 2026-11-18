from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox

class StateSelectionPanel(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        layout = QVBoxLayout(self)
        
        group = QGroupBox("Icon_States")
        btn_layout = QHBoxLayout()
        
        self.btn_default = QPushButton("Default")
        self.btn_hover = QPushButton("Hover")
        self.btn_active = QPushButton("Active")
        
        for btn in [self.btn_default, self.btn_hover, self.btn_active]:
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, b=btn: self.select_state(b))
            
        btn_layout.addWidget(self.btn_default)
        btn_layout.addWidget(self.btn_hover)
        btn_layout.addWidget(self.btn_active)
        
        group.setLayout(btn_layout)
        layout.addWidget(group)
        
    def select_state(self, selected_btn):
        for btn in [self.btn_default, self.btn_hover, self.btn_active]:
            if btn == selected_btn:
                btn.setStyleSheet("background-color: #d78300; color: white; border: 1px solid #ff9900;")
            else:
                btn.setStyleSheet("")
                btn.setChecked(False)
