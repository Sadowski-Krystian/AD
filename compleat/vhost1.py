'''
Author:		Petri Grzegorz & Students
Date:		2022-01-04
Desc:		Apache's vhosts (sites configuration files) manager & editor tools [AHMET] lub [AVM] Apache Vhosts Manager
Version:	0.9.6
'''
appVersion = "0.9.6"
import os
from os.path import exists
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from configparser import ConfigParser
import re
# konfiguracja, której nie było - nie trzeba pisać
confFile = "vhost.conf.ini"
langFile = "vhost.lang.ini"

if( exists(confFile) ):
	conf = ConfigParser()
	conf.read(confFile)
	size = conf.get('window', 'size')
	vHostsDir = conf.get('main', 'vHostsDir')
	#ttl = conf.get('main', 'title')
	print(size)
else:
	print("No "+confFile+" file found")
# size = "800x500"
win = Tk()
win.title("Apache Vhost Manager")
win.geometry("800x500")

asd = Frame(win,width=300)#height=500,
# przeniesiono na dół #asd.pack(side=LEFT,expand=True,fill=BOTH)
body = Frame(win)
# przeniesiono na dół #body.pack(expand=True,fill=BOTH)

tc = ttk.Notebook(body)
tab1 = ttk.Frame(tc)
tab2 = ttk.Frame(tc)
tc.add(tab1, text="Konfiguracja")
tc.add(tab2, text="Zawartość pliku")
tc.pack(expand=1, fill="both")

# TabFrame1 - Configuration fields
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

##
# Zmienne globalne
##
patterns = ('<VirtualHost ','DocumentRoot ','ServerAdmin ','ServerName ',
			'ErrorLog ','CustomLog ','<Directory ')
cmds = {'vtHost':{'ent':["split",":",entSrvIp,entSrvPort]},
		'docRot':{'ent':entDocsDir},
		'srvAdm':{'ent':entAdmEmail},
		'srvNam':{'ent':entDomain},
		'errLog':{'ent':entErrLogDir},
		'cstLog':{'ent':entCmpLogDir},
		'dir':{'ent':entDoc2Dir}}
#struct = {'':None,'ctrl':None,'value':None}
cmdKeys = list(cmds.keys())
#radios = {"TAR":"tar","ZIP":"zip"}
#archNameZip = "zipArch.zip"
#archNameTar = "tarArch.tar"
fileToOpen = None
statText = ""
vHostsDir = "/"
lsb = None
dirName = ""
lstVh = []

##
# Funkcje do obsługi narzędzia
##
def listVhosts(dirName=vHostsDir):
	#return os.listdir(dirName)	print(dirName)
	lst = [ent for ent in os.listdir(dirName)
			if ent.endswith(".conf") and not ent.endswith("~")]
#	setVhostList(lst)
	lst.sort(reverse=False)	#	print(lst)
	return lst

def setVhostList(lstVh):
	if(type(lsb)!=None):
		lsb.delete(0,END)
	lstVhosts = StringVar(value=lstVh)
	lsb["listvariable"] = lstVhosts
	
def setStatus(event):
	statText="Naciśnięto przycisk Q"
	status["text"] = statText

def pickFile(event):
	fileToOpen = lsb.get(lsb.curselection())
	entVHname.delete(0, END)
	entVHname.insert(0, fileToOpen)
	status["text"] = "Wybrano plik: "+fileToOpen
	read(fileToOpen)

def openFile():
	status["text"] = "Otwieranie pliku" # TUPLE
	filename = filedialog.askopenfilename(initialdir="/", title="Wybierz plik", filetypes=[("pliki tekstowe","*.txt")] )

def browseVhostDir():
	status["text"] = "kliknięto Zmień katalog plików VHosts"
	dirName = filedialog.askdirectory()
	global vHostsDir
	vHostsDir = dirName
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
	
# TU była ARCHIWIZACJA

def read(fileToOpen):
	#s1 = input1.get()
	txa.delete(1.0, "end")
	pathFile=vHostsDir+"/"+fileToOpen#	print(pathFile)
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
					#	print("Próba dodania treści do "+ str(cmds[cmdKeys[ic]]) )
						ent = cmds[cmdKeys[ic]]['ent']	#print(type(ent))
						if( type(ent)!=list ):
							ent.delete(0, END)
							ent.insert(0, onlyCont)
						else:
							if(ent[0]=="split"):
							#	print("split")
								cmdCnt = 2
								sign = ent[1]
								oc = onlyCont.split(sign)
								for x in range(cmdCnt,len(ent)):
									ent[x].delete(0, END)
									ent[x].insert(0, oc[x-cmdCnt])
							
					#print(str(ic)+' '+lineCont) print(cmdKeys[ic])
			txa.insert(str(row+1)+'.0',lineCont)
			row+=1
	#	line = reader.readline()
	#	while line!='':
	#		txa.insert('1.0',line)
	#		line = reader.readline()

def parseLine( ic, line ):
	pt = "^( |\t)*("+patterns[ic]+"){1}([\S\d:*\"][^>]+)(>)*"
	m = re.match(pt,line)	#print("PTRN="+pt)	print(m)
	#if(m is not None):
#	print(m.group(3))
	return m.group(3).rstrip("\r\n")

def save():
	# odczyt danych z input1
	#s1 = input1.get()
	# odczyt danych z txa
	s2 = txa.get('1.0','end')
	txa['state'] = 'disabled'
	# zapis do pliku
	#with open(s1, "w") as writer:
		#writer.write(s2)
	#txa['state'] = 'normal'

def lock():
	txa['state'] = 'disabled'
	txa['bg'] = "#c3c6c5"
def unlock():
	txa['state'] = 'normal'
	txa['bg'] = "white"

##
# Budowa UI
##
import Toolbar1

lstVh = listVhosts()
tools = Toolbar1.build(win,browseVhostDir,read,save,lock,unlock,vHostsDir,lstVh)
#tools = Frame(win).pack()

status = Label(win,text="AVM ver. "+appVersion)
status.pack(side=BOTTOM, expand=False)
asd.pack(side=LEFT,expand=True,fill=BOTH)
body.pack(expand=True,fill=BOTH)

##
# Central form Controls
##
lblVHname = Label(box,anchor=E,text="Nazwa pliku VHosta")#, expand=YES)
#entVHname = Entry(box)
lblSrvIpPort = Label(box,anchor=E,text="Adres IP : numer Portu")
#boxIpPort = Frame(box)
#entF2ip = Entry(boxIpPort,width=15).pack(side=LEFT)
entSrvIp.pack(side=LEFT)
#entF2port = Entry(boxIpPort,width=4).pack(side=RIGHT)
entSrvPort.pack(side=RIGHT)
lblDomain = Label(box,anchor=E,text="Nazwa serwera (domena)")
#entDomain = Entry(box)
lblAdmEmail = Label(box,anchor=E,text="Adres e-mail administratora")
#entAdmEmail = Entry(box)
lblDocsDir = Label(box,anchor=E,text="Ścieżka dokumentów")
#boxDocDir = Frame(box)
#entF5 = Entry(boxDocDir)	# dlaczego rozbijamy Entry().pack() na dwa wiersze?
entDocsDir.pack(side=LEFT) # Entry().pack() returns None
btnDocsDirBrw = Button(box,text="...", command=lambda: browseDir("docsDir") )
#btnDocsDirBrw = Button(boxDocDir,text="...", command=browseDir).pack(side=RIGHT)
									#	command= ()=>{ browseDir("docsDir"); }
lblErrLogDir = Label(box,anchor=E,text="Ścieżka do dziennika błędów")
btnErrLogDirBrw = Button(box,text="...", command=lambda: browseDir("errLogDir") )#.pack(side=RIGHT)

lblCmpLogDir = Label(box,anchor=E,text="Ścieżka do dziennika ogólnego")
btnCmpLogDirBrw = Button(box,text="...", command=lambda: browseDir("cmpLogDir") )

lblDoc2Dir = Label(box,anchor=E,text="Ścieżka dokumentów")
btnDoc2DirBrw = Button(box,text="...", command=lambda: browseDir("doc2Dir") )

lblOptions = Label(box,anchor=E,text="Opcje")

lblVHname.grid(sticky=NSEW,row=1,column=1)
entVHname.grid(sticky=W,row=1,column=2, pady=3)
lblSrvIpPort.grid(sticky=NSEW,row=2,column=1)
boxIpPort.grid(sticky=W,row=2,column=2, pady=3)

lblDomain.grid(sticky=E,row=3,column=1)
entDomain.grid(sticky=W,row=3,column=2, pady=3)
lblAdmEmail.grid(sticky=E,row=4,column=1)
entAdmEmail.grid(sticky=W,row=4,column=2, pady=3)

lblDocsDir.grid(sticky=E,row=5,column=1)
boxDocDir.grid(sticky=E,row=5,column=2, pady=3)
btnDocsDirBrw.grid(sticky=E,row=5,column=3)

lblErrLogDir.grid(sticky=E,row=6,column=1)
entErrLogDir.grid(sticky=W,row=6,column=2, pady=3)
btnErrLogDirBrw.grid(sticky=E,row=6,column=3)

lblCmpLogDir.grid(sticky=E,row=7,column=1)
entCmpLogDir.grid(sticky=W,row=7,column=2, pady=3)
btnCmpLogDirBrw.grid(sticky=W,row=7,column=3)

lblDoc2Dir.grid(sticky=E,row=8,column=1)
entDoc2Dir.grid(sticky=W,row=8,column=2, pady=3)
btnDoc2DirBrw.grid(sticky=W,row=8,column=3)

lblOptions.grid(sticky=W,row=9,column=1,columnspan=2)
box.pack(fill=BOTH)#expand=True,

##		####	####	##
# Aside VHosts file List #
##						##
lblLst1 = Label(asd,text="Lista plików VHost")
lblLst1.pack(fill=X) #expand=YES)

scb = Scrollbar(asd,orient='vertical') #,command=lsb.yview)
scb.pack(side=RIGHT,fill=Y)#)#side=RIGTH,fill=Y)
lsb = Listbox(asd,
	selectmode='browse',
	exportselection=False,
	yscrollcommand=scb.set)
	#listvariable=lstVhosts,
lstVhosts = StringVar(value=lstVh)
setVhostList(lstVh)#osts)
lsb.bind('<<ListboxSelect>>',pickFile)
lsb.pack(side=LEFT,fill=BOTH)
#lsb['yscrollcommand']=scb.set
scb.config(command=lsb.yview)

# TU BYŁO textarea

boxTxa.pack()

mainloop()
