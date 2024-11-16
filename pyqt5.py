# $$$$$$$$$$$$$$$$$$$$Check Pyqt5 is install or not$$$$$$$$$$$$$$$$$$$$$
# try:
#     from PyQt5 import QtWidgets
#     print("Pyqt5 is installed !")
# except ImportError:
#     print("Pyqt5 is not installed !")


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the GUI components
        self.initUI()

    def initUI(self):
        # Create a vertical layout
        layout = QVBoxLayout()

        # Create a label
        self.label = QLabel('Hello, World!', self)
        layout.addWidget(self.label)

        # Create a button
        btn = QPushButton('Click me', self)
        btn.clicked.connect(self.on_click)  # Connect button click to the function
        layout.addWidget(btn)

        # Set the layout to the window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('PyQt5 Example')
        self.setGeometry(100, 100, 300, 200)

    def on_click(self):
        self.label.setText('Button Clicked!')  # Change label text on button click

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())




