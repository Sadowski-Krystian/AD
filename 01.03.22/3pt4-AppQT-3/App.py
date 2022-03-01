import sys
import PySide2

from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class App(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		grid = QGridLayout(self)

		sidebar = QWidget()
		list = QVBoxLayout()
		self.pc1 = QLabel("PC-1")
		pc2 = QLabel("PC-2")
		pc3 = QLabel("PC-3")
		pc4 = QLabel("PC-4")
		pc5 = QLabel("PC-5")
		list.addWidget( self.pc1 )
		list.addWidget( pc2 )
		list.addWidget( pc3 )
		list.addWidget( pc4 )
		list.addWidget( pc5 )
		sidebar.setLayout(list)

		

		toolbar = QWidget()
		tools = QHBoxLayout()
		btnStart = QPushButton("Start")
		btnShtdw = QPushButton("Shutdown")
		btnStdBy = QPushButton("Stand By")
		btnHbrt = QPushButton("Hibernate")
		btnStart.clicked.connect( self.handleClick )
		btnStart.released.connect( lambda : self.pc1.setText("Zwolniony") )
		btnShtdw.clicked.connect( self.appClose )

		tools.addWidget( btnStart )
		tools.addWidget( btnShtdw )
		tools.addWidget( btnStdBy )
		tools.addWidget( btnHbrt )
		toolbar.setLayout(tools)

		main = QWidget()
		body = QVBoxLayout()
		body.addWidget( QLabel("Tekst") )
		body.addWidget( QPushButton("Przycisk") )
		main.setLayout(body)

		grid.addWidget(toolbar, 0, 0, 1, 2)
		grid.addWidget(sidebar, 1, 0)
		grid.addWidget(main, 1,1)
		self.setLayout(grid)

	def handleClick(self):
		nadawca = self.sender()
		print(nadawca.text())
		lbl = self.pc1.text()
		self.pc1.setText(lbl+": "+nadawca.text())

	def appClose(self):
		self.close()

	def closeEvent(self, ev):
		resp = QMessageBox.question(self, "Komunikat", "Czy aby napewno zakończyć", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if resp == QMessageBox.Yes:
			ev.accept()
		else:
			ev.ignore()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	#win = QWidget()
	win = App()
	win.setWindowTitle("Room PC ctrl")
	win.setGeometry(2000,100,640,480)
	win.show()
	sys.exit( app.exec_() )












