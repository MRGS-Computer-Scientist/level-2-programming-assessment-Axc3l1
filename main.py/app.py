from tkinter import *
from tkinter import ttk, messagebox
#from app_settings import *
from os import *
from PIL import ImageTk, Image
import sqlite3

from googletrans import Translator
import data as d
import custom as cs

w_width = 414
h_height = 816

bg_color = "#FF851B"

button_font=("airel", 20, "bold")
fun_font=("airel", 15, "bold")

class App():

    current_frame = "Home"
    


    def __init__(self):

        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(h_height))
        self.window.title("Dish Lister")


        

        self.top_frame = Frame(background='orange', width=w_width, height= 75)
        self.top_frame.pack(side='top')
    
        image = Image.open('imgs\logo.png')
        photo = ImageTk.PhotoImage(image.resize((450, 135)))

        settings_icon = Image.open("imgs\cog_image.png")
        settings_image = ImageTk.PhotoImage(settings_icon.resize((50,50)))

        home_icon = Image.open("imgs\home.png")
        home_image= ImageTk.PhotoImage(home_icon.resize((50,50)))
      


        self.home_frame = Frame(background=bg_color, width=w_width, height=h_height)






        self.title_label = Label(self.home_frame, text="Home")
        self.title_label.pack()

        bg_image = Label(self.top_frame, image=photo)
        bg_image.pack()

        self.bottom_frame = Frame(background=bg_color, width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')



        self.view_button = Button(self.bottom_frame, text="View Recipies", height=3, width=15, bg="#FF851B", borderwidth=0, font=fun_font, command=self.view_notes)
        self.view_button.place(x=65,y=15)

        self.newrecipie_button = Button(self.bottom_frame, text="New Recipie", height=3, width=10, bg="#FF851B", font=button_font, borderwidth=0, command=self.new_rec)
        self.newrecipie_button.place(x=230,y=0)

        self.home_button = Button(self.top_frame, image=home_image, borderwidth= 0, highlightthickness=0, command= lambda: self.go_to_frame("Home"))
        self.home_button.place(x=-5,y=50)

        self.exit_button = Button(self.bottom_frame, text="Exit", height=3, width=3, bg="#FF851B", borderwidth=0, font=button_font, command=self.exit)
        self.exit_button.place(x=10,y=0)

        self.settings_button = Button(self.top_frame, image=settings_image, borderwidth= 0, highlightthickness=0, command= lambda: self.go_to_frame("Settings"))
        self.settings_button.place(x=365,y=50)



        


        ###settings frame####
        self.settings_frame = Frame(background='white', width=w_width, height=h_height)


        self.title_label = Label(self.settings_frame, text="Settings")
        self.title_label.pack()



        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'images/')

        print("the path is", self.filename)


         
        

        self.window.mainloop()


    #this function checks if the next frame is settings and if it is it changes to the settings frame or if the next frame is home it changes to the home frame
    def go_to_frame(self, next_frame):



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
         
 


    def exit(self):
        self.window.destroy()

   


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
         view_window.title("Recipe Notes")
         

         
         self.currLang = StringVar()
         self.currLang.set("Not Detected")
         # Label: For showing the name of detected language
         self.detectedLang = Label(view_window, 
         textvariable=self.currLang, font=(cs.font3, 20), 
         bg='white')
         self.detectedLang.place(x=5, y=325)

         self.note_entry = Text(view_window, height=20)
         self.note_entry.pack()

         
         self.save_button = Button(view_window, text="Save Note", command=self.save_note)
         self.save_button.pack()

         self.translate_button = Button(view_window, text="Translate", command = self.Translator)                           
         self.translate_button.pack()

         text = StringVar()
         self.toLang = ttk.Combobox(view_window, textvariable=text, 
         font=(cs.font1, 15))
         self.toLang['values'] = d.lang_list
         self.toLang.current(0)
         self.toLang.place(x=100, y=375)

         







         view_window.mainloop()


    #opens a window where the user inputs their notes and opens another window with their translated notes
    def Translator(self):
        view_window = Toplevel(self.window)
        view_window.geometry("400x400")
        view_window.title("Notes Translation")

        self.note_translation = Text(view_window, height =20)
        self.note_translation.pack()

        try:
            fromText = self.note_entry.get("1.0", "end-1c")

            # Instance of Translator class
            translator = Translator()

            dest_lang = self.toLang.get()

            if dest_lang == '':
                messagebox.showwarning("Nothing has chosen!", "Please Select a Language")
            else:
                if fromText != '':
                    langType = translator.detect(fromText)

                    # Translating the text
                    result = translator.translate(fromText, dest=dest_lang)

                    self.currLang.set(d._languages[langType.lang.lower()])
                    
                    self.note_translation.delete("1.0", END)

                    self.note_translation.insert(INSERT, result.text)
        except Exception:
            messagebox.showerror("Error!")


    #opens up a new window where the notes you have saved are
    def view_notes(self):
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()
        conn.close()
                
        view_window = Toplevel()
        view_window.title("View Notes")
        view_text = Text(view_window)
        for note in notes:
            view_text.insert(END, note[1] + "\n")
        view_text.pack()




