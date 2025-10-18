from customtkinter import *
from random import randint as num
from threading import Thread as Th

set_default_color_theme('green')
set_appearance_mode('dark')

lines = []

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title('Lines')

def color():
    random_number = num(0, 0xFFFFFF)
    hex_color = f'#{random_number:06x}'
    return hex_color

def makeline(x:int):
    global lines
    lines.append(canvas.create_line(x, 0, x, 400, fill=color()))

def makelines():
    global lines
    for x in range(0, 600):
        makeline(x)
    while 1:
        lines.reverse()
        for line in lines:
            canvas.itemconfig(line, fill=color())

root = App()
canvas = CTkCanvas()

canvas.config(width=600, height=400, bg='black')
canvas.pack()

thread = Th(target=makelines)
thread.daemon = True
thread.start()

root.mainloop()