from tkinter import *
import zipfile
import tarfile

dd = StringVar()			# _POST from OptionMenu
listVh = []
vHostsDir = None
archMode = None
DD_DEF = "Archiwizuj"
DD_FILE = "plik"
DD_DIR = "katalog"

#def pickArcMeth():
#	global arcMeth
#	arcMeth = v.get()

def archiveIt(event):
	#if( event==DD_FILE ):
	global archMode
	archMode = event
	arcMeth = "zip"
	if arcMeth=="tar":
		tarIt()
	if arcMeth=="zip":
		zipIt()
	print("Wybrano archiwizację do: "+arcMeth)
	dd.set( DD_DEF )		# powrót do pierwotnie wyświetlanego tekstu
	
def zipIt():
	#tf = zipfile.ZipFile(archNameZip,"w")
	global archMode
	global listVh
	archNameZip = "2022-01-04_202500.zip"	#TODO dynamic
	with zipfile.ZipFile(archNameZip,"w") as tf:
		#files = os.listdir(".")
		files = []
		if( archMode==DD_FILE ):
			files = ["000-local.conf"]	#TODO dynamic
		else:
			print("katalog: "+vHostsDir)	#TODO dynamic
			print(listVh)	#TODO dynamic
			files = listVh
		for file in files:
			if file!=archNameZip:
				tf.write(vHostsDir+"/"+file)
		for fin in tf.namelist():
			print("Dodano %s" % fin)
		#	print(tf.getinfo(fin))
		tf.close()

def unZip():
	print("unzip")
	with zipfile.ZipFile(archNameZip, "r") as uzi:
		for file in uzi.namelist():
			uzi.extract(file,"out")

def tarIt():
	with tarfile.open(archNameTar,"w") as tf:
		files = os.listdir(".")
		for file in files:
			if file!=archNameTar:
				tf.add(file)
		for fin in tf.getnames():
			print("Dodano %s" % fin)
		tf.close()

def unTar():
	with tarfile.open(archNameTar,"r:") as utr:
		for file in utr.getnames():
			utr.extract(file,"out")
		utr.close()

def build(win,browseVhostDir,read,save,lock,unlock,LvHostsDir,lstVh):
	global listVh
	global vHostsDir
	vHostsDir = LvHostsDir	# przypisanie wartości z Parametru do zmiennej lokalnej
	listVh = lstVh
	tools	= Frame(win)
	path	= Frame(win)
	tools.pack(fill=X)
	path.pack(fill=X)

	opts	= [DD_FILE,DD_DIR]
	dd.set( DD_DEF )
	drop	= OptionMenu(tools, dd, *opts, command=archiveIt )
	btnBrw	= Button(path,text="Zmień katalog", command=browseVhostDir)
	lblPath	= Label(path,text="PATH: "+vHostsDir)
	btnWrt	= Button(tools,text="Zapisz",command=save)
	#btnRed	= Button(tools,text="Otwórz",command=read)
	btnBrw.pack(side=LEFT)
	lblPath.pack(side=LEFT)
	drop.pack(side=LEFT)
	btnWrt.pack(side=LEFT)
	#btnRed.pack(side=LEFT)

	if(1==1):
		#for (text,value) in radios.items():
		#	Radiobutton(tools,
		#	text=text,
		#	variable=v,
		#	value=value,
		#	command=pickArcMeth).pack()
		#	# ,indicator=0
		print()
	#btnZip	= Button(tools,text="Archiwizuj",command=archiveIt)
	#btnUzi	= Button(tools,text="Wypakuj",command=unZip)
	btnChk	= Button(tools,text="Walidacja")
	btnCnf	= Button(tools,text="Ustawienia")
	#btnLck	= Button(tools,text="Lock",command=lock)
	#btnUnl	= Button(tools,text="Unlock",command=unlock)
	#btnZip.pack(side=BOTTOM)
	#btnUzi.pack(side=RIGHT)
	# ponieważ side=R działa jak CSS Float, więc najpierw dodaj co ma być na końcu
	btnCnf.pack(side=RIGHT)
	btnChk.pack(side=RIGHT)
	#btnLck.pack(side=LEFT)
	#btnUnl.pack(side=LEFT)
	return tools
