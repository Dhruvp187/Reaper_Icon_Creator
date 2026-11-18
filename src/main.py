import sys
import os
import copy

# Add the project root to sys.path so 'src' can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication, QFileDialog
from PIL import Image, ImageDraw, ImageEnhance, ImageChops
from src.ui import AppUI

class SimpleIconCreator:
    def __init__(self):
        self.raw_image = None
        self.processed_image = None
        self.styles = {
            "default": {"bg": None, "border": None, "tint": None},
            "hover": {"bg": None, "border": None, "tint": None},
            "active": {"bg": None, "border": None, "tint": None}
        }
        
        # Undo/Redo stacks
        self.undo_stack = []
        self.redo_stack = []
        
        self.ui = AppUI(self)
        
        self.ui.toolbar.import_btn.clicked.connect(self.import_image)
        self.ui.toolbar.undo_btn.clicked.connect(self.undo)
        self.ui.toolbar.redo_btn.clicked.connect(self.redo)
        self.ui.controls.resize_btn.clicked.connect(self.resize_image)
        self.ui.controls.export_btn.clicked.connect(self.export_strip)

    def save_state(self):
        self.undo_stack.append(copy.deepcopy(self.styles))
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(copy.deepcopy(self.styles))
            self.styles = self.undo_stack.pop()
            self.update_processed_image()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(copy.deepcopy(self.styles))
            self.styles = self.redo_stack.pop()
            self.update_processed_image()

    def update_state_style(self, state, settings):
        self.save_state()
        self.styles[state] = settings
        self.update_processed_image()

    def import_image(self):
        path, _ = QFileDialog.getOpenFileName(self.ui, "Open_Image")
        if path:
            self.raw_image = Image.open(path).convert("RGBA")
            self.ui.controls.w_in.setText(str(self.raw_image.width))
            self.ui.controls.h_in.setText(str(self.raw_image.height))
            self.update_processed_image(reset_zoom=True)

    def process_state(self, img, style):
        # Tint
        tint = style.get("tint")
        if tint and tint.get("intensity", 0) > 0:
            r, g, b, _ = tint["color"]
            intensity = tint["intensity"]
            tint_layer = Image.new("RGBA", img.size, (r, g, b, 255))
            alpha = img.getchannel('A')
            tinted = Image.composite(tint_layer, img, alpha)
            img = Image.blend(img, tinted, intensity)
        
        # Background
        if style.get("bg"):
            bg = Image.new("RGBA", img.size, style["bg"])
            img = Image.alpha_composite(bg, img)
        
        # Border
        border = style.get("border")
        if border and border["thickness"] > 0:
            scale = min(img.width, img.height) / 100.0
            thickness = max(1, int(border["thickness"] * scale))
            radius = int(border["radius"] * scale)
            draw = ImageDraw.Draw(img)
            draw.rounded_rectangle([0, 0, img.width-1, img.height-1], radius=radius, outline=border["color"], width=thickness)
        return img

    def update_processed_image(self, reset_zoom=False):
        if not self.raw_image:
            return
        
        try:
            w, h = int(self.ui.controls.w_in.text()), int(self.ui.controls.h_in.text())
            resized = self.raw_image.resize((w, h), Image.Resampling.LANCZOS)
            
            strip = Image.new("RGBA", (w * 3, h), (0, 0, 0, 0))
            strip.paste(self.process_state(resized.copy(), self.styles["default"]), (0, 0))
            strip.paste(self.process_state(resized.copy(), self.styles["hover"]), (w, 0))
            strip.paste(self.process_state(resized.copy(), self.styles["active"]), (w * 2, 0))
            
            self.processed_image = strip
            self.ui.preview_area.set_image(self.processed_image, reset_zoom=reset_zoom)
        except ValueError:
            pass

    def resize_image(self):
        if self.raw_image:
            self.update_processed_image()

    def export_strip(self):
        if not self.processed_image:
            return

        folder = QFileDialog.getExistingDirectory(self.ui, "Select Export Folder")
        if not folder:
            return

        filename = self.ui.controls.name_in.text() or "icon_strip"
        
        scales = []
        if self.ui.controls.check_100.isChecked(): scales.append(1.0)
        if self.ui.controls.check_150.isChecked(): scales.append(1.5)
        if self.ui.controls.check_200.isChecked(): scales.append(2.0)

        for scale in scales:
            s_w = int(self.processed_image.width * scale)
            s_h = int(self.processed_image.height * scale)
            scaled_img = self.processed_image.resize((s_w, s_h), Image.Resampling.LANCZOS)
            suffix = f"_{int(scale*100)}" if scale != 1.0 else ""
            scaled_img.save(f"{folder}/{filename}{suffix}.png")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = SimpleIconCreator()
    controller.ui.show()
    sys.exit(app.exec())
