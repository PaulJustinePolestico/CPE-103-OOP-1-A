import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Simple Registration Form"
        self.x = 200
        self.y = 200
        self.width = 450
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('person_public_17869.ico'))

        # Create textboxes
        self.textbox = QLineEdit(self)
        self.textbox.move(150, 90)
        self.textbox.resize(200, 30)
        self.textbox.setPlaceholderText("Enter Your First Name")

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 140)
        self.textbox2.resize(200, 30)
        self.textbox2.setPlaceholderText("Enter Your Last Name")

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(150, 195)
        self.textbox3.resize(200, 30)
        self.textbox3.setPlaceholderText("Enter Your Username")

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(150, 245)
        self.textbox4.resize(200, 30)
        self.textbox4.setEchoMode(QLineEdit.Password)  # Set for password field to hide input
        self.textbox4.setPlaceholderText("Enter Your Password")

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(150, 295)
        self.textbox5.resize(200, 30)
        self.textbox5.setPlaceholderText("Enter Your Email Address")

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 345)
        self.textbox6.resize(200, 30)
        self.textbox6.setPlaceholderText("Enter Your Contact Number")

        # Create labels
        self.textboxlbl = QLabel("First Name: ", self)
        self.textboxlbl.move(25, 100)

        self.textboxlbl2 = QLabel("Last Name: ", self)
        self.textboxlbl2.move(25, 150)

        self.textboxlbl3 = QLabel("Username: ", self)
        self.textboxlbl3.move(25, 200)

        self.textboxlbl4 = QLabel("Password: ", self)
        self.textboxlbl4.move(25, 250)

        self.textboxlbl5 = QLabel("Email Address: ", self)
        self.textboxlbl5.move(25, 300)

        self.textboxlbl6 = QLabel("Contact Number: ", self)
        self.textboxlbl6.move(25, 350)

        # Submit Button
        self.button = QPushButton("Submit", self)
        self.button.setToolTip("Submit your registration.")
        self.button.move(150, 400)
        self.button.clicked.connect(self.submit_form)  # Connect Submit button to function

        # Clear Button
        self.button2 = QPushButton("Clear", self)
        self.button2.setToolTip("Clear your registration.")
        self.button2.move(300, 400)
        self.button2.clicked.connect(self.clear_form)  # Connect Clear button to function

        self.show()

    def submit_form(self):
        # Collect data from all the text fields
        first_name = self.textbox.text()
        last_name = self.textbox2.text()
        username = self.textbox3.text()
        password = self.textbox4.text()
        email = self.textbox5.text()
        contact = self.textbox6.text()

        # Show message box with confirmation
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Registration Confirmation")
        msg.setText(f"Thank you for your registration, {first_name}!")
        msg.setInformativeText(f"Details submitted:\n\n"
                               f"Username: {username}\n"
                               f"Email: {email}\n"
                               f"Contact: {contact}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def clear_form(self):
        # Clear all the text fields
        self.textbox.clear()
        self.textbox2.clear()
        self.textbox3.clear()
        self.textbox4.clear()
        self.textbox5.clear()
        self.textbox6.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
