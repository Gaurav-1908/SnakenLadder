from cProfile import label
from tkinter import *
from board import gameboard
win = None

def select(players):
    win.destroy()
    gameboard('mul',players)

def selectplayers():
    print('in select Player')
    global win
    win = Tk()
    win.title("Players")
    win.geometry('650x350')
    win.config(background="#000088")

    label = Label(win, text='Select No. of Players', font=('times new roman', 15),bg="#2bff0a",relief="solid")
    label.place(x = 50, y = 50 , height=100, width=550)

    b1 = Button(win, command = lambda:select(1) ,text = '1', font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
    b1.place(x = 50, y= 200 , height=100, width= 100)

    b2 = Button(win, command = lambda:select(2) ,text = '2', font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
    b2.place(x = 200, y= 200 , height=100, width= 100)

    b3 = Button(win, command = lambda:select(3) ,text = '3', font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
    b3.place(x = 350, y= 200 , height=100, width= 100)

    b4 = Button(win, command = lambda:select(4) ,text = '4', font=('times new roman', 20), activebackground="#FF0000",bg="#ffc30f")
    b4.place(x = 500, y= 200 , height=100, width= 100)

    win.mainloop()

# def board(players):
#     print(players)

