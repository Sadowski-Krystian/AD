from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Tabs")
win.geometry("640x480")

tc = ttk.Notebook(win)
tab1 = ttk.Frame(tc)
tab2 = ttk.Frame(tc)

tc.add(tab1, text="A")
tc.add(tab2, text="B")

tc.pack(expand=1, fill="both")

ttk.Label(tab1, text="Yellow this is Tab A").pack()
ttk.Label(tab2, text="Beton this is Tab B").pack()

mainloop()
