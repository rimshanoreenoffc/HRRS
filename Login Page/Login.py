from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk      #pip istall pillow 
from tkinter import messagebox


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #==========Background Image===========
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Administrator\Pictures\Saved Pictures\hotels.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #==========login frame===============
        frame=Frame(self.root,bg="white")
        frame.place(x=510,y=170, width=340,height=450)
        
        #=============user icon================
        img1=Image.open(r"C:\Users\Administrator\Pictures\Saved Pictures\5087607.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(frame,image=self.photoimg1,bg="white",borderwidth=0)
        lblimg1.place(x=120,y=10,width=100,height=100)

        
        #==============Get Started Label===========
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=95, y=100)

        #============username Label and entry=========== 
        username=lbl=Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username.place(x=70, y=155)
        self.txtuser=ttk.Entry(frame, font=("times new roman", 15,"bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # =============Password Label and Entry=============
        password=lbl= Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)
        

        #==========icon image============
        img2=Image.open(r"C:\Users\Administrator\Pictures\Saved Pictures\5087607.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="white",borderwidth=0)
        lblimg2.place(x=550,y=325,width=25,height=25)


        img3=Image.open(r"C:\Users\Administrator\Pictures\Saved Pictures\7570524.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="white",borderwidth=0)
        lblimg3.place(x=552,y=392,width=25,height=25)

        #login button
        loginbtn = Button(frame,command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="blue", activeforeground="white", activebackground="blue")
        loginbtn.place(x=110, y=300, width=120, height=35)

        #register button
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"),borderwidth=0, fg="black", bg="white", activeforeground="white", activebackground="white")
        registerbtn.place(x=15, y=350, width=160)

        #forget password button
        loginbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),borderwidth=0, fg="black", bg="white", activeforeground="white", activebackground="white")
        loginbtn.place(x=10, y=370, width=160)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif  self.txtuser.get()=="abc" and self.txtpass.get()=="123":
            messagebox.showinfo("Success","Welcome")
        else:
            messagebox.showerror("Invalid","Invalid username & password")






    
if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()