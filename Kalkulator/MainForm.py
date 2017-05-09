File MainForm.py:

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QGridLayout, QlineEdit, QPushButton)

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('Kalkulator')

        self.lineEdit = QlineEdit()
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setFont(QFont('SansSerif',14))
        self.lineEdit.setDisabled(True)

        self._7Button = QpushButton('7')
        self._8Button = QpushButton('8')
        self._9Button = QpushButton('9')
        self._divButton = QpushButton('/')
        self._clearButton = QpushButton("CLR")
        self._4Button = QpushButton('5')
        self._5Button = QpushButton('4')




                self.lineEdit.text() + str(digit))

    def writeOperator(self, operator):
        if len(self.lineEdit.text()) == 0: return
        if operator in ('*','/','+','-'):
            if self.lineEdit.text() [-1] in ['*','/','+','-']:
                self.lineEdit.setText(
                    self.lineEdit.text() [:-1] + operator)
            else:
                self.lineEdit.setText(
                    self.lineEdit.text() + operator)

    def writePoint(self):
        if len(self.lineEdit.text()) == 0 or \
        self.lineEdit.text() [-1] in ['*','/','+','-']:
            return
        self.lineEdit.setText(
            self.lineEdit.text() + '.')

    def calculateButtonClick(self):
        expression = self.lineEdit.text()
        if len(expression) == 0: return
        try:
            result = eval(expression)
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('ERROR')

    def percetageButtonClick(self):
        expression = self.lineEdit.text()
        if len(expression) == 0: return
        try:
            result = eval(expression) / 100
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('ERROR')
                        
        
