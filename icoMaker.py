import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog,
    QLineEdit, QCheckBox, QHBoxLayout, QMessageBox, QFrame
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from PIL import Image


class IcoMakerApp(QWidget):
    def __init__(self):
        super().__init__()

        # App settings
        self.setWindowTitle("icoMaker")
        self.setFixedSize(520, 460)
        self.setStyleSheet("background-color: #09000f; color: #ffffff;")

        # Font settings
        self.font = QFont("Roboto", 12)
        self.button_font = QFont("Roboto", 12, QFont.Weight.Bold)

        # File paths
        self.input_files = []
        self.output_folder = ""
        self.output_filename = ""

        # Sizes selection
        self.sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]
        self.size_checkboxes = []

        self.init_ui()

    def init_ui(self):
        """Builds the modern UI layout."""
        layout = QVBoxLayout()

        # Title
        title = QLabel("icoMaker")
        title.setFont(QFont("Roboto", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Divider
        layout.addWidget(self.create_divider())

        # Image Selection
        self.input_label = QLabel("No images selected")
        self.input_label.setFont(self.font)
        self.input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn_select_images = QPushButton("Choose Images")
        btn_select_images.setFont(self.button_font)
        btn_select_images.setStyleSheet(self.button_style())
        btn_select_images.clicked.connect(self.select_images)

        layout.addWidget(btn_select_images)
        layout.addWidget(self.input_label)

        # Divider
        layout.addWidget(self.create_divider())

        # Output Folder Selection
        self.output_label = QLabel("No output folder selected")
        self.output_label.setFont(self.font)
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn_select_output = QPushButton("Choose Output Folder")
        btn_select_output.setFont(self.button_font)
        btn_select_output.setStyleSheet(self.button_style())
        btn_select_output.clicked.connect(self.select_output_folder)

        layout.addWidget(btn_select_output)
        layout.addWidget(self.output_label)

        # Divider
        layout.addWidget(self.create_divider())

        # Output File Name
        self.filename_input = QLineEdit()
        self.filename_input.setFont(self.font)
        self.filename_input.setPlaceholderText("Enter output file name (optional)")
        self.filename_input.setStyleSheet("background-color: #6b4a5e; color: #ffffff; padding: 6px;")
        layout.addWidget(self.filename_input)

        # Divider
        layout.addWidget(self.create_divider())

        # Icon Sizes Selection
        size_label = QLabel("Select Icon Sizes:")
        size_label.setFont(self.font)
        layout.addWidget(size_label)

        size_layout = QHBoxLayout()
        for size in self.sizes:
            checkbox = QCheckBox(f"{size[0]}x{size[1]}")
            checkbox.setChecked(True)
            checkbox.setFont(self.font)
            checkbox.setStyleSheet("color: #ffffff;")
            size_layout.addWidget(checkbox)
            self.size_checkboxes.append(checkbox)

        layout.addLayout(size_layout)

        # Divider
        layout.addWidget(self.create_divider())

        # Convert Button
        btn_convert = QPushButton("Convert to .ICO")
        btn_convert.setFont(self.button_font)
        btn_convert.setStyleSheet(self.button_style())
        btn_convert.clicked.connect(self.convert_to_ico)
        layout.addWidget(btn_convert)

        self.setLayout(layout)

    def create_divider(self):
        """Creates a modern divider."""
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setStyleSheet("color: #6b4a5e;")
        return line

    def button_style(self):
        """Returns a consistent button style."""
        return """
        QPushButton {
            background-color: #6b4a5e;
            color: white;
            border-radius: 5px;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #8c6278;
        }
        QPushButton:pressed {
            background-color: #5a3a4c;
        }
        """

    def select_images(self):
        """Opens file dialog to select images."""
        files, _ = QFileDialog.getOpenFileNames(self, "Select Images", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.webp *.tiff)")
        if files:
            self.input_files = files
            self.input_label.setText(f"{len(files)} image(s) selected")

    def select_output_folder(self):
        """Opens folder dialog to select output folder."""
        folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder:
            self.output_folder = folder
            self.output_label.setText(f"Selected: {folder}")

    def convert_to_ico(self):
        """Converts selected images to ICO format."""
        if not self.input_files:
            QMessageBox.warning(self, "Error", "Please select image files.")
            return

        if not self.output_folder:
            QMessageBox.warning(self, "Error", "Please select an output folder.")
            return

        selected_sizes = [size for size, checkbox in zip(self.sizes, self.size_checkboxes) if checkbox.isChecked()]
        if not selected_sizes:
            QMessageBox.warning(self, "Error", "Please select at least one icon size.")
            return

        self.output_filename = self.filename_input.text().strip()

        for file in self.input_files:
            try:
                img = Image.open(file).convert("RGBA")
                output_file = os.path.join(
                    self.output_folder, 
                    f"{self.output_filename or os.path.splitext(os.path.basename(file))[0]}.ico"
                )
                img.save(output_file, format="ICO", sizes=selected_sizes)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {e}")

        QMessageBox.information(self, "Success", "All images converted successfully!")

if __name__ == "__main__":
    app = QApplication([])
    window = IcoMakerApp()
    window.show()
    app.exec()
