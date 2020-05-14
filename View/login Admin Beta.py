import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class AdminLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Admin Login')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel ('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please Enter Your Admin Username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username,0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please Enter Your Password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')

        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()

        if self.lineEdit_username.text() == 'raven' and self.lineEdit_password.text() == '121':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = AdminLogin()
    form.show()

    sys.exit(app.exec())
