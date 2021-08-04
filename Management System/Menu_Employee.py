from tkinter import *
from tkinter import ttk

import Register_student
import MarksManager
import FeesManager
import Manage_Attendance


class Employee_Menu:
    def __init__(self, root, ls, frame_old, frame_run):
        # Creating the first frame.
        self.frame_run = frame_run
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Labeling the page.
        self.title = Label(self.frame, text='Nirma University', font=('Algerian', 25, 'bold'), bg="#163148",
                           fg="#ffffff").pack(
            side=TOP)

        # Creating a second frame.
        self.frame2 = Frame(self.frame, bg='#ffffff')
        self.frame2.place(x=ls[0] // 9, y=ls[1] // 8, width=ls[0] // 9 * 7, height=ls[1] // 8 * 6)

        # Title for Register/Login.
        self.title1 = Label(self.frame2, text='Faculty management system', font=('Algerian', 22, 'bold'),
                            bg='#ffffff').pack(
            side=TOP)

        # Taking All pics in the variable.
        self.photo_new_student = PhotoImage(file=r"Images/New Student.png")
        self.photo_attendance = PhotoImage(file=r"Images/attendance.png")
        self.photo_marksheet = PhotoImage(file=r"Images/marksheet.png")
        self.photo_fees = PhotoImage(file=r"Images/fees.png")
        self.photo_exit = PhotoImage(file=r"Images/exit.png")

        # Resizing the Images as per requirement.
        self.photo_new_student = self.photo_new_student.subsample(7, 7)
        self.photo_attendance = self.photo_attendance.subsample(5, 5)
        self.photo_marksheet = self.photo_marksheet.subsample(5, 5)
        self.photo_fees = self.photo_fees.subsample(5, 5)
        self.photo_exit = self.photo_exit.subsample(5, 5)

        # Creating a Button Images.
        self.new_student_btn = Button(self.frame2, text='Manage Student', bd=0, bg='#fbf8e6', image=self.photo_new_student,
                              compound=TOP, command=self.Register) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9, y=ls[1] // 6)

        self.attendance = Button(self.frame2, text='Manage Attendance', bd=0, bg='#fbf8e6', image=self.photo_attendance,
                                 compound=TOP, command=self.ManageAttendance) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 3, y=ls[1] // 6)

        self.marksheet = Button(self.frame2, text='Manage Marks', bd=0, bg='#fbf8e6', image=self.photo_marksheet,
                                compound=TOP, command=self.Manage_Marks) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 5, y=ls[1] // 6)

        self.fees_btn = Button(self.frame2, text='Manage Fee Status', bd=0, bg='#fbf8e6', image=self.photo_fees,
                               compound=TOP, command=self.Manage_Fees) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 2, y=ls[1] // 6 * 3)

        self.Exit_btn = Button(self.frame2, text='Exit', bd=0, bg='#fbf8e6', image=self.photo_exit,
                               compound=TOP, command=self.exiting) \
            .place(width=ls[0] // 9 + 10, height=ls[1] // 6 + 10, x=ls[0] // 9 * 4, y=ls[1] // 6 * 3)

    def Manage_Marks(self):
        self.frame.place_forget()
        MarksManager.Class_Marks(self.root, self.ls, self.frame)
        pass

    def Manage_Fees(self):
        self.frame.place_forget()
        FeesManager.ClassFees(self.root, self.ls, self.frame)
        pass

    def ManageAttendance(self):
        self.frame.place_forget()
        Manage_Attendance.Class_Attendance(self.root, self.ls, self.frame)
        pass

    def Register(self):
        self.frame.place_forget()
        Register_student.Registration(self.root, self.ls, self.frame)
        pass

    def exiting(self):
        self.frame.place_forget()
        self.frame_run.destroy()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass

