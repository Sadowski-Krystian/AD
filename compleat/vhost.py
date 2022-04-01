from os import *
import os
import re
import tarfile
from tkinter import * 
from re import *
from zipfile import *
import zipfile
from tarfile import *
from configparser import ConfigParser
from tkinter import ttk
from tkinter import filedialog



win = Tk()
win.title("Apache Vhost Manager")
win.geometry("800x500")
asd = Frame(win , width=300)
body = Frame(win)
tc = ttk.Notebook(body)
tab1 = ttk.Frame(tc)
tab2 = ttk.Frame(tc)
tc.add(tab1, text="Konfiguracja")
tc.add(tab2, text="Zawartość Pliku")
tc.pack(expand=1, fill="both")
box = Frame(tab1)
entVHname = Entry(box)
boxIpPort = Frame(box)
entSrvIp = Entry(boxIpPort,width=15)
entSrvPort = Entry(boxIpPort,width=4)
entDomain = Entry(box)
entAdmEmail = Entry(box)
boxDocDir = Frame(box)
entDocsDir = Entry(boxDocDir, width=32)
entErrLogDir = Entry(box, width=32)
entCmpLogDir = Entry(box, width=32)
entDoc2Dir = Entry(box, width=32)
# TabFrame2 - Raw Content File
boxTxa = Frame(tab2)
txa = Text(boxTxa,wrap="none")#, height=16
txa.insert( '1.0', "Przykładowa zawartość")
scbTxaY = Scrollbar(boxTxa,orient='vertical',command=txa.yview)
scbTxaX = Scrollbar(boxTxa,orient='horizontal',command=txa.xview)
txa['xscrollcommand'] = scbTxaX.set
txa['yscrollcommand'] = scbTxaY.set
scbTxaX.pack(side=BOTTOM,fill=X)
scbTxaY.pack(side=RIGHT,fill=Y)
txa.pack(side=LEFT,fill=X)




patterns = ('<VirtualHost ','DocumentRoot ','ServerAdmin ','ServerName ',
            'ErrorLog ','CustomLog ','<Directory ')
cmds = {'vtHost':{'ent':["split",":",entSrvIp,entSrvPort]},
        'docRot':{'ent':entDocsDir},
        'srvAdm':{'ent':entAdmEmail},
        'srvNam':{'ent':entDomain},
        'errLog':{'ent':entErrLogDir},
        'cstLog':{'ent':entCmpLogDir},
        'dir':{'ent':entDoc2Dir}}
#radios = {"TAR": "tar", "ZIP": "zip"}
#archNameZip = "zipArch.zip"
#archNameTar = "tarArch.tar"
cmdKeys = list(cmds.keys())
fileToOpen = None
startText = ""
lsb = None
dirName = ""
lstVh =[]

def listVhosts(dirName=vHostDir):
    lst = [ent for ent in os.listdir(dirName)
            if ent.endswith(".conf") and not ent.endswith("~")]
    lst.sort(reverse=False)
    return lst

def setVhostList(lstVh):
    if(type(lsb)!=None):
        lsb.delete(0, END)
    lstVhost = StringVar(value=lstVh)
    lsb["listvariable"] = lstVhost

def setStatus(event):
    statText="Naciśnięto przycisk q"
    status["text"] = statText

def pickFile(event):
    fileToOpen = lsb.get(lsb.curselection())
    entVHname.delete(0, END)
    entVHname.insert(0, fileToOpen)
    status["text"] = "Wyprano plik: "+fileToOpen
    read(fileToOpen)

def openFile():
    status["text"] = "Otwieranie pliku"
    filename = filedialog.askopenfilename(initialdir="/", title="Wybierz plik")

def browseVhostDir():
    status["text"] = "kliknięto zmień katalog plików VHosts"
    dirName = filedialog.askdirectory()
    global vHostDir
    vHostDir = dirName
    lstVh = listVhosts(dirName)
    setVhostList(lstVh)


def browseDir(btn):
    print(btn)
    status["text"] = "kliknięto Przeglądaj"
    dirName = filedialog.askdirectory()
    entF5 = None
    if( btn=="docsDir" ):
        entF5 = entDocsDir
    if( btn=="errLogDir" ):
        entF5 = entErrLogDir
    if( btn=="cmpLogDir" ):
        entF5 = entCmpLogDir
    if( btn=="doc2Dir" ):
        entF5 = entDoc2Dir
    entF5.delete(0, END)
    entF5.insert(0, dirName)
def quitApp(event):
    win.quit()



def read(fileToOpen):
    #s1 = input1.get()
    txa.delete(1.0, "end")
    pathFile=vHostDir+"/"+fileToOpen#  print(pathFile)
    with open(pathFile, "r") as reader:
        row=0
        content = reader.readlines()
        for line in content:
            lineCont = content[row]
            ic = 0
            for pattern in patterns:            
                if( '#' not in lineCont and pattern in lineCont):
                    ic = patterns.index(pattern)
                    onlyCont = parseLine( ic, lineCont )
                    # MV to FN(): add content to Textarea
                    if 'ent' in cmds[cmdKeys[ic]] and cmds[cmdKeys[ic]]['ent']!=None:
                    #   print("Próba dodania treści do "+ str(cmds[cmdKeys[ic]]) )
                        ent = cmds[cmdKeys[ic]]['ent']  #print(type(ent))
                        if( type(ent)!=list ):
                            ent.delete(0, END)
                            ent.insert(0, onlyCont)
                        else:
                            if(ent[0]=="split"):
                            #   print("split")
                                cmdCnt = 2
                                sign = ent[1]
                                oc = onlyCont.split(sign)
                                for x in range(cmdCnt,len(ent)):
                                    ent[x].delete(0, END)
                                    ent[x].insert(0, oc[x-cmdCnt])
                    #print(str(ic)+' '+lineCont) print(cmdKeys[ic])
            txa.insert(str(row+1)+'.0',lineCont)
            row+=1
    
def parseLine( ic, line ):
    pt = "^( |\t)*("+patterns[ic]+"){1}([\S\d:*\"][^>]+)(>)*"
    m = re.match(pt,line)   #print("PTRN="+pt)  print(m)
    return m.group(3).rstrip("\r\n")

def save():
    #s1 = input.get()
    #s2 = input2.get(1.0, END)
    #input2["state"]='disable'
    #print(s1)
    #print(s2)
    with open(s1, "w") as writer:
        writer.write(s2)
    #input2["state"]='normal'

def lock():
    print("lock")
    #if(input2["state"] == 'normal'):
        #input2["state"] = 'disable'
        #input2['background'] = "gray"
    #else:
        #input2["state"] = 'normal'
        #input2['background'] = "white"


import toolbar
lstVh = listVhosts()
tools = toolbar.build(win,browseVhostDir,read,save,lock, vHostDir,lstVh)

status = Label(win,text="AVM ver. 10")
status.pack(side=BOTTOM, expand=False)
asd.pack(side=LEFT,expand=True,fill=BOTH)
body.pack(expand=True,fill=BOTH)


mainloop()