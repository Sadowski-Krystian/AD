from tkinter import *

win = Tk()
win.title('My First Py Layout')



left = Frame(win, height=500, width=200,)
lstItemsArr = ('Nowy VHost', 'vhost-1', 'vhost-2', 'vhost-a', 'vhost-b', 'vhost-c')
lstItems = StringVar(value=lstItemsArr)
scb = Scrollbar(left, orient="vertical")
lsb = Listbox(left, listvariable=lstItems, selectmode="browse", yscrollcommand=scb.set)
lsb.pack(side=LEFT)
scb.pack(side=LEFT, fill=Y)

left.grid(row="1", column="1")
btm = Frame(win, height=200, background='red')

for x in range(1,7):
    Label(btm, text="Jakaś opcja "+str(x)).grid(row=x, column="1")
btm.grid(row="2", column="2")

top = Frame(win, height=300)
names = ('Nazwa pliku VHosta', 'Adres IP: numer portu', 'Nazwa Serwera (domena)', 'Adres e-mail administrator', 'Scieżka dokumentów', 'Scieżka do dziennika Błędów', 'Scieżka do dziennika ogólnego', 'Scieżka dokumentów')
Label(top, text="konfiguracja").grid(row="1", column="1")
Label(top, text="Zawartość").grid(row="1", column="2")


for a in range(2, 10):
    Label(top, text=names[a-2]).grid(row=a, column="1")

for c in range(2,10):   
    Entry(top).grid(row=c, column="2")

for i in range(6,10):
    Button(top, text='przeglądaj').grid(row=i, column="3")
top.grid(row="1", column="2")


#top = Frame(win, height=200, background='yellow')
#top.pack(side=TOP, expand=False, fill=BOTH)
#left = Frame(win, height=500, width=200, background="red")
#left.pack(side=LEFT, expand=False, fill=BOTH)
#right = Frame(win, height=500, width=200, background="green")
#right.pack(side=RIGHT, expand=False, fill=BOTH)
#btn = Frame(win, height=200, background="blue")
#grd = Frame(btn, background="white")
#Button(grd, text="1").grid(row="1", column="1")
#Button(grd, text="2").grid(row="1", column="2")
#Button(grd, text="3").grid(row="1", column="3")
#Button(grd, text="4").grid(row="2", column="1")
#Button(grd, text="5").grid(row="2", column="2")
#Button(grd, text="6").grid(row="2", column="3")
#Button(grd, text="7").grid(row="3", column="1")
#Button(grd, text="8").grid(row="3", column="2")
#Button(grd, text="9").grid(row="3", column="3")
#grd.pack()
#btn.pack(side=BOTTOM, expand=False, fill=BOTH)
#Label(win, text="Jestem wolnym elektronem", background='pink').place(x=13, y=13, height="64")
mainloop()