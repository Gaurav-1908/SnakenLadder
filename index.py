from tkinter import *
from players import selectplayers
from board import gameboard
win = Tk()

def multiplayer():
    win.destroy()
    selectplayers()

def computer():
    win.destroy()
    gameboard('sys')

def mode():
    
    win.title("Index")
    win.geometry('450x300')
    win.config(background="#000088")

    b1 = Button(win, command=multiplayer ,text = 'Multiplayer', font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
    b1.place(x=50, y=100, width=150, height=100)

    b1 = Button(win, command = computer ,text="Computer", font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
    b1.place(x=250, y=100, width=150, height=100)

    win.mainloop()
