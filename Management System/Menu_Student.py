from tkinter import *
from tkinter import ttk

import GeneratorID
import GeneratorMarksheet
import GeneratorAttendance
import GeneratorFees


class Student_Menu:
    def __init__(self, root, ls, frame_old, frame_run, roll):
        # Creating the first frame.
        self.ls = ls
        self.root = root
        self.roll = roll
        self.frame_old = frame_old
        self.frame_run = frame_run
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Labeling the page.
        self.title = Label(self.frame, text='Nirma University', font=('Algerian', 25, 'bold'), bg="#163148", fg="#ffffff").pack(
            side=TOP)

        # Creating a second frame.
        self.frame2 = Frame(self.frame, bg='#ffffff')
        self.frame2.place(x=ls[0]//9, y=ls[1]//8, width=ls[0]//9*7, height=ls[1]//8*6)

        # Title for Register/Login.
        self.title1 = Label(self.frame2, text='student management system', font=('Algerian', 22, 'bold'), bg='#ffffff').pack(
            side=TOP)

        # Taking All pics in the variable.
        self.photo_ID_Card = PhotoImage(file=r"Images/IDCard.png")
        self.photo_attendance = PhotoImage(file=r"Images/attendance.png")
        self.photo_marksheet = PhotoImage(file=r"Images/marksheet.png")
        self.photo_fees = PhotoImage(file=r"Images/fees.png")
        self.photo_exit = PhotoImage(file=r"Images/exit.png")

        # Resizing the Images as per requirement.
        self.photo_ID_Card = self.photo_ID_Card.subsample(11, 11)
        self.photo_attendance = self.photo_attendance.subsample(5, 5)
        self.photo_marksheet = self.photo_marksheet.subsample(5, 5)
        self.photo_fees = self.photo_fees.subsample(5, 5)
        self.photo_exit = self.photo_exit.subsample(5, 5)

        # Creating a Button Images.
        self.ID_card = Button(self.frame2, text='Generate ID Card', bd=0, bg='#fbf8e6', image=self.photo_ID_Card, compound=TOP, command=self.IDGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1]//6+10, x=ls[0]//9, y=ls[1] // 6)

        self.attendance = Button(self.frame2, text='Show Attendance', bd=0, bg='#fbf8e6', image=self.photo_attendance,
                              compound=TOP, command=self.AttendanceGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9*3, y=ls[1] // 6)

        self.marksheet = Button(self.frame2, text='Show Marksheet', bd=0, bg='#fbf8e6', image=self.photo_marksheet,
                                 compound=TOP, command=self.MarksheetGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9 * 5, y=ls[1] // 6)

        self.fees_btn = Button(self.frame2, text='Fee Status', bd=0, bg='#fbf8e6', image=self.photo_fees,
                                 compound=TOP, command=self.FeesGenerator) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9 * 2, y=ls[1] // 6*3)

        self.Exit_btn = Button(self.frame2, text='Exit', bd=0, bg='#fbf8e6', image=self.photo_exit,
                                compound=TOP, command=self.exiting) \
            .place(width=ls[0] // 9+10, height=ls[1] // 6+10, x=ls[0] // 9 * 4, y=ls[1] // 6*3)

    def FeesGenerator(self):
        self.frame.place_forget()
        GeneratorFees.Class_Fees(self.root, self.ls, self.frame, self.roll)

    def AttendanceGenerator(self):
        self.frame.place_forget()
        GeneratorAttendance.Class_Attendance(self.root, self.ls, self.frame, self.roll)

    def IDGenerator(self):
        self.frame.place_forget()
        GeneratorID.Class_ID(self.root, self.ls, self.frame, self.roll)

    def MarksheetGenerator(self):
        self.frame.place_forget()
        GeneratorMarksheet.Class_Marksheet(self.root, self.ls, self.frame, self.roll)

    def exiting(self):
        self.frame.place_forget()
        self.frame_run.destroy()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass

