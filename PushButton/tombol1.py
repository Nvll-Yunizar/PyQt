#!/usr/bin/python3
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
GPIO.setmode(GPIO.BOARD)
li = 40
l2 = 12
l3 = 11
l4 = 13


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("LAMP 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("LAMP 2", self)
        btn2.move(150, 50)

        btn3 = QPushButton("LAMP 3", self)
        btn3.move(30, 100)

        btn4 = QPushButton("LAMP 4", self)
        btn4.move(150, 100)

      
        btn1.clicked.connect(self.buttonClicked1)            
        btn2.clicked.connect(self.buttonClicked2)
        btn3.clicked.connect(self.buttonClicked3)
        btn4.clicked.connect(self.buttonClicked4)
        
        
        self.statusBar()
        
        self.setGeometry(400, 300, 300, 200)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked1(self):
        GPIO.setup(li,GPIO.OUT)
        sender = self.sender()
        if  (GPIO.input(li) == False) :
        	GPIO.output(li,True)
        	self.statusBar().showMessage(sender.text() + ' ON')
        else :
         GPIO.output(li,False)
         self.statusBar().showMessage(sender.text() + ' OFF')
        
    def buttonClicked2(self):
        GPIO.setup(l2,GPIO.OUT)
        sender = self.sender()
        if  (GPIO.input(l2) == False) :
        	GPIO.output(l2,True)
        	self.statusBar().showMessage(sender.text() + ' ON')
        else :
         GPIO.output(l2,False)
         self.statusBar().showMessage(sender.text() + ' OFF')
        
    def buttonClicked3(self):
        GPIO.setup(l3, GPIO.OUT)
        sender = self.sender()
        if  (GPIO.input(l3) == False) :
        	GPIO.output(l3,True)
        	self.statusBar().showMessage(sender.text() + ' ON')
        else :
         GPIO.output(l3,False)
         self.statusBar().showMessage(sender.text() + ' OFF')

    def buttonClicked4(self):
        GPIO.setup(l4, GPIO.OUT)
        sender = self.sender()
        if  (GPIO.input(l4) == False) :
        	GPIO.output(l4,True)
        	self.statusBar().showMessage(sender.text() + ' ON')
        else :
         GPIO.output(l4,False)     
         self.statusBar().showMessage(sender.text() + ' OFF')



        
       # sender = self.sender()
       # self.statusBar().showMessage(sender.text() + ' was pressed')
		
		
		
	
		
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
