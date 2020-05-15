from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLineEdit,QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, QWidget, QDateEdit, QSpinBox, QDialog, QDialogButtonBox
from PyQt5 import QtCore
import sys
from PyQt5 import QtGui

class Mainmenu(QWidget):
    def __init__(self):
        super().__init__()

        Label = QLabel("Admin Main Menu")
        Label.setAlignment(QtCore.Qt.AlignCenter)
        submitbtn = QPushButton("Submit")


        title = "Admin Main Menu "
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "icon.png"


        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.MainM()
        self.show()

    def MainM(self):
        self.form = QFormLayout(self)

        self.submit = QPushButton(self)
        self.submit.setText("Insert New Book")
        self.submit.clicked.connect(self.submit_btn)
        self.form.addRow(self.submit,)

        self.submit = QPushButton(self)
        self.submit.setText("Weekly Income")
        self.submit.clicked.connect(self.submit_btn)
        self.form.addRow(self.submit,)

        self.submit = QPushButton(self)
        self.submit.setText("Monthly Income")
        self.submit.clicked.connect(self.submit_btn)
        self.form.addRow(self.submit,)

        self.submit = QPushButton(self)
        self.submit.setText("Show Book")
        self.submit.clicked.connect(self.submit_btn)
        self.form.addRow(self.submit,)


    def submit_btn(self):
        print("Book Name :  {}\nPrice : {}\nAmount : {}".
        format(self.nama.text(),
        self.noTel.text(),
        self.alamat.toPlainText(),
        self.jk.currentText(),
        self.Nik.text(),
        self.tglLahir.text()))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    inBook = Mainmenu()
    sys.exit(App.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = AdminLogin()
    form.show()

    sys.exit(app.exec())
