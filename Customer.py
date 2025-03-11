from tkinter import *
from PIL import Image,ImageTk     #pip install pillow
from tkinter import ttk



class Cust_Win:
    def __init__ (self,root):
        self.root = root
        self.root.title("Hotel Room Reservation System")
        self.root.geometry("1140x530+230+220")

        # ================Validation function for alphabets=============
        def validate_alphabets(input_text):
            return input_text.isalpha() or input_text == ""
        
        # =============Register validation function==============
        validate_alpha = self.root.register(validate_alphabets)



        # =========title===============
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)


        # =========logo=========
        img2 = Image.open(r"C:\Users\Administrator\Pictures\Saved Pictures\gold-feather-hotel-logo-inspiration-grand-hotel-logo-stock-gold-feather-hotel-logo-inspiration-luxury-grand-hotel-logo-stock-169469900.webp")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)


        #===============labelFrame==============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #=============label and entries==============
        # custReference
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,font=("arial", 13, "bold"),width=29)
        enty_ref.grid(row=0,column=1)

        # customer name
        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"), validate="key", validatecommand=(validate_alpha, "%P"))
        txtcname.grid(row=1, column=1)

        # father name
        lblmname = Label(labelframeleft, text="Father Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"), validate="key", validatecommand=(validate_alpha, "%P"))
        txtmname.grid(row=2, column=1)

        # gender combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial", 12, "bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,font=("arial", 12, "bold"), width=27,state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)


        # mobile number
        lblMobile=Label(labelframeleft,text="Mobile:",font=("arial", 12, "bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,width=29,font=("arial", 13, "bold"))
        txtMobile.grid(row=5,column=1)

        # email
        lblEmail=Label(labelframeleft,text="Email:",font=("arial", 12, "bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,width=29,font=("arial", 13, "bold"))
        txtMobile.grid(row=6,column=1)

        # nationality
        lblNationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        txtNationality = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"), validate="key", validatecommand=(validate_alpha, "%P"))
        txtNationality.grid(row=7, column=1)

        # address
        lblAddress=Label(labelframeleft,text="Address:",font=("arial:", 12, "bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,width=29,font=("arial", 13, "bold"))
        txtAddress.grid(row=10,column=1)


        #=============buttons=================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial", 12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial", 12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial", 12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial", 12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)


        #=============table frame================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman", 12, "bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial:", 12, "bold"),bg="Red",fg="White")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search= ttk.Combobox(Table_Frame,font=("arial", 12, "bold"),width=24,state="readonly")
        combo_Search["values"] = ("Mobile","mail")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        txtSearch=ttk.Entry(Table_Frame,width=24,font=("arial", 13, "bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",font=("arial", 12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial", 12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)


        #=================show data table==============
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name",
                                                                    "father","gender","mobile","email","nationality","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("father",text="Father Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("father",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)








if __name__ == "__main__":
    root = Tk()
    obj= Cust_Win(root)
    root.mainloop()    
