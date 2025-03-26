import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from registration import App


if __name__ == "__main__":
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())