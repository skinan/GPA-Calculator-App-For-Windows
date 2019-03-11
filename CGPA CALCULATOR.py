import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QMessageBox
import json

import pictures2

# Application root location ↓
appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\"


class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        # Loading Main UI Design Files ↓
        uic.loadUi(appFolder + 'uicgpa.ui', self)

        # calling  main funtion
        self.sakib()

        # to show statusbar
        self.statusBar().showMessage("Fill up all 2 boxes."
                                     "Default per theory subject's credit is 3.00 and per lab subject's credit is 1.50")
        self.msg = QMessageBox()


    def sakib(self):
        self.pushButton.clicked.connect(self.buttonClick)
        self.pushButton_2.clicked.connect(self.clearbutton)


    def buttonClick(self):
        try:
            with open(appFolder + "sakib.json", "r") as file:
                cgpa = json.loads(file.read())

            mytext = self.lineEdit.text().upper()
            lab = self.lineEdit_2.text().upper()
            x = mytext.strip().split(',')
            z = lab.strip().split(',')

            sumo = 0
            for i in range(0, len(x)):
                y = float(cgpa[str(x[i])])
                sumo = float(sumo) + (y * float(3))

            suml = 0
            for i in range(0, len(z)):
                w = float(cgpa[str(z[i])])
                suml = float(suml) + (w * float(1.5))

            result = (sumo + suml)/((len(x) * 3) + (len(z) * 1.5))

            tmp = '{:.2f}'.format(result)
            self.label_5.setText(str(tmp))

        except:
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Error")
            self.msg.setInformativeText("Wrong Information!")
            self.msg.setWindowTitle("Error")
            self.msg.exec_()

    def clearbutton(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label_5.setText("0.00")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

