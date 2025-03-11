from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        # ============== Variables =============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()


        #=============== Background Image===============
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Administrator\Pictures\Saved Pictures\pexels-dkux-932320.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ===============Left Image===========
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Administrator\Pictures\Saved Pictures\pngtree-clipart-of-beautiful-young-girl-using-laptop-png-image_13125436.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        #================Main Frame ===============
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        register_lbl.place(x=20, y=20)

        # ============== Labels and Entries==============

        # --------------- Row 1 ---------------
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # --------------- Row 2 ---------------
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # --------------- Row 3 ---------------
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Favourite Team", "Your Favorite Food")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA ,font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # --------------- Row 4 ---------------
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass ,font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ================ Checkbutton ================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check, text="I Agree The Terms & Conditions",font=("times new roman", 12, "bold"), onvalue=1, offvalue=0, bg="white")
        checkbtn.place(x=50, y=380)

        # =================== Buttons ================
        img = Image.open(r"C:\Users\Administrator\Pictures\Saved Pictures\register-now-button-sign-key-push-vector-31008182.jpg")
        img = img.resize((200, 70), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,  command=self.register_data,image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=50, y=420, width=200)

        img1 = Image.open(r"C:\Users\Administrator\Pictures\Saved Pictures\login-button-blue-i8.jpg")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1,borderwidth=0, cursor="hand2")
        b2.place(x=370, y=420, width=200)

        # ============= Function Declaration ==============
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='PEARL',database='mydata')
            my_cursor=conn.cursor()
            Query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(Query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register(fname, lname, contact, email, securityQ, securityA, password) values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.var_fname.get(),
                                                                                  self.var_lname.get(),
                                                                                  self.var_contact.get(),
                                                                                  self.var_email.get(),
                                                                                  self.var_securityQ.get(),
                                                                                  self.var_securityA.get(),
                                                                                  self.var_pass.get()
                                                                                        ))
                
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

        
        
        
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()