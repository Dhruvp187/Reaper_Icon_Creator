from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QGroupBox, QCheckBox, QHBoxLayout

class ControlPanel(QWidget):
    def __init__(self, controller):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Actions Section
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout(action_group)
        self.import_btn = QPushButton("Import")
        self.undo_btn = QPushButton("Undo")
        self.redo_btn = QPushButton("Redo")
        action_layout.addWidget(self.import_btn)
        action_layout.addWidget(self.undo_btn)
        action_layout.addWidget(self.redo_btn)
        layout.addWidget(action_group)

        # Style Editor
        from src.style_editor import StyleEditor
        style_group = QGroupBox("Style & Color")
        style_layout = QVBoxLayout(style_group)
        self.style_editor = StyleEditor(controller)
        style_layout.addWidget(self.style_editor)
        layout.addWidget(style_group)
        
        # Resize Section
        resize_group = QGroupBox("Dimensions")
        resize_layout = QVBoxLayout(resize_group)
        
        dims_row = QHBoxLayout()
        width_group = QGroupBox("Width")
        width_layout = QVBoxLayout(width_group)
        self.w_in = QLineEdit()
        width_layout.addWidget(self.w_in)
        dims_row.addWidget(width_group)
        
        height_group = QGroupBox("Height")
        height_layout = QVBoxLayout(height_group)
        self.h_in = QLineEdit()
        height_layout.addWidget(self.h_in)
        dims_row.addWidget(height_group)
        
        resize_layout.addLayout(dims_row)
        self.resize_btn = QPushButton("Resize / Refresh")
        resize_layout.addWidget(self.resize_btn)
        layout.addWidget(resize_group)
        
        # Filename Section
        filename_group = QGroupBox("Filename")
        filename_layout = QVBoxLayout(filename_group)
        self.name_in = QLineEdit("icon_strip")
        filename_layout.addWidget(self.name_in)
        layout.addWidget(filename_group)
        
        # Export Options
        export_group = QGroupBox("Export Scale")
        export_layout = QVBoxLayout(export_group)
        self.check_100 = QCheckBox("100% Icon")
        self.check_150 = QCheckBox("150% Icon")
        self.check_200 = QCheckBox("200% Icon")
        self.export_btn = QPushButton("Export Selection")
        
        export_layout.addWidget(self.check_100)
        export_layout.addWidget(self.check_150)
        export_layout.addWidget(self.check_200)
        export_layout.addWidget(self.export_btn)
        layout.addWidget(export_group)

        layout.addStretch()
