from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3
import Menu_Employee

class Employee_Show:
    def __init__(self,root,ls,frame_old):
        self.frame_old = frame_old
        self.root = root
        self.ls = ls

        # Creating the variable.
        self.id_var = StringVar()
        self.password_var = StringVar()

        # Creating the first frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0] // 7 * 2, y=ls[1] // 4, width=ls[0] // 7 * 3, height=ls[1] // 4 * 2)

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the page.
        self.title = Label(self.frame, text='NIRMA UNIVERSITY', font=('Algerian', 25, 'bold'), bg='LightGreen').pack(
            side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='Faculty Login', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(
            side=TOP)

        # Label Login
        lbl_id = Label(self.frame1, text="Id: ", bg="white", fg="blue", font=("times new roman",15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*127//714)

        txt_id = Entry(self.frame1, textvariable=self.id_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*130//714)

        # Label Login
        lbl_id = Label(self.frame1, text="Password: ", bg="white", fg="blue", font=("times new roman", 15))
        lbl_id.place(x=ls[0]*130//1336, y=ls[1]*197//714)

        txt_id = Entry(self.frame1, textvariable=self.password_var, font=("times new roman", 12), bd=2,
                       relief=GROOVE)
        txt_id.place(x=ls[0]*230//1336, y=ls[1]*200//714)

        # Submit Button
        self.fees_btn = Button(self.frame1, text='Login', bd=0, bg='black',fg='white',font=("times new roman", 15),
                               compound=TOP, command=self.new_page)
        self.fees_btn.place(x=ls[0]*250//1336, y=ls[1]*300//714)

    def new_page(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM employee_login where id=" + str(self.id_var.get()))

        rows = cur.fetchall()
        if len(rows) != 0:
            if str(self.password_var.get()) == str(rows[0][1]):
                firster = Menu_Employee.Employee_Menu(self.root, self.ls, self.frame_old, self.frame)
            else:
                messagebox.showerror("Error", "Wrong Password, Please Input Valid Password.")
        else:
            messagebox.showerror("Error", "No such employee found!!!")
        pass

    def exiting(self):
        self.frame.place_forget()
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
        pass