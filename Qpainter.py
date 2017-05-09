from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys

def main():  
    app = QtWidgets.QApplication(sys.argv)

    pixmap = QtGui.QPixmap (QtCore.QSize(400,400))    
    painter = QtGui.QPainter(pixmap)
    
    painter.fillRect ( QtCore.QRectF(0, 0, 400, 400),QtGui.QColor(241,15,218))
    painter.drawText ( QtCore.QRectF(0, 0, 400, 400),QtCore.Qt.AlignCenter,"This is an image created with QPainter!!")
    painter.end()    
    pixmap.save("output.jpg")
if __name__ == '__main__':
    main()
