from tkinter import *
from tkinter import ttk
# import HomePage
import ctypes
import sqlite3

class Class_Attendance:
    def __init__(self, root, ls, frame_old):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()
        self.var_radio = IntVar()
        self.flag1 = 0
        self.flag2 = 0

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Attendence Generator', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a top-Side Frame.
        Roll_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg='LightBlue')
        Roll_Frame.place(x=ls[0] // 2 - 200, y=ls[1] // 7 * 1, width=ls[0]*400//1336, height=ls[1] // 7 * 2)

        # Creating a Bottom-Side Frame.
        self.Manage_Frame = Frame(self.frame, bd=1, relief=RIDGE, bg="cornsilk")
        self.Manage_Frame.place(x=ls[0] // 2 - 400, y=ls[1] // 7 * 4, width=ls[0]*800//1336, height=ls[1] // 7 * 2)

        # Labeling And Roll_No
        lbl_roll = Label(Roll_Frame, text="Enter Your Roll No.", bg="LightBlue", fg="RED",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=25, padx=70, sticky="w")

        # Text Box For Roll_No.
        txt_Roll = Entry(Roll_Frame, width=20, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=2, column=0, pady=0, padx=105, sticky="w")

        # Button
        CheckBtn = Button(Roll_Frame, text="Check It!!", bg='black', fg='white', width=10, command=self.Attendance)
        CheckBtn.grid(row=3, column=0, pady=20, padx=150, sticky="w")
        # -----------

    def Attendance(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.Roll_No_var.get()))

        rows = cur.fetchall()

        if len(rows) != 0:
            def sel():
                selection = "You selected the option " + str(self.var_radio.get())

            if self.flag1 == 0:
                if self.flag2 == 0:
                    self.lbl = Label(self.Manage_Frame, text="Mark Present/Absent ", bg="cornsilk", fg="red",
                                 font=("times new roman", 16, "bold"))
                    self.lbl.place(x=self.ls[0]*300//1336, y=self.ls[1]*10//714)

                    self.present = Radiobutton(self.Manage_Frame, text="Present", bg="cornsilk", variable=self.var_radio,
                                           value=1,
                                           command=sel, font=("times new roman", 16))
                    self.present.place(x=self.ls[0]*350//1336, y=self.ls[1]*35//714)

                    self.Absent = Radiobutton(self.Manage_Frame, text="Absent", bg="cornsilk", variable=self.var_radio,
                                          value=2,
                                          command=sel, font=("times new roman", 16))
                    self.Absent.place(x=self.ls[0]*350//1336, y=self.ls[1]*75//714)

                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                     command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*350//1336, y=self.ls[1]*130//714)
                    self.flag1 = 1
                else:
                    self.Attendence.destroy()
                    self.lbl = Label(self.Manage_Frame, text="Mark Present/Absent ", bg="cornsilk", fg="red",
                                     font=("times new roman", 16, "bold"))
                    self.lbl.place(x=self.ls[0]*300//1336, y=self.ls[1]*10//714)

                    self.present = Radiobutton(self.Manage_Frame, text="Present", bg="cornsilk",
                                               variable=self.var_radio,
                                               value=1,
                                               command=sel, font=("times new roman", 16))
                    self.present.place(x=self.ls[0]*350//1336, y=self.ls[1]*35//714)

                    self.Absent = Radiobutton(self.Manage_Frame, text="Absent", bg="cornsilk", variable=self.var_radio,
                                              value=2,
                                              command=sel, font=("times new roman", 16))
                    self.Absent.place(x=self.ls[0]*350//1336, y=self.ls[1]*75//714)

                    # Insert Button
                    self.ok_btn = Button(self.Manage_Frame, text="OK", bg='black', fg='white', width=10,
                                         command=self.ok_fun)
                    self.ok_btn.place(x=self.ls[0]*350//1336, y=self.ls[1]*130//714)
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
                    self.lbl.place_forget()
                    self.present.place_forget()
                    self.Absent.place_forget()
                    self.ok_btn.place_forget()
                    self.Attendence = Label(self.Manage_Frame, text="Roll Number Does not Exist", anchor=CENTER,
                                            bg='cornsilk', font=("times new roman", 30))
                    self.Attendence.pack(fill=BOTH, expand=1)
                    self.flag2 = 1
                    self.flag1 = 0
            elif self.flag2 == 1:
                pass
        pass

    def ok_fun(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()
        c.execute("SELECT * FROM student_attendance WHERE roll_no = "+str(self.Roll_No_var.get()))
        rows = c.fetchall()
        att = int(self.var_radio.get()) - 1

        if att==0:
            present = int(rows[0][1]) + 1
            total = int(rows[0][2]) + 1
            print(present, total)
            c.execute(f"UPDATE student_attendance SET present={present}, total={total} WHERE roll_no = " + str(self.Roll_No_var.get()))
            # Update both
        else:
            total = int(rows[0][2]) + 1
            c.execute(f"UPDATE student_attendance SET total={total} WHERE roll_no = " + str(
                self.Roll_No_var.get()))

        self.var_radio.set(0)
        conn.commit()
        conn.close()
        pass

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

