import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

DEFAULT_HEIGHT = 800

DEFAULT_WIDTH = 1200


class HelloWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(200, 100, DEFAULT_WIDTH, DEFAULT_HEIGHT)
        self.setWindowTitle('Labels')
        self.add_labels()
        self.show()

    def add_labels(self):
        hello_label = QLabel(self)
        hello_label.setText('Hello, Qt!')
        hello_label.move(105, 15)

        try:
            image_path = '/Users/ngrigg/Desktop/img/garthHacking.png'
            with open(image_path):
                image_label = QLabel(self)
                pixmap = QPixmap(image_path).scaled(DEFAULT_WIDTH, DEFAULT_HEIGHT, Qt.AspectRatioMode.KeepAspectRatio)
                image_label.setPixmap(pixmap)
                image_label.move(25, 40)
        except FileNotFoundError as ferror:
            print(f'Image not found.\n{ferror}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWindow()
    sys.exit(app.exec())
