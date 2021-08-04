from tkinter import *
from tkinter import ttk

import sqlite3


class ClassFees:
    def __init__(self, root, ls, frame_old):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.flag2 = 0
        self.flag1 = 0

        self.Roll_No_var = StringVar()
        self.search_txt = StringVar()
        self.fees_paid = StringVar()
        self.fees_rem = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Manage Student Fees', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a top-Side Frame.
        Roll_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Roll_Frame.place(x=ls[0] // 2 - 200, y=ls[1] // 7 * 1, width=ls[0] * 400 // 1336, height=ls[1] // 7 * 2)

        # Creating a Bottom-Side Frame.
        self.Manage_Frame = Frame(self.frame, bd=1, relief=RIDGE, bg="cornsilk")
        self.Manage_Frame.place(x=ls[0] // 2 - 400, y=ls[1] // 7 * 4, width=ls[0] * 800 // 1336, height=ls[1] // 7 * 2)

        # Labeling And Roll_No
        lbl_roll = Label(Roll_Frame, text="Enter Your Roll No.", bg="LightBlue", fg="RED",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=25, padx=70, sticky="w")

        # Text Box For Roll_No.
        txt_Roll = Entry(Roll_Frame, width=20, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=2, column=0, pady=0, padx=105, sticky="w")

        # Button
        CheckBtn = Button(Roll_Frame, text="Check It!!", bg='black', fg='white', width=10, command=self.Fees)
        CheckBtn.grid(row=3, column=0, pady=20, padx=150, sticky="w")
        # -----------

    def Fees(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.Roll_No_var.get()))

        rows = cur.fetchall()

        if len(rows) != 0:
            if self.flag1 == 0:
                if self.flag2 == 0:
                    # Paid Fees Part
                    self.Frame_paid = Frame(self.Manage_Frame, bg='cornsilk')
                    self.Frame_paid.place(x=0,y=0,width=(self.ls[0] * 800 // 1336)//2-5, height=150)

                    # Fees Remaining.
                    # Paid Fees Part
                    self.Frame_rem = Frame(self.Manage_Frame, bg='cornsilk')
                    self.Frame_rem.place(x=(self.ls[0] * 800 // 1336)//2+5, y=0, width=(self.ls[0] * 800 // 1336) // 2-5, height=150)

                    # Labeling And Text.
                    self.lbl_paid = Label(self.Frame_paid,anchor=CENTER, text="Enter Fees Paid",font=("times new roman", 16), bg='cornsilk', fg='blue')
                    self.lbl_paid.place(x=0,y=0,width=(self.ls[0] * 800 // 1336)//2-5, height=75)

                    # Labeling And Text.
                    self.lbl_paid = Label(self.Frame_rem, anchor=CENTER, text="Enter Fees Remaining",font=("times new roman", 16), bg='cornsilk', fg='blue')
                    self.lbl_paid.place(x=0, y=0, width=(self.ls[0] * 800 // 1336) // 2 - 5, height=75)

                    # Text Paid.
                    self.txt_paid = Entry(self.Frame_paid,textvariable=self.fees_paid, font=("times new roman", 14))
                    self.txt_paid.place(x=self.ls[0]*115//1336,y=self.ls[1]*78//714,width=self.ls[0]*175//1336)

                    # Text Rem.
                    self.txt_rem = Entry(self.Frame_rem,textvariable=self.fees_rem, font=("times new roman", 14))
                    self.txt_rem.place(x=self.ls[0]*115//1336, y=self.ls[1]*78//714, width=self.ls[0] * 175 // 1336)

                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                     command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*360//1336, y=self.ls[1]*170//714)
                    self.flag1 = 1
                else:
                    self.Attendence.destroy()
                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                         command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*360//1336, y=self.ls[1]*170//714)
                    self.flag1 = 1
                    self.flag2 = 0
            elif self.flag1 == 1:
                pass
        else:
            if self.flag2 == 0:
                if self.flag1 == 0:
                    self.Attendence = Label(self.Manage_Frame,text="Roll Number Does not Exist", anchor=CENTER, bg='cornsilk', font=("times new roman", 30))
                    self.Attendence.pack(fill=BOTH, expand=1)
                    self.flag2 = 1
                else:
                    self.Attendence = Label(self.Manage_Frame, text="Roll Number Does not Exist", anchor=CENTER,
                                            bg='cornsilk', font=("times new roman", 30))
                    self.Attendence.pack(fill=BOTH, expand=1)
                    self.flag2 = 1
                    self.flag1 = 0
            elif self.flag2 == 1:
                pass

    def ok_fun(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM student_fees WHERE roll_no = " + str(self.Roll_No_var.get()))
        rows = c.fetchall()
        if int(self.fees_paid.get())>=0 and int(self.fees_rem.get())>=0:
            c.execute(f"UPDATE student_fees SET fees_paid={self.fees_paid.get()}, fees_rem={int(self.fees_rem.get())} WHERE roll_no = " + str(
                self.Roll_No_var.get()))
        conn.commit()
        conn.close()
        self.Frame_paid.place_forget()
        self.Frame_rem.place_forget()
        self.ok_btn.place_forget()
        pass

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
