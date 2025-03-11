from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk      #pip install pillow
from tkinter import messagebox



class register:
   def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

      ###############bg image################
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Administrator\Pictures\Saved Pictures\hotels.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)








if __name__ =="__main__":
    root = Tk()
    app=register(root)
    root.mainloop() 