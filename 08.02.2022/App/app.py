import sys
from tkinter import CENTER, LEFT, RIGHT
import PySide6
if 'PySide6' in sys.modules:
    print('PySide6')
    from PySide6 import QtGui, QtWidgets
    from PySide6.QtWidgets import *

if 'PyQt5' in sys.modules:
    print('PyQt5')
    from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("PyQT App")
win.setGeometry(100,100,280,90)

layH = QHBoxLayout()
layH.addWidget(QPushButton(LEFT))
layH.addWidget(QPushButton(CENTER))
layH.addWidget(QPushButton(RIGHT))
win.setLayout(layH)

lib1 = QLabel("<h1>Q World</h>", parent=win)
lib1.move(50,10)
win.show()
sys.exit( app.exec_() )