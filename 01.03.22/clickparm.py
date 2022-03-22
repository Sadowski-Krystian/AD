import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot
def mojaFunkcja(mamArgument):
    print("Kliknięto mnie!")
    print(mamArgument)
class Sygnalista(QObject):
    sygnalek = Signal(str)
app = QApplication(sys.argv)
btn = QPushButton("Kliknij mnie")
syg = Sygnalista()
syg.sygnalek.connect(mojaFunkcja)
syg.sygnalek.emit("Bo TAK!")
btn.show()
sys.exit(app.exec_())