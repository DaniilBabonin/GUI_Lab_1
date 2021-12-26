from PyQt5.QtWidgets import *
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.lbl = QLabel(self)
        self.lbl.setText("Hellow, world!")
        self.lbl.move(90, 30)

        self.btn1 = QPushButton("Translate", self)
        self.btn1.move(90, 80)
        self.btn1.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(300, 300, 250, 150)
        self.show()


    def buttonClicked(self):
        self.lbl.setText("Привет, мир!")
        self.lbl.move(90, 30)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())