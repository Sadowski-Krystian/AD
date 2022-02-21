import sys
import PySide6

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import(
    QWidget,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton
    
)

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle("PyQt Layout Manager")
win.setGeometry(100,100,280,390)

layW = QVBoxLayout()

tlb = QWidget()
lay = QHBoxLayout()
lay.addWidget(QPushButton("Left"))
lay.addWidget(QPushButton("Center"), 1)
lay.addWidget(QPushButton("Right"), 2)
tlb.setLayout(lay)

p = tlb.palette()
p.setColor(tlb.backgroundRole(), Qt.red)
tlb.setPalette(p)

lst = QWidget()

pal = win.palette()
pal.setColor(win.backgroundRole(), Qt.red)
lst.setAutoFillBackground(True)
lst.setPalette(pal)

layV = QVBoxLayout()

lbl1 = QLabel("<h1>Line2</h1>")#, parent=win)
lbl2 = QLabel("<h1>Line3</h1>")#, parent=win)
lbl3 = QLabel("<h1>LineIV</h1>")#, parent=win)
layV.addWidget(lbl1)
layV.addWidget(lbl2)
layV.addWidget(lbl3)
lst.setLayout(layV)


layW.addWidget(tlb)
layW.addWidget(lst)
win.setLayout(layW)

win.show()
sys.exit(app.exec())