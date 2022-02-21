from os import *
import os
import re
import tarfile
from tkinter import * 
from re import *
from zipfile import *
import zipfile
from tarfile import *
dd = StringVar()
listVh = []
vHostsDir = None
archMode = None
DD_DEF = "Archiwizuj"
DD_FILE = "plik"
DD_DIR = "katalog"



def zipIt():
    global archMode
    global listVh
    archNameZip = "2022-01-04_202500.zip"
    with zipfile.ZipFile(archNameZip, 'w') as tf:
        if( archMode == DD_FILE):
            files = ["000-local.conf"]
        else:
            files = listVh
        for file in files:
            if file!=archNameZip:
                tf.write(vHostsDir+"/"+file)
        for fin in tf.namelist():
            print("Dodano %s" % fin)
        tf.close

def unZip():
    print("unzip")
    with zipfile.ZipFile(archNameZip, 'r') as uzi:
        for file in uzi.namelist():
            uzi.extract(file, "out")

def tarIt():
    with tarfile.open(archNameTar, 'w') as tf:
        files = os.listdir('.')
        for file in files:
            if file!=archNameTar:
                tf.add(file)
        for fin in tf.getnames():
            print("Dodano %s" % fin)
        tf.close

def unTar():
    print("unTar")
    with tarfile.open(archNameTar, 'r') as uzi:
        for file in uzi.getnames():
            uzi.extract(file, "out")

def archiveIt(event):
    global archMode
    archMode = event
    arcMeth = "zip"
    if arcMeth=="tar":
        tarIt()
    if arcMeth=="zip":
        zipIt()
    print("Wybrano archiwizacje do: "+arcMeth)
    dd.set(DD_DEF)

def build(win,browseVhostDir,read,save,lock,unlock,LvHostsDir,lstVh):
    global listVh
    global vHostsDir
    vHostsDir = LvHostsDir
    listVh = lstVh
    tools   = Frame(win)
    path    = Frame(win)
    tools.pack(fill=X)
    path.pack(fill=X)
    opts    = [DD_FILE,DD_DIR]
    dd.set( DD_DEF )
    drop    = OptionMenu(tools, dd, *opts, command=archiveIt )
    btnBrw  = Button(path,text="Zmień katalog", command=browseVhostDir)
    lblPath = Label(path,text="PATH: "+vHostsDir)
    btnWrt  = Button(tools,text="Zapisz",command=save)
    #btnRed = Button(tools,text="Otwórz",command=read)
    btnBrw.pack(side=LEFT)
    lblPath.pack(side=LEFT)
    drop.pack(side=LEFT)
    btnWrt.pack(side=LEFT)
    #btnRed.pack(side=LEFT)
    btnChk  = Button(tools,text="Walidacja")
    btnCnf  = Button(tools,text="Ustawienia")
    btnCnf.pack(side=RIGHT)
    btnChk.pack(side=RIGHT)
    return tools