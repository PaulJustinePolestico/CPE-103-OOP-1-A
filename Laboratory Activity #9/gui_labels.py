import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit,QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__() #Initializes the main window like in the previous one
        #window = QMainWindow()
        self.title= "PyQt Line Edit"
        self.x= 200 #or left
        self.y= 200 #or top
        self.width=300
        self.height=300
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('person_public_17869.ico'))

        self.textboxlbl = QLabel("Hello World! ",self)
        self.textboxlbl.move(110,50)

        self.textboxlbl2 = QLabel("This program is written in Pycharm",self)
        self.textboxlbl2.move(60,60)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


