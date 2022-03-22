import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import SIGNAL, QObject # stare podejście
def mojaFunkcja():
    print("Kliknięto mnie!")
    
app = QApplication(sys.argv)
btn = QPushButton("Kliknij mnie")
QObject.connect(btn, SIGNAL ('clicked()'), mojaFunkcja) # stare podejście
btn.clicked.connect(mojaFunkcja) # nowe podejście
btn.show()
sys.exit(app.exec_())