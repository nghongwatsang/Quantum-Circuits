from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300,300,400,400)
        self.setWindowTitle('Quantum Circuits')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Welcome to the Future')
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Classes')
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText('Here are your classes')

def clicked():
    print('clicked')       

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()