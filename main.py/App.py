from tkinter import *
#from app_settings import *
from os import *


w_width = 414
h_height = 816

bg_color = "#FFA500"

class App():
    def __init__(self):
        window = Tk()
        window.geometry(str(w_width) + "x" + str(h_height))
        window.title("Dish Lister")

        top_frame = Frame(background='orange', width=w_width, height= 100)
        top_frame.pack(side='top')

        main_frame = Frame(background=bg_color, width=w_width, height=h_height)
        main_frame.pack

        bottom_frame = Frame(background='yellow', width=w_width, height=100)
        bottom_frame.pack(side='bottom')

        home_button = Button(top_frame, text="Menu", height=5, width=5, bg='white')
        home_button.place(x=15,y=7)

        exit_button = Button(bottom_frame, text="Exit", height=5, width=5, bg='white')
        exit_button.place(x=100,y=100)

        dirname = path.dirname(__file__)
        filename = path.join(dirname, 'images/')

        print("the path is", filename)

        window.mainloop()

