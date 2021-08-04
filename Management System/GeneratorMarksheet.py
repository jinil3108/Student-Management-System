from tkinter import *
from tkinter import ttk

import sqlite3


class Class_Marksheet:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.roll = roll
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Marksheet Generator', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a Main-side Frame
        Manage_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="lightblue")
        Manage_Frame.place(x=ls[0]*430//1336, y=ls[1]*100//714, width=ls[0]*450//1336, height=ls[1]*580//714)


        # Database
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_marks where Roll_No= "+self.roll)

        rows = cur.fetchall()

        self.sub1 = rows[0][1]
        self.sub2 = rows[0][2]
        self.sub3 = rows[0][3]
        self.sub4 = rows[0][4]
        self.sub5 = rows[0][5]
        self.sub6 = rows[0][6]
        flag=0


        # Label Nirma
        uni_labl = Label(Manage_Frame, anchor=CENTER, bg='lightblue', text='Nirma University', font=('Algerian', 20))
        uni_labl.pack(side=TOP,fill=X)

        # Creating the Sr. No.
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Sr No.", font=('Times New Roman', 18))
        srl_lbl.place(x=ls[0]*30//1336,y=ls[1]*100//714)

        # Creating the subject tag.
        name_lbl = Label(Manage_Frame, bg='lightblue', text="Subject", font=('Times New Roman', 18))
        name_lbl.place(x=ls[0]*175//1336, y=ls[1]*100//714)

        # Creating the marks_lbl.
        marks_lbl = Label(Manage_Frame, bg='lightblue', text="Marks", font=('Times New Roman', 18))
        marks_lbl.place(x=ls[0]*320//1336, y=ls[1]*100//714)


        # Creating the Sr. No.1
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="1", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*140//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Data Structures", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*140//1336, y=ls[1]*140//714)

        sub1_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub1, font=('Times New Roman', 16))
        sub1_lbl.place(x=ls[0]*335//1336, y=ls[1]*140//714)

        if int(self.sub1) < 33:
            flag=1
            sub1_lbl.config(fg='red')


        # Creating the Sr. No.2
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="2", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*180//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Digital Electronics", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*130//1336, y=ls[1]*180//714)

        sub2_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub2, font=('Times New Roman', 16))
        sub2_lbl.place(x=ls[0]*335//1336, y=ls[1]*180//714)

        if int(self.sub2) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        # Creating the Sr. No.3
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="3", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*220//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Discrete Mathematics", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*120//1336, y=ls[1]*220//714)

        sub3_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub3, font=('Times New Roman', 16))
        sub3_lbl.place(x=ls[0]*335//1336, y=ls[1]*220//714)

        if int(self.sub3) < 33:
            flag=1
            sub1_lbl.config(fg='red')


        # Creating the Sr. No.4
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="4", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*260//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Principle Of Economics", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*110//1336, y=ls[1]*260//714)

        sub4_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub4, font=('Times New Roman', 16))
        sub4_lbl.place(x=ls[0]*335//1336, y=ls[1]*260//714)

        if int(self.sub4) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        # Creating the Sr. No.5
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="5", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*300//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Object Oriented Prog.", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*120//1336, y=ls[1]*300//714)

        sub5_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub5, font=('Times New Roman', 16))
        sub5_lbl.place(x=ls[0]*335//1336, y=ls[1]*300//714)

        if int(self.sub5) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        # Creating the Sr. No.6
        srl_lbl = Label(Manage_Frame, bg='lightblue', text="6", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*35//1336, y=ls[1]*340//714)

        srl_lbl = Label(Manage_Frame, bg='lightblue', text="Digital Communication", font=('Times New Roman', 16))
        srl_lbl.place(x=ls[0]*110//1336, y=ls[1]*340//714)

        sub6_lbl = Label(Manage_Frame, bg='lightblue', text=self.sub6, font=('Times New Roman', 16))
        sub6_lbl.place(x=ls[0]*335//1336, y=ls[1]*340//714)

        if int(self.sub6) < 33:
            flag=1
            sub1_lbl.config(fg='red')

        total = int(self.sub1) + int(self.sub2) + int(self.sub3) + int(self.sub4) +int(self.sub5) +int(self.sub6)

        total_lbl = Label(Manage_Frame, bg='lightblue', text="Total", font=('Times New Roman', 16))
        total_lbl.place(x=ls[0]*285//1336, y=ls[1]*390//714)

        total_lbl = Label(Manage_Frame, bg='lightblue', text=total, font=('Times New Roman', 16))
        total_lbl.place(x=ls[0]*335//1336, y=ls[1]*390//714)

        if flag==1:
            total_lbl.config(text="IF", fg='red')

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

