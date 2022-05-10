import os
import sys
import warnings
import configparser
import asyncio
import socket
import websockets
import PySide2

from NetUtl import NetUtl
from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class Client (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        toolbar = QWidget()
        