from tkinter import *
from tkinter import messagebox
import random
r_x = 5
r_y = 635
v_x = 5
v_y = 675


players = 0
x = 1
steps = 0

players_color = ['red','yellow','orange','voilet']
red_pos = 1
violet_pos = 1
board = [[100,99,98,97,96,95,94,93,92,91],
        [81,82,83,84,85,86,87,88,89,90],
        [80,79,78,77,76,75,74,73,72,71],
        [61,62,63,64,65,66,67,68,69,70],
        [60,59,58,57,56,55,54,53,52,51],
        [41,42,43,44,45,46,47,48,49,50],
        [40,39,38,37,36,35,34,33,32,31],
        [21,22,23,24,25,26,27,28,29,30],
        [20,19,18,17,16,15,14,13,12,11],
        [1,2,3,4,5,6,7,8,9,10]
        ]

snake = {
    99 : 41,
    76 : 58,
    89 : 53,
    40 : 3,
    27 : 5
}

ladder = {
    4 : 25,
    13 : 46,
    43 : 77,
    74 : 92,
    62 : 81
}
def indexof( char):
    for sub_list in board:
        if char in sub_list:
            return (board.index(sub_list), sub_list.index(char))
def play():

    global red,vio
    red = Label(win,text = 'P1' ,bg='#FFFFFF',fg = '#FF0000')
    red.place(x = r_x, y= r_y, height= 20, width=20)

    vio = Label(win, text ='P2',bg='#FFFFFF',fg = '#EE82EE')
    vio.place(x = v_x, y= v_y, height= 20, width=20)
    # violet.destroy()
    
    
    
def roll():
    global x,steps,l3
    x = random.choice((1,2,3,4,5,6))
    steps = steps + 1
    l3.config(text=x)
    move(x)

def move(dice):
    global red_pos,violet_pos,r_x,v_x,red,vio,r_y,v_y,win
    if steps % 2 == 1: #1st palyer move
        red_pos = red_pos + dice
        if red_pos in ladder:
            red_pos = ladder[red_pos]
        elif red_pos in snake:
            red_pos = snake[red_pos]
        
        if red_pos == 100:
            messagebox.showinfo("Game Over", "P1 Wins")
            win.destroy()
        elif red_pos > 100:
            red_pos = red_pos - dice
        
        pos = indexof(red_pos)
        r_x = 5 + pos[1]*70
        r_y = 5 + pos[0]*70
        
        

    else: # #2nd player move
        violet_pos = violet_pos + dice
        if violet_pos in ladder:
            violet_pos = ladder[violet_pos]
        elif violet_pos in snake:
            violet_pos = snake[violet_pos]

        if violet_pos == 100:
            messagebox.showinfo("Game Over", "P2 Wins")
            win.destroy()
        elif violet_pos > 100:
            violet_pos = violet_pos - dice
        

        pos = indexof(violet_pos)
        v_x = v_x + 70*dice
        v_x = 5 + pos[1]*70
        v_y = 45 + pos[0]*70
        
    red.destroy()
    vio.destroy()
        
    
    red = Label(win,text = 'P1' ,bg='#FFFFFF',fg = '#FF0000')
    red.place(x = r_x, y= r_y, height= 20, width=20)

    vio = Label(win, text ='P2',bg='#FFFFFF',fg = '#EE82EE')
    vio.place(x = v_x, y= v_y, height= 20, width=20)

def gameboard(mode,players = 0):
    color = -1
    global win
    win = Tk()
    win.title("Snake And Ladder")
    win.geometry('1000x700')
    win.config(background="#000088")
    for row in range(10):
        for col in range(10):
            if board[col][row] in ladder:
                if color == -1:
                    l1 = Label(win, text='L'+ str(ladder[board[col][row]]), font=('times new roman', 15),bg="#FFFFFF",relief="solid",fg = '#DC9000')
                    l1.place(x=row*70, y=col*70, width=70, height=70)
                    color = -1*color
                else:
                    l1 = Label(win, text='L' + str(ladder[board[col][row]]), font=('times new roman', 15),bg="#F0F0F0",relief="solid",fg = '#DC9000')
                    l1.place(x=row*70, y=col*70, width=70, height=70)
                    color = -1*color
            elif board[col][row] in snake:
                if color == -1:
                    l1 = Label(win, text='S'+ str(snake[board[col][row]]), font=('times new roman', 15),bg="#FFFFFF",relief="solid",fg = '#FF0000')
                    l1.place(x=row*70, y=col*70, width=70, height=70)
                    color = -1*color
                else:
                    l1 = Label(win, text='S'+str(snake[board[col][row]]), font=('times new roman', 15),bg="#F0F0F0",relief="solid",fg = '#FF0000')
                    l1.place(x=row*70, y=col*70, width=70, height=70)
                    color = -1*color
            else:
                if color == -1:
                    l1 = Label(win, text=board[col][row], font=('times new roman', 15),bg="#FFFFFF",relief="solid",fg = '#030000')
                    l1.place(x=row*70, y=col*70, width=70, height=70)
                    color = -1*color
                else:
                    l1 = Label(win, text=board[col][row], font=('times new roman', 15),bg="#F0F0F0",relief="solid",fg = '#030000')
                    l1.place(x=row*70, y=col*70, width=70, height=70)
                    color = -1*color
        color = -1*color

        l2 = Label(win, text='Roll The Dice', font=('times new roman', 15), bg="#F0F0F0",relief="solid",fg = '#000000')
        l2.place(x = 750, y = 70, height=70, width=200)

        b1 = Button(win, command = roll ,text="Roll", font=('times new roman', 20), activebackground="#F0F0F0",bg="#FFFFFF")
        b1.place(x=750, y=170, width=70, height=70)
            
        global l3
        l3 = Label(win, text=x, font=('times new roman', 15), bg="#F0F0F0",relief="solid",fg = '#000000')
        l3.place(x = 870, y = 170, height=70, width=70)

        b2 = Button(win, command = play ,text="Play", font=('times new roman', 20), activebackground="#F0F0F0",bg="#FFFFFF")
        b2.place(x=750, y=270, width=200, height=70)

        # red = Label(win,text = r_x ,bg='#FFFFFF',fg = '#FF0000')
        # red.place(x = r_x, y= r_y, height= 20, width=20)

        # violet = Label(win, text ='P2',bg='#FFFFFF',fg = '#EE82EE')
        # violet.place(x = v_x, y= v_y, height= 20, width=20)
        
    win.mainloop()

gameboard('mul')