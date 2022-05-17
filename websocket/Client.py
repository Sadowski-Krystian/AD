import imp
import os
import sys
import warnings
import configparser
import asyncio
import socket
from NetUtl import NetUtl
import websockets
import PySide2

from PySide2 import QtGui, QtWidgets
from PySide2 import Qt
from PySide2.QtWidgets import *

class Client(QWidget):
    def __init__(self,parent=None):
        QtWidget.__init__(self, parent)
        toolbar = QtWidget()
        hTopBar = QHBoxLayout()
        btnChat = QPushButton('chat')
        btnSett = QPushButton('sett')
        btnChat.clicked.connect(lambda: self.changeTab("chat"))
        btnSett.clicked.connect(lambda: self.changeTab("sett"))
        hTopBar.addWidget(btnChat)
        hTopBar.addWidget(btnSett)
        toolbar.addWidget(hTopbar)

        self.chatTab = QtWidget()
        self.chatTab.setVisible(False)
        chat = QVBoxLayout()
        self.msgEntry = QLineEdit()
        self.sendBtn = QPushButton("Send")
        self.sendBtn.clicked.connect(self.sendMsg)
        chat.addWidget(self.msgEntry)
        chat.addWidget(self.sendBtn)
        self.chatTab.setLayout(chat)

        self.settTab = QtWidget()
        self.settTab.setVisible(False)
        info = QVBoxLayout()
        net = NetUtl()
        self.conf = {}
        self.conf['host'] = socket.gethostname()
        hostOs = os.uname()[1]
        self.hostname = QLabel("Hostname: " + self.conf['host'] + hostOs)
        info.addWidget(self.hostname)
        self.conf['ip'] = net.getIp()

        def connToserver(self):
            self.readSettings()
            print(self.srvAddr)
            loop = asyncio.asyncio.get_event_loop()
            loop.run_util_complete(self.sendMsg())

        def getMessage(self):
            self.smg = self.msgEntry.text()
            print(self.msg)
            self.msgEntry.clear()
        
        async def sendMsg(self):
            async with websockets.connect("ws://" + self.srvAddrs) as websocket:
                await websocket.send(self.msgEntry.text())
                await websocket.recv()

        def changeTab(self, bttn):
            print(bttn)
            if bttn == 'chat':
                self.connToServer()
                self.chatTab.setVisible(True)
            if bttn == 'sett':
                self.settTab.setVisible(True)

        def storeSettings(self):
            self.cnf = configparser.ConfigParser()
            self.cnf['DEFAULT'] = {
                'hostname':self.conf['host'],
                'ip4addr':self.conf['ip'],
                'username':self.conf['user'],
                'student':self.studentEntry.text()

            }
            self.cnf['SERVER'] = {
                'ip4addr':'192.168.88.129',
                'port':8765
            }
            self.gatherDataToSave()
            with open('client.ini', 'w') as confFile:
                self.cnf.write(confFile)

            def gatherDataToSave(self):
                self.cnf['DEFAULT']['student'] = self.studentEntry.text()
            
            def readSetting(self):
                self.conn = configparser
                self.conn.read('client.ini')
                self.cnf.sections()
                self.srvAddr = self.confp['SERVER']['ip4addr'] + self.cnf['SERVER']['port']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Client()
    win.setWindowTitle("Classroom Client")
    win.setGeometry(600, 0,400,800)
    win.show()
    sys.exit(app.exec_())