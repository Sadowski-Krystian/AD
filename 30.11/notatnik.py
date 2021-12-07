from os import name, write
from tkinter import * 

win = Tk()
win.geometry("320x480")

def save():
    s1 = input.get()
    s2 = input2.get(1.0, END)
    input2["state"]='disable'
    print(s1)
    print(s2)
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
                    lc = patterns.index(pattern)
                    print(str(ic)+" "+lineCont)
                    print(cmdKeys[ic])
            input2.insert(str(row+1)+'.0',lineCont)
            row+=1
    



frame  = Frame(win)
scb = Scrollbar(frame, orient="vertical")
fileName = Label(win, text="text").pack()
input = Entry(win)
input.insert(0, "Nowy-Plik")
input.pack()
content = Label(frame, text="treść").pack()
input2 = Text(frame, height=12, yscrollcommand=scb.set)
input2.insert(1.0, "Przykładowa zawartość")

scb.pack(side=RIGHT, fill=Y)
scb.config(command=input2.yview)
input2.pack()
btn = Button(win, command=save, text="zapisz").pack()
btn = Button(win, command=read, text="Otwórz").pack()
btnLock = Button(win, command=lock, text="Zablokuj/Odblokij").pack()
frame.pack()
mainloop()