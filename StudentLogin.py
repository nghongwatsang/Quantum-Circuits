import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self)._init()
        loadUi("Login.ui", self)
        self.enterButton.clicked.connect(self.loginfunction)
    
    def loginfuntion(self):
        code = self.code.text()
        name = self.code.text()
        print("Successfully logged in with", code, 'Welcome to Quantum Circuits', name)

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.show()
app.exec_()  