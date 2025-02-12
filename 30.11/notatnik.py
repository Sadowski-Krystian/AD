from os import *
import os
import re
import tarfile
from tkinter import * 
from re import *
from zipfile import *
import zipfile
from tarfile import *
win = Tk()
win.geometry("320x480")

def save():
    s1 = input.get()
    s2 = input2.get(1.0, END)
    input2["state"]='disable'
    #print(s1)
    #print(s2)
    with open(s1, "w") as writer:
        writer.write(s2)
    input2["state"]='normal'

def lock():
    if(input2["state"] == 'normal'):
        input2["state"] = 'disable'
        input2['background'] = "gray"
    else:
        input2["state"] = 'normal'
        input2['background'] = "white"

patterns = ("<VirtualHost", "DocumentRoot", "ServerAdmin", "ServerName", "ErrorLog", "CustomLog", "<Directory")
cmds = {"vHost":"", "docRot":"", "srvAdm":"", "srvNam":"", "errLog":"", "cstLog":"", "dir":""}
radios = {"TAR": "tar", "ZIP": "zip"}
archNameZip = "zipArch.zip"
archNameTar = "tarArch.tar"
cmdKeys = list(cmds.keys())
def read():
    s1 = input.get()
    input2.delete(1.0, "end")
    with open(s1, 'r') as reader:
        row=0
        content = reader.readlines()
        for line in content:
            lineCont = content[row]
            ic = 0
            for pattern in patterns:
                if("#" not in lineCont and pattern in lineCont):
                    ic = patterns.index(pattern)
                    parseLine(ic, lineCont)
                    #print(cmdKeys[ic])
            input2.insert(str(row+1)+'.0',lineCont)
            row+=1
    
def parseLine(ic, line):
    pt = "^( |\t)*("+patterns[ic]+"){1}([\s\d:*\"][^>]+)(>)*"
    m =re.match(pt, line)
    if m is not None:
        print(m.group(3))


def zipIt():
    with zipfile.ZipFile(archNameZip, 'w') as tf:
        files = os.listdir('.')
        for file in files:
            if file!=archNameZip:
                tf.write(file)
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

v= StringVar(win, '1')
def pickArcMeth():
    global arcMeth
    arcMeth = v.get()

def archiveIt():
    if arcMeth=="tar":
        tarIt()
    if arcMeth=="zip":
        zipIt()

frame  = Frame(win)
scb = Scrollbar(frame, orient="vertical")
fileName = Label(win, text="text").pack()
input = Entry(win)
input.insert(0, "000-default.conf")
input.pack()
content = Label(frame, text="treść").pack()
input2 = Text(frame, height=12, yscrollcommand=scb.set)
input2.insert(1.0, "Przykładowa zawartość")

scb.pack(side=RIGHT, fill=Y)
scb.config(command=input2.yview)
input2.pack()

for (text, value) in radios.items():
    Radiobutton(win,text=text,variable=v, value=value, command=pickArcMeth).pack()
btn = Button(win, command=save, text="zapisz").pack()
btn = Button(win, command=read, text="Otwórz").pack()
btn = Button(win, command=archiveIt, text="Archwyizuj").pack()
btn = Button(win, command=unZip, text="Wypakuj").pack()
btnLock = Button(win, command=lock, text="Zablokuj/Odblokij").pack()
frame.pack()
mainloop()