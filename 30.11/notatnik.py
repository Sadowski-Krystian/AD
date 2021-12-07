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
    else:
        input2["state"] = 'normal'

    



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
btnLock = Button(win, command=lock, text="Zablokuj/Odblokij").pack()
frame.pack()
mainloop()