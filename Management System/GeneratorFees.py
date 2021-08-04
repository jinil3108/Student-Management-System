from tkinter import *
from tkinter import ttk


import sqlite3

class Class_Fees:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.roll=roll
        self.frame_old = frame_old

        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Fee Status Checker', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a top-Side Frame.
        Paid_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Paid_Frame.place(x=ls[0]//2-350, y=ls[1]//9*1+50, width=ls[0]*300//1336, height=ls[1]//9*2)

        # Creating a top-Side Frame.
        Rem_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Rem_Frame.place(x=ls[0] // 2 + 50, y=ls[1] // 9 * 1 + 50, width=ls[0]*300//1336, height=ls[1] // 9 * 2)

        # Creating a Bottom-Side Frame.
        Manage_Frame = Frame(self.frame, bd=1, relief=RIDGE, bg="cornsilk")
        Manage_Frame.place(x=ls[0]//2-400, y=ls[1]//7*4, width=ls[0]*800//1336, height=ls[1]//7*2)

        # Text Variable.
        self.Txt_fees = Label(Manage_Frame, anchor=CENTER, bg='cornsilk', font=("times new roman", 30))
        self.Txt_fees.pack(fill=BOTH, expand=1)

        # Text Variable.
        self.Txt_paid = Label(Paid_Frame, anchor=CENTER, text="Fees Paid", bg='lightblue',fg='red', font=("times new roman", 18))
        self.Txt_paid.place(x=0, y=ls[1]*50//714, width=ls[0]*300//1336-15)

        # Text Variable.
        self.Txt_rem = Label(Rem_Frame,anchor=CENTER, text="Fees Remaining", bg='lightblue',fg='red', font=("times new roman", 18))
        self.Txt_rem.place(x=0, y=ls[1]*50//714, width=ls[0]*300//1336-15)

        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM student_fees WHERE Roll_No= "+self.roll)

        rows = c.fetchall()

        if int(rows[0][1]) == 0:
            self.Txt_fees.config(text="Fees Data Not Available")
        else:
            if int(rows[0][2]) == 0:
                self.Txt_fees.config(text="Your current semester fees has been paid.")
            else:
                self.Txt_fees.config(text="Partial Fees Paid")

        # Creating the fees.
        self.fees_paid = Label(Paid_Frame,anchor=CENTER, text=str(rows[0][1]), bg='lightblue', font=("times new roman", 18))
        self.fees_paid.place(x=0, y=ls[1]*80//714, width=ls[0]*300//1336-15)

        # Creating the fees.
        self.fees_rem = Label(Rem_Frame,anchor=CENTER, text=str(rows[0][2]), bg='lightblue', font=("times new roman", 18))
        self.fees_rem.place(x=0, y=ls[1]*80//714, width=ls[0]*300//1336-15)


    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

