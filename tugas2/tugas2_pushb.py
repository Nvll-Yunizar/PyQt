#!/usr/bin/python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


switch_pin = 18
led_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setwarnings(False)

led_state = False
old_input_state = True

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setupUi()

    def setupUi(self):
        self.resize(900, 900)
        self.move(300, 300)
        self.setWindowTitle('Tugas 2 Lamp Button')

        self.label2 = QLabel()
        self.label2.setText('<img src="lampmati.jpg">')

        layout = QVBoxLayout()
        layout.addWidget(self.label2)
        self.setLayout(layout)

    def buttonPressed(self)
        while True:
            new_input_state = GPIO.input(switch_pin)
            if new_input_state == False and old_input_state == True:
                led_state = not led_state
            old_input_state = new_input_state
            GPIO.output(led_pin, led_state)



if __name__ == '__main__':
    a = QApplication(sys.argv)
    
    form = MainForm()
    form.show()

    

    a.exec_()
