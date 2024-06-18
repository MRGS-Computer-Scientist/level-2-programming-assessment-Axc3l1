from tkinter import *
from tkinter import messagebox
#from app_settings import *
from os import *
from PIL import ImageTk, Image
import sqlite3

w_width = 414
h_height = 816

bg_color = "#FF851B"

button_font=("airel", 20, "bold")
fun_font=("airel", 10, "bold")

class App():

    current_frame = "Home"
    
    #note_entry = Text()
    #note_entry.pack()

    def __init__(self):

        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(h_height))
        self.window.title("Dish Lister")

        #self.window.iconbitmap('c:/gui/codemy.ico')

        

        self.top_frame = Frame(background='orange', width=w_width, height= 75)
        self.top_frame.pack(side='top')
    
        image = Image.open("main.py\imgs\logo.png")
        photo = ImageTk.PhotoImage(image.resize((450, 135)))

        settings_icon = Image.open("main.py\imgs\cog_image.png")
        settings_image = ImageTk.PhotoImage(settings_icon.resize((50,50)))

        home_icon = Image.open("main.py\imgs\home.png")
        home_image= ImageTk.PhotoImage(home_icon.resize((50,50)))
      

        #self.save_button = Button(self.top_frame, text="save note", command=self.save_note)
        #self.save_button.pack()

        self.home_frame = Frame(background=bg_color, width=w_width, height=h_height)
        #self.home_frame.pack()

        self.title_label = Label(self.home_frame, text="Home")
        self.title_label.pack()

        bg_image = Label(self.top_frame, image=photo)
        bg_image.pack()

        self.bottom_frame = Frame(background=bg_color, width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        #self.home_button = Button(self.top_frame, text="Menu", height=3, width=5, bg='orange', command= lambda: self.go_to_frame("Home"), borderwidth= 0)
        #self.home_button.place(x=0,y=50)

        #self.view_button = Button(self.bottom_frame, text="view notes", command=self.view_notes)
        #self.view_button.pack()

        self.newrecipie_button = Button(self.bottom_frame, text="New Recipie", height=3, width=10, bg="#FF851B", font=button_font, borderwidth=0, command=self.new_rec)
        self.newrecipie_button.place(x=230,y=0)

        self.home_button = Button(self.top_frame, image=home_image, borderwidth= 0, highlightthickness=0, command= lambda: self.go_to_frame("Home"))
        self.home_button.place(x=-5,y=50)

        self.exit_button = Button(self.bottom_frame, text="Exit", height=3, width=3, bg="#FF851B", borderwidth=0, font=button_font, command=self.exit)
        self.exit_button.place(x=10,y=0)

        self.settings_button = Button(self.top_frame, image=settings_image, borderwidth= 0, highlightthickness=0, command= lambda: self.go_to_frame("Settings"))
        self.settings_button.place(x=365,y=50)

        #self.settings_button = Button(self.top_frame, text="Settings", height=3, width=5, bg='orange', borderwidth= 0, command= lambda: self.go_to_frame("Settings"))
        #self.settings_button.place(x=370,y=50)

        


        ###settings frame####
        self.settings_frame = Frame(background='white', width=w_width, height=h_height)


        self.title_label = Label(self.settings_frame, text="Settings")
        self.title_label.pack()

        self.test_button = Button(self.settings_frame, text="test", height=3, width=3, bg="#FF851B")   

        #self.exit_button = Button(self.settings_frame, text="Exit", height=5, width=5, bg='white', command=self.exit)
        #self.exit_button.place(x=15,y=7)

        ###New recipie###


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

        print("CURRENT FRAME", self.current_frame)
        print("NEXT FRAME", next_frame)

        """ if self.current_frame == "Home":
            self.home_frame.pack_forget()
        elif self.current_frame == "Settings":
            self.settings_frame.pack_forget() """
        
        self.hide_all_frames()
       
        if next_frame == "Settings":
                self.settings_frame.pack()
                self.current_frame = "Settings"
        elif next_frame == "Home":
                self.home_frame.pack()
                self.current_frame = "Home"


    def hide_all_frames(self):
         self.home_frame.pack_forget()
         self.settings_frame.pack_forget()
         
    #def settings(self):
        #self.settings_frame


    def exit(self):
        self.window.destroy()

    
    #def home_open(self):
        #print("yes")


    #def new_rec(self):
        #print("123 fun fun fun")

    def save_note(self):
        note = self.note_entry.get("1.0", END)
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
        cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))

        messagebox.showinfo(title="Recipe saved!", message="Saved successfully!")
        conn.commit()
        conn.close()

    def new_rec(self):
         view_window = Toplevel(self.window)
         view_window.geometry("400x400")
         view_window.title("Test")

         
         self.note_entry = Text(view_window, height=20)
         self.note_entry.pack()

         
         self.save_button = Button(view_window, text="save note", command=self.save_note)
         self.save_button.pack()

         #recipe_name = Label(view_window, text="Recipe")
         #recipe_name.pack()

         view_window.mainloop()

    
 
        