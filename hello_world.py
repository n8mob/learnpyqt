import sys
from PyQt6.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle('Empty Window in PyQt6')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
