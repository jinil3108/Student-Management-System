from tkinter import *
from tkinter import ttk

import Login_Student
import Login_Employee

class Main_Page:
    def __init__(self, root, ls):
        self.root = root
        self.ls = ls
        # Creating the first frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0]//9*2, y=ls[1]//4, width=ls[0]//9*5, height=ls[1]//4*2)

        # Taking All pics in the variable.
        self.photo_student = PhotoImage(file=r"Images/student_img.png")
        self.photo_employee = PhotoImage(file=r"Images/employee.png")

        # Resizing the Images as per requirement.
        self.photo_student = self.photo_student.subsample(4, 4)
        self.photo_employee = self.photo_employee.subsample(4, 4)

        # Labeling the page.
        self.title = Label(self.frame, text='NIRMA UNIVERSITY', font=('Algerian', 25, 'bold'), bg='LightGreen').pack(
            side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='Register/Login', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(side=TOP)

        # Creating two buttons.
        self.student_btn = Button(self.frame1, text='Student', bd=0, bg='#ffffff', image=self.photo_student,
                                   compound=TOP, command=self.student) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9)*3-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)

        self.employee_btn = Button(self.frame1, text="Faculty", bd=0, bg='#ffffff', image=self.photo_employee,
                                   compound=TOP, command=self.employee) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9 * 5)-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)

    def student(self):
        self.frame.place_forget()
        student_menu = Login_Student.Student_Show(self.root, self.ls, self.frame)

    def employee(self):
        self.frame.place_forget()
        employee_menu = Login_Employee.Employee_Show(self.root, self.ls, self.frame)