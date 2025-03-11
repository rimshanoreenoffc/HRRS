from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk      #pip install pillow
from tkinter import messagebox



class register:
   def _init_(self, root):
       
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #############variables#############
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        


           
           

            ###############bg image################
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SE\Pictures\Saved Pictures\360_F_355607062_zYMS8jaz4SfoykpWz5oViRVKL32IabTP.jpg")


        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)



         ###############left image################
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\SE\Pictures\Saved Pictures\images.jpeg")


        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=50)




        #========== main frame===============
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100, width=800,height=550)

        

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)


        ###############lable and entries ##############

        #---------------row1
        fname=Label(frame,text="First Name",font=("times new roman", 15, "bold"),bg="white")
        fname.place(x=50,y=100)

        self_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        self_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("timous new roman",15,"bold"),bg="ehite",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("timous new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)


        #------------------row2

        contact=Label(frame,text="Contact No",font=("timous new roman",15,"bold"),bg="ehite",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("timer new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("timous new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("timous new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        #--------------row3

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)


        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)



        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("timous new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #---------------row4
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("timous new roman",15))
        self.txt_pswd.place(x=370,y=270,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("timous new roman",15))
        self.txt_confirm_pswd.place(x=370,y=270,width=250)


        ##############checkbutton###############
        self.var_check=IntVar
        checkbtn=Checkbutton(frame,variable=self.var_check_check,text="I Agree The Terms & Condition",font=("times new roman",15,"bold"),ownvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #################buttons#################
        img=Image.open(r"C:\Users\SE\Pictures\Saved Pictures\register button.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"C:\Users\SE\Pictures\Saved Pictures\login-button-blue-i8.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)


        ###################function declaration ###############
        
        def register_data(self):
            if self.var_fname.grt()==""or self.var_email.get()==""or self.var_securityQ.get=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_pass()!=self.var_confpass.get():
                messagebox.showerror("Error","password & confirm password must be same")
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and condition")
            else:
                messagebox.showinfo("Success","Welcome friends")

    



if __name__=="__main__":
    root=Tk()
    app=register(root)
    root.mainloop()


