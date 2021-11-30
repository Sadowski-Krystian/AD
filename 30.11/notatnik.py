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

    



fileName = Label(win, text="text").pack()
input = Entry(win)
input.insert(0, "Nowy-Plik")
input.pack()
content = Label(win, text="treść").pack()
input2 = Text(win, height=12)
input2.insert(1.0, "Przykładowa zawartość")
input2.pack()
btn = Button(win, command=save, text="zapisz").pack()
btnLock = Button(win, command=lock, text="Zablokuj/Odblokij").pack()
mainloop()

