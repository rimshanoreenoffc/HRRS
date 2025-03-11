from tkinter import *
from PIL import Image,ImageTk     #pip install pillow
from tkinter import ttk

class RoomBooking:
    def __init__ (self,root):
        self.root = root
        self.root.title("Hotel Room Reservation System")
        self.root.geometry("1140x530+230+220")

    

        # =========title===============
        lbl_title = Label(self.root, text="Room Booking DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)


        # =========logo=========
        img2 = Image.open(r"C:\Users\Administrator\Pictures\Saved Pictures\gold-feather-hotel-logo-inspiration-grand-hotel-logo-stock-gold-feather-hotel-logo-inspiration-luxury-grand-hotel-logo-stock-169469900.webp")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        #===============labelFrame==============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #=============label and entries==============
        # custReference
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        enty_contact.grid(row=0,column=1)

        # Check_in Date
        check_in_date=Label(labelframeleft,text="Check_in Date",font=("arial", 12, "bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        # Check_Out Date
        lbl_Check_out=Label(labelframeleft,text="Check_Out Date",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

        # Room Type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial", 12, "bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)
        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available Rooms
        lblRoomAvailable=Label(labelframeleft,text="Available Room",font=("arial", 12, "bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

        # No Of Days
        lblNoOAfDays=Label(labelframeleft,text="No Of Days",font=("arial", 12, "bold"),padx=2,pady=6)
        lblNoOAfDays.grid(row=5,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        txtNoOfDays.grid(row=5,column=1)

        # Paid Tax
        lblNoOAfDays=Label(labelframeleft,text="Paid Tax:",font=("arial", 12, "bold"),padx=2,pady=6)
        lblNoOAfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        # Sub Total
        lblNoOAfDays=Label(labelframeleft,text="Sub Total",font=("arial", 12, "bold"),padx=2,pady=6)
        lblNoOAfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        # Total Cost
        lblIdNumber=Label(labelframeleft,text="Total Cost:",font=("arial", 12, "bold"),padx=2,pady=6)
        lblIdNumber.grid(row=8,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        txtIdNumber.grid(row=8,column=1)


        




if __name__ == "__main__":
    root = Tk()
    obj= RoomBooking(root)
    root.mainloop()    