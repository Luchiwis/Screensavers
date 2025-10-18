from customtkinter import *
from os import system as cmd

class App(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode('dark')
        set_default_color_theme('green')
        self.geometry('300x250')
        self.title('Screensaver Selector')
    def choose(self, choice:str):
        self.program = f'{choice}.pyw'
        self.destroy()

root = App()

labl = CTkLabel(root, text='Select a scrensaver', text_color='green', font=CTkFont('Arial', 22))
labl.place(x=55, y=5)

but1 = CTkButton(root, width=50, text='Lines', font=CTkFont('Arial', 25, 'bold'), text_color='black', command=lambda: root.choose('lines'))
but1.place(x=40, y=77)

but1 = CTkButton(root, width=50, text='Squares', font=CTkFont('Arial', 25, 'bold'), text_color='black', command=lambda: root.choose('squares'))
but1.place(x=150, y=77)

# root.bind('<Button>', print) x=53, y=77 - x=172, y=77

root.mainloop()

cmd(f'.\\{root.program}')