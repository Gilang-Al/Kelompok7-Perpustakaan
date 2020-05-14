from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLineEdit,QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, QWidget, QDateEdit, QSpinBox, QDialog, QDialogButtonBox
from PyQt5 import QtCore
import sys
from PyQt5 import QtGui

class InputBook(QWidget):
    def __init__(self):
        super().__init__()

        Label = QLabel("Input Book")
        Label.setAlignment(QtCore.Qt.AlignCenter)
        submitbtn = QPushButton("Submit")


        title = "Librarian "
        left = 0
        right = 0
        width = 400
        height = 600
        iconName = "assets/img/icon.png"


        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, right, height, width)
        self.inputBook()
        self.show()

    def inputBook(self):
        self.form = QFormLayout(self)

        self.book = QLineEdit(self)
        self.book.setPlaceholderText("Book Name")
        self.form.addRow("Book Name", self.book)

        self.price = QLineEdit(self)
        self.price.setPlaceholderText("Price")
        self.form.addRow("Price", self.price)

        self.price = QLineEdit(self)
        self.price.setPlaceholderText("Author")
        self.form.addRow("Author", self.price)

        self.amount = QSpinBox(self)
        self.form.addRow("Amount", self.amount)

        self.submit = QPushButton(self)
        self.submit.setText("Add")
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
    inBook = InputBook()
    sys.exit(App.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = AdminLogin()
    form.show()

    sys.exit(app.exec())
