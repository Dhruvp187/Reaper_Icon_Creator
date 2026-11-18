from PySide6.QtWidgets import QScrollArea, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap

class PreviewArea(QScrollArea):
    def __init__(self):
        super().__init__()
        self.preview_label = QLabel("Import_an_image_to_start")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setMinimumSize(400, 400)
        self.preview_label.setStyleSheet("border: 1px solid gray;")
        
        self.setWidget(self.preview_label)
        self.setWidgetResizable(True)
        
        self.zoom_factor = 1.0
        self.master_image = None

    def set_image(self, pil_img, reset_zoom=False):
        self.master_image = pil_img
        if reset_zoom:
            self.zoom_factor = 1.0
        self.update_display()

    def update_display(self):
        if not self.master_image:
            return
            
        qimg = QImage(self.master_image.tobytes("raw", "RGBA"), 
                      self.master_image.width, 
                      self.master_image.height, 
                      QImage.Format_RGBA8888)
        
        pixmap = QPixmap.fromImage(qimg)
        scaled_size = pixmap.size() * self.zoom_factor
        self.preview_label.setPixmap(pixmap.scaled(scaled_size, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.preview_label.setToolTip("Default | Hover | Active")

    def wheelEvent(self, event):
        if self.master_image:
            if event.angleDelta().y() > 0:
                self.zoom_factor *= 1.1
            else:
                self.zoom_factor /= 1.1
            self.update_display()
        else:
            super().wheelEvent(event)
