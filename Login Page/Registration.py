from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import DateEntry  # Install using `pip install tkcalendar`

class HotelRegistration:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Room Reservation")
        self.root.geometry("800x600+200+100")

        # Title
        title_label = Label(self.root, text="Hotel Room Reservation", font=("Arial", 20, "bold"), bg="blue", fg="white")
        title_label.pack(side=TOP, fill=X)

        # Frame for form
        form_frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        form_frame.place(x=50, y=70, width=700, height=500)

        # Name
        lbl_name = Label(form_frame, text="Full Name:", font=("Arial", 14), bg="white")
        lbl_name.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        self.entry_name = Entry(form_frame, font=("Arial", 14))
        self.entry_name.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        # Contact Number
        lbl_contact = Label(form_frame, text="Contact Number:", font=("Arial", 14), bg="white")
        lbl_contact.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        self.entry_contact = Entry(form_frame, font=("Arial", 14))
        self.entry_contact.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Email
        lbl_email = Label(form_frame, text="Email:", font=("Arial", 14), bg="white")
        lbl_email.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.entry_email = Entry(form_frame, font=("Arial", 14))
        self.entry_email.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # Room Type
        lbl_room_type = Label(form_frame, text="Room Type:", font=("Arial", 14), bg="white")
        lbl_room_type.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.combo_room_type = ttk.Combobox(form_frame, font=("Arial", 14), state="readonly")
        self.combo_room_type['values'] = ("Single", "Double", "Suite", "Deluxe")
        self.combo_room_type.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        self.combo_room_type.current(0)  # Default selection

        # Check-in Date
        lbl_checkin = Label(form_frame, text="Check-in Date:", font=("Arial", 14), bg="white")
        lbl_checkin.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        self.checkin_date = DateEntry(form_frame, font=("Arial", 14), date_pattern="yyyy-mm-dd", width=18)
        self.checkin_date.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # Check-out Date
        lbl_checkout = Label(form_frame, text="Check-out Date:", font=("Arial", 14), bg="white")
        lbl_checkout.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        self.checkout_date = DateEntry(form_frame, font=("Arial", 14), date_pattern="yyyy-mm-dd", width=18)
        self.checkout_date.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # Number of Guests
        lbl_guests = Label(form_frame, text="Number of Guests:", font=("Arial", 14), bg="white")
        lbl_guests.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        self.entry_guests = Entry(form_frame, font=("Arial", 14))
        self.entry_guests.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Buttons
        btn_register = Button(form_frame, text="Register", font=("Arial", 14, "bold"), bg="green", fg="white", command=self.register)
        btn_register.grid(row=7, column=0, pady=20, padx=20)

        btn_reset = Button(form_frame, text="Reset", font=("Arial", 14, "bold"), bg="red", fg="white", command=self.reset_form)
        btn_reset.grid(row=7, column=1, pady=20, padx=20)

    def register(self):
        # Gather data from fields
        name = self.entry_name.get()
        contact = self.entry_contact.get()
        email = self.entry_email.get()
        room_type = self.combo_room_type.get()
        checkin = self.checkin_date.get_date()
        checkout = self.checkout_date.get_date()
        guests = self.entry_guests.get()

        # Validate the inputs
        if not name or not contact or not email or not room_type or not guests:
            messagebox.showerror("Error", "All fields are required!")
            return

        if checkout <= checkin:
            messagebox.showerror("Error", "Check-out date must be after check-in date!")
            return

        # Confirm registration
        messagebox.showinfo("Success", f"Reservation Successful!\n\nDetails:\nName: {name}\nContact: {contact}\nEmail: {email}\nRoom: {room_type}\nGuests: {guests}\nCheck-in: {checkin}\nCheck-out: {checkout}")
        self.reset_form()

    def reset_form(self):
        # Reset all fields to default
        self.entry_name.delete(0, END)
        self.entry_contact.delete(0, END)
        self.entry_email.delete(0, END)
        self.combo_room_type.current(0)
        self.checkin_date.set_date("")
        self.checkout_date.set_date("")
        self.entry_guests.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = HotelRegistration(root)
    root.mainloop()














