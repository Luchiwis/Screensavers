from customtkinter import *
from random import randint as num
from threading import Thread as Th

set_default_color_theme('green')
set_appearance_mode('dark')

sqrs = []

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('Squares')

def color():
    random_number = num(0, 0xFFFFFF)
    hex_color = f'#{random_number:06x}'
    return hex_color

def makesqr(x:int, y:int):
    global sqrs
    sqrs.append(canvas.create_rectangle(x, y, x+10, y+10, outline=color()))

def makesqrs():
    global sqrs
    for y in range(0, 40):
        for x in range(0, 60):
            makesqr(x*10, y*10)
    while 1:
        sqrs.reverse()
        for sqr in sqrs:
            canvas.itemconfig(sqr, outline=color())

root = App()
canvas = CTkCanvas()

canvas.config(width=600, height=400, bg='black')
canvas.pack()

thread = Th(target=makesqrs)
thread.start()

root.mainloop()