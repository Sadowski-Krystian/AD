from tkinter import *
from typing import List
win = Tk()
win.title("Mw wishList")
win.geometry('640x480')
asd = Frame(win, background='red', height=100)
lstItemsArr = ('AI', 'AD', 'AM', 'PR', 'TiDA', 'BD', 'WI', 'ZAW', 'CMS', 'INF', 'SO', 'SKiBW')
lstItemsArr = ['AI', 'AD', 'AM', 'PR', 'TiDA', 'BD', 'WI', 'ZAW', 'CMS', 'INF', 'SO', 'SKiBW']

lstItems = StringVar(value=lstItemsArr)

scb = Scrollbar(asd, orient="vertical")
lsb = Listbox(asd, listvariable=lstItems, selectmode="browse", yscrollcommand=scb.set)
lsb.pack(side=LEFT)
scb.pack(side=LEFT, fill=Y)
scb.config(command=lsb.yview)
asd.pack(side=LEFT, anchor=N, expand=False)
status = Label(win , text="jestek statusem")
def addEventClick():
    status['text'] = "kliknołes mnie"

btn1 = Button(win, text="przycisk", command=addEventClick)
btn1.pack()
status.pack()
mainloop()