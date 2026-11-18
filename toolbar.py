from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class Toolbar(QWidget):
    def __init__(self, controller):
        super().__init__()
        layout = QHBoxLayout(self)
        self.import_btn = QPushButton("Import")
        self.undo_btn = QPushButton("Undo")
        self.redo_btn = QPushButton("Redo")
        
        layout.addWidget(self.import_btn)
        layout.addWidget(self.undo_btn)
        layout.addWidget(self.redo_btn)
        layout.addStretch()
