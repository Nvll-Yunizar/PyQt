import RPi.GPIO as GPIO
import time
from PyQt5.QtWidgets import *
import sys

switch_pin = 18
led_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

led_state = False
old_input_state = True
counter = 0;


class ShowText(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
		
		sender = self.sender()

	def initUI(self):
		self.statusBar()
		
		self.setGeometry(400, 300, 300, 200)	
		self.setWindowTitle('Tombol')
		self.show()
	
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = ShowText()
	sys.exit(app.exec_())

	while True:
		new_input_state = GPIO.input(switch_pin)
		if new_input_state == False and old_input_state == True:
			led_state = not led_state
		old_input_state = new_input_state
		GPIO.output(led_pin, led_state)

		if led_state == True:
			counter+=1
	
		self.statusBar().showMessage(sender.text() + counter)
