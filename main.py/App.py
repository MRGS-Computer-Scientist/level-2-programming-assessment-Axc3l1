from tkinter import *
#from app_settings import *
from os import *

w_width = 414
h_height = 816

bg_color = "#FFA500"



class App():

    

    def __init__(self):

        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(h_height))
        self.window.title("Dish Lister")

        #self.window.iconbitmap('c:/gui/codemy.ico')

        self.top_frame = Frame(background='orange', width=w_width, height= 100)
        self.top_frame.pack(side='top')

        self.main_frame = Frame(background=bg_color, width=w_width, height=h_height)
        self.main_frame.pack

        self.bottom_frame = Frame(background='yellow', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        self.home_button = Button(self.top_frame, text="Menu", height=5, width=5, bg='white', command=self.home_open)
        self.home_button.place(x=15,y=7)

        self.exit_button = Button(self.bottom_frame, text="Exit", height=5, width=5, bg='white', command=self.exit)
        self.exit_button.place(x=15,y=7)

        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        print("the path is", self.filename)

        my_menu = Menu()
        self.config(menu=my_menu)

        def our_command():
            self.my_label = Label(text="womp womp").pack()

            file_menu = Menu(my_menu)
            my_menu.add_cascade(Label="File", menu=file_menu)
            file_menu.add_command(Label="New...", command=our_command)
            file_menu.add_separator()
            file_menu.add_command(Label="Exit", command=quit)

            edit_menu = Menu(my_menu)
            my_menu.add_cascade(Label="Edit", menu=edit_menu)
            edit_menu.add_command(Label="Cut", command=our_command)
            edit_menu.add_command(Label="Copy", command=our_command)
        
        self.window.mainloop()



  

    def exit(self):
        self.window.destroy()

    
    def home_open(self):
        print("yes")


    



    
        
      
    