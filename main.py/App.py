from tkinter import *
#from app_settings import *
from os import *

from PIL import ImageTk, Image

w_width = 414
h_height = 816

bg_color = "#FFA500"



class App():

    current_frame = "Home"
    

    def __init__(self):

        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(h_height))
        self.window.title("Dish Lister")

        #self.window.iconbitmap('c:/gui/codemy.ico')

        

        self.top_frame = Frame(background='orange', width=w_width, height= 75)
        self.top_frame.pack(side='top')
    
        image = Image.open("main.py\imgs\logo.png")
        photo = ImageTk.PhotoImage(image.resize((450, 135)))

        #image_label = Label(self.top_frame, image=photo)
        #image_label.pack()

        #bg_image = Label(self.home_frame, image=photo)
        #bg_image.pack()

        #self.image_label = Tk.Label(self, image=self.image)
        #self.image_label.pack()

        #canvas = Canvas(height = 100, width = 100)
        #canvas.pack()

        #img = PhotoImage(file = r'[main.py\\imgs\\logo.png]')
        #bg = Label(canvas, image = img)
        #bg.pack()


        self.home_frame = Frame(background=bg_color, width=w_width, height=h_height)
        self.home_frame.pack

        self.title_label = Label(self.home_frame, text="Home")
        self.title_label.pack()

        bg_image = Label(self.top_frame, image=photo)
        bg_image.pack()

        self.bottom_frame = Frame(background=bg_color, width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        self.home_button = Button(self.top_frame, text="Menu", height=3, width=5, bg='orange', command= lambda: self.go_to_frame("Home"), borderwidth= 0)
        self.home_button.place(x=0,y=50)

        self.exit_button = Button(self.bottom_frame, text="Exit", height=3, width=3, bg='white', command=self.exit)
        self.exit_button.place(x=15,y=7)

        #click_btn= PhotoImage(file='main.py\imgs\cog image.png')
        #img_label= Label(image=click_btn)
        #button= Button(image=click_btn, command= funtimes, borderwidth=0)
        #button.pack(pady=30)
        #text= Label(text= "no123")
        #text.pack(pady=30)

        self.settings_button = Button(self.top_frame, text="Settings", height=3, width=5, bg='white', command= lambda: self.go_to_frame("Settings"))
        self.settings_button.place(x=370,y=50)

        


        ###settings frame####
        self.settings_frame = Frame(background='white', width=w_width, height=h_height)
        self.settings_frame.pack()

        self.title_label = Label(self.settings_frame, text="Settings")
        self.title_label.pack()

        

        #self.exit_button = Button(self.settings_frame, text="Exit", height=5, width=5, bg='white', command=self.exit)
        #self.exit_button.place(x=15,y=7)

        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        print("the path is", self.filename)

        #my_menu = Menu()
        #self.config(menu=my_menu)

        #def our_command():
            #self.my_label = Label(text="womp womp").pack()

            #file_menu = Menu(my_menu)
            #my_menu.add_cascade(Label="File", menu=file_menu)
            #file_menu.add_command(Label="New...", command=our_command)
            #file_menu.add_separator()
            #file_menu.add_command(Label="Exit", command=quit)

            #edit_menu = Menu(my_menu)
            #my_menu.add_cascade(Label="Edit", menu=edit_menu)
            #edit_menu.add_command(Label="Cut", command=our_command)
            #edit_menu.add_command(Label="Copy", command=our_command)
        
      


        self.window.mainloop()



    def go_to_frame(self, next_frame):

        if self.current_frame == "Home":
            self.home_frame.pack_forget()
        elif self.current_frame == "Settings":
            self.settings_frame.pack_forget()
       
        if next_frame == "Settings":
                self.settings_frame.pack()
                self.current_frame = "Settings"
        elif next_frame == "Home":
                self.home_frame.pack()
                self.current_frame = "Home"

    #def settings(self):
        #self.settings_frame


    def exit(self):
        self.window.destroy()

    
    #def home_open(self):
        #print("yes")


    



    
