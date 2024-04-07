
from tkinter import *
import tkinter.messagebox

play = Tk()
play.geometry('600x500')
play.title('Tic-Tac-Toe')
play.configure(bg='lavender')


bclick = True
turns = 0
buttons = StringVar()

def btnclick(buttons):
    global bclick,turns
    if buttons['text'] == ' ' and bclick == True:
        buttons['text'] = 'X'
        bclick = False
        turns += 1
        possibilities()

    elif buttons['text'] == ' ' and bclick == False:
        buttons['text'] = 'O'
        bclick = True
        turns += 1
        possibilities()

    else:
        tkinter.messagebox.showwarning('Tic-Tac-Toe','Button Already Clicked!....')

def possibilities():
    if (b1['text']=='X' and b2['text']=='X' and b3['text']=='X' or
        b4['text']=='X' and b5['text']=='X' and b6['text']=='X' or
        b7['text']=='X' and b8['text']=='X' and b9['text']=='X' or
        b1['text']=='X' and b4['text']=='X' and b7['text']=='X' or
        b2['text']=='X' and b5['text']=='X' and b8['text']=='X' or
        b3['text']=='X' and b6['text']=='X' and b9['text']=='X' or
        b1['text']=='X' and b5['text']=='X' and b9['text']=='X' or
        b3['text']=='X' and b5['text']=='X' and b7['text']=='X'):

        tkinter.messagebox.showinfo('Tic-Tac-Toe',p1.get() + " Wins!...")

    elif(b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
        b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
        b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
        b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
        b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
        b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O' or
        b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
        b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O'):

        tkinter.messagebox.showinfo('Tic-Tac-Toe', p2.get() + " Wins!...")

    elif turns == 9:
        tkinter.messagebox.showinfo('Tic-Tac-Toe', "Match Draw")


def reset():

    global p1,p2
    p1 = StringVar()
    p2 = StringVar()

    Label(play,text='Tic-Tac-Toe',font=('calibri',17),bg='purple',fg='Lavender').place(x=240,y=15)
    Label(play,text='Player 1 Name :',font=('calibri',17),fg='purple',bg='Lavender').place(x=40,y=65)
    Label(play,text='Player 2 Name :',font=('calibri',17),fg='purple',bg='Lavender').place(x=40,y=105)

    Entry(play,textvariable=p1,font=(10),bg='lavender',fg='purple',width='30').place(x=220,y=75)
    Entry(play,textvariable=p2,font=(10),bg='lavender',fg='purple',width='30').place(x=220,y=115)


    global bclick,turns
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    bclick = True
    turns = 0
    b1 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b1))
    b1.place(x=150,y=200)
    b2 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b2))
    b2.place(x=220,y=200)
    b3 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b3))
    b3.place(x=290,y=200)
    b4 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b4))
    b4.place(x=150,y=260)
    b5 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b5))
    b5.place(x=220,y=260)
    b6 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b6))
    b6.place(x=290,y=260)
    b7 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b7))
    b7.place(x=150,y=320)
    b8 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b8))
    b8.place(x=220,y=320)
    b9 = Button(play,text=' ',font=('calibri'),bg='purple',fg='lavender',width='7',height='2',command=lambda:btnclick(b9))
    b9.place(x=290,y=320)

    Button(play,text='RESET',font=('calibri',12,'bold'),bg='purple',fg='lavender',activebackground='lavender',
           activeforeground='purple',command=reset).place(x=230,y=410)

reset()

play.mainloop()
