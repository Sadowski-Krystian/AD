from tkinter import * 

win = Tk()
win.title('My First PyApp')
win.geometry('640x240')
lbl1 = Label(win, text='SCP - 173')
lbl1.pack()
lbl2 = Label(win, text='Ten Poniżej to entry')
lbl2.pack()
entr1 = Entry(win, background='red')
entr1.pack()
bt1 = Button(win, text="jestem przyciskiem", background='pink').pack()
mainloop()