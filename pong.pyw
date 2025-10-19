import customtkinter as ctk
from random import randint, random
from threading import Thread
from math import pi, sin, cos


ctk.set_default_color_theme('green')
ctk.set_appearance_mode('dark')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 400
        self.geometry = f"{self.width}x{self.height}"
        self.title = "pong"
        self.canvas = ctk.CTkCanvas(self,width = self.width, height = self.height)
        self.canvas.pack()
        self.radius = 20
        self.ballx = 200
        self.bally = 200
        self.ballangle = pi/4
        self.vel = 3
        # threading
        self.thread = Thread(target=self.update)
        self.thread.daemon = True
        self.thread.start()
        
    def color(self):
        random_number = randint(0, 0xFFFFFF)
        hex_color = f'#{random_number:06x}'
        return hex_color
    
    def update(self):
        while True:
            self.checkborder()
            self.draw_ball(self.ballx,self.bally,self.color())
            # new position
            self.ballx += self.vel * cos(self.ballangle)
            self.bally += self.vel * sin(self.ballangle)
    
    def checkborder(self):
        top = self.bally - self.radius < 0
        bottom = self.bally + self.radius > self.height
        left = self.ballx - self.radius < 0
        right = self.ballx + self.radius > self.width
        if (top or bottom or left or right):
            self.ballangle += pi/2
            self.add_angle_variation()
            # self.canvas.delete("all") xd

    def draw_ball(self,x,y,color):
        self.canvas.create_aa_circle(x,y,self.radius, fill=color)
        
    def add_angle_variation(self,tolerance=0.001):
        self.ballangle += random() * tolerance



root = App()
root.mainloop()