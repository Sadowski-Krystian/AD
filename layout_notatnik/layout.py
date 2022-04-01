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
frameleft = Frame(win)
lstItemsArr = ('Nowy VHost', 'vhost-1', 'vhost-2', 'vhost-a', 'vhost-b', 'vhost-c')
lstItems = StringVar(value=lstItemsArr)
scbl = Scrollbar(frameleft, orient="vertical")
lsb = Listbox(frameleft, listvariable=lstItems, selectmode="browse", yscrollcommand=scbl.set)
lsb.pack(side=LEFT)
scbl.pack(side=LEFT, fill=Y)
frame  = Frame(win)


input = Entry(frame)
input.insert(0, "000-default.conf")
input.grid(row=1, column=2)
Label(frame, text="Nazwa").grid(row=1, column=1)
Entry(frame).grid(row=2, column=2)
Label(frame, text="Adres IP : numer Portu").grid(row=2, column=1)
Entry(frame).grid(row=3, column=2)
Label(frame, text="Nazwa serwera (domena)").grid(row=3, column=1)
Entry(frame).grid(row=4, column=2)
Label(frame, text="Adres e-mail administratora").grid(row=4, column=1)
Entry(frame).grid(row=5, column=2)
Label(frame, text="Ścieżka dokumentów").grid(row=5, column=1)
Button(frame, text='przeglądaj').grid(row=5, column="3")
Entry(frame).grid(row=6, column=2)
Label(frame, text="Ścieżka do dziennika błędów").grid(row=6, column=1)
Button(frame, text='przeglądaj').grid(row=6, column="3")
Entry(frame).grid(row=7, column=2)
Label(frame, text="Ścieżka do dziennika ogólnego").grid(row=7, column=1)
Button(frame, text='przeglądaj').grid(row=7, column="3")
Entry(frame).grid(row=8, column=2)
Label(frame, text="Ścieżka dokumentów").grid(row=8, column=1)
Button(frame, text='przeglądaj').grid(row=8, column="3")

mainFrame = Frame(frame)
scb = Scrollbar(mainFrame, orient="vertical")
input2 = Text(mainFrame, height=12, yscrollcommand=scb.set)
input2.insert(1.0, "Przykładowa zawartość")


scb.config(command=input2.yview)
input2.pack(side=LEFT)
scb.pack(side=RIGHT, fill=Y)
mainFrame.grid(row=9, columnspan=4)



formatFrame = Frame(frame)
for (text, value) in radios.items():
    Radiobutton(formatFrame,text=text,variable=v, value=value, command=pickArcMeth).pack()

formatFrame.grid(row=10, column=2)
btn = Button(frame, command=save, text="zapisz").grid(row=11, column=2)
btn = Button(frame, command=read, text="Otwórz").grid(row=12, column=2)
btn = Button(frame, command=archiveIt, text="Archwyizuj").grid(row=13, column=2)
btn = Button(frame, command=unZip, text="Wypakuj").grid(row=14, column=2)
btnLock = Button(frame, command=lock, text="Zablokuj/Odblokij").grid(row=15, column=2)
frameleft.grid(row=1, column=1)
frame.grid(row=1, column=2)
mainloop()