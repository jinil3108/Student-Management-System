from tkinter import *
from tkinter import ttk

import sqlite3


class Class_Marks:
    def __init__(self, root, ls, frame_old):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()
        self.search_txt = StringVar()

        # Creating Subject Variable.
        self.Subject_1 = StringVar()
        self.Subject_2 = StringVar()
        self.Subject_3 = StringVar()
        self.Subject_4 = StringVar()
        self.Subject_5 = StringVar()
        self.Subject_6 = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Manage Student Marks', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Creating a Left-side Frame
        Manage_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="lightblue")
        Manage_Frame.place(x=ls[0]*20//1336, y=ls[1]*100//714, width=ls[0]*450//1336, height=ls[1]*580//714)

        # Labeling a manage frame.
        m_title = Label(Manage_Frame, text="Manage Students", bg="lightpink", fg="blue",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # Create a roll Number, name, email, and all things like form.
        lbl_roll = Label(Manage_Frame, text="Roll No", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_sub1 = Label(Manage_Frame, text="Data Structures: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub1.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_sub1 = Entry(Manage_Frame, textvariable=self.Subject_1, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_sub1.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_sub2 = Label(Manage_Frame, text="Digital Electronics: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub2.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_sub2 = Entry(Manage_Frame, textvariable=self.Subject_2, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_sub2.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_sub3 = Label(Manage_Frame, text="Discrete Mathematics: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub3.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_sub3 = Entry(Manage_Frame, textvariable=self.Subject_3, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_sub3.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_sub4 = Label(Manage_Frame, text="Principle of Economics: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub4.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_sub4 = Entry(Manage_Frame, textvariable=self.Subject_4, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_sub4.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_sub5 = Label(Manage_Frame, text="Object Oriented Prog.: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub5.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_sub5 = Entry(Manage_Frame, textvariable=self.Subject_5, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_sub5.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_sub6 = Label(Manage_Frame, text="Digital Communication: ", bg="LightBlue", fg="RED", font=("times new roman", 14, "bold"))
        lbl_sub6.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_sub6 = Entry(Manage_Frame, textvariable=self.Subject_6, font=("times new roman", 12), bd=2, relief=GROOVE)
        txt_sub6.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Creating a second frame.
        btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        btn_frame.place(x=ls[0]*15//1336, y=ls[1]*500//714, width=ls[0]*420//1336)

        Addbtn = Button(btn_frame, text="ADD", bg='black', fg='white', width=10, command=self.add_data).grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=10,
                                                                                                             pady=10)
        updatebtn = Button(btn_frame, text="UPDATE", bg='black', fg='white', width=10, command=self.update_data).grid(
            row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="DELETE", bg='black', fg='white', width=10, command=self.delete_data).grid(
            row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_frame, text="CLEAR", bg='black', fg='white', width=10, command=self.clear).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=10,
                                                                                                              pady=10)

        Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
        Detail_Frame.place(x=ls[0]*490//1336, y=ls[1]*100//714, width=ls[0]*830//1336, height=ls[1]*580//714)

        lbl_search = Label(Detail_Frame, text="Search By", bg="cornsilk", fg="blue",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame, width=20, textvariable=self.search_txt, font=("times new roman", 12, "bold"),
                           bd=2, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,column=3, padx=10, pady=10)
        showall_btn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch).grid(row=0, column=4, padx=10, pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        Table_Frame.place(x=ls[0]*10//1336, y=ls[1]*70//714, width=ls[0]*760//1336, height=ls[1]*500//714)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,
                                          columns=("Roll", "DSA", "D.E.", "D.M.", "POE", "OOPs", "D.C."),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll", text="Roll NO.")
        self.Student_table.heading("DSA", text="DSA")
        self.Student_table.heading("D.E.", text="D.E.")
        self.Student_table.heading("D.M.", text="D.M.")
        self.Student_table.heading("POE", text="POE")
        self.Student_table.heading("OOPs", text="OOPs")
        self.Student_table.heading("D.C.", text="D.C.")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("DSA", width=100)
        self.Student_table.column("D.E.", width=100)
        self.Student_table.column("D.M.", width=100)
        self.Student_table.column("POE", width=100)
        self.Student_table.column("OOPs", width=100)
        self.Student_table.column("D.C.", width=100)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch()

    def add_data(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("SELECT * FROM student_data WHERE roll_no= "+self.Roll_No_var.get())

        rows = c.fetchall()

        if len(rows)!=0:
            c.execute("INSERT INTO student_marks VALUES (?,?,?,?,?,?,?)", (self.Roll_No_var.get(),
                                                                          self.Subject_1.get(),
                                                                          self.Subject_2.get(),
                                                                          self.Subject_3.get(),
                                                                          self.Subject_4.get(),
                                                                          self.Subject_5.get(),
                                                                          self.Subject_6.get()
                                                                          ))
            conn.commit()
            self.fetch()
            self.clear()
            conn.close()
            pass
        else:
            #Message Box.
            pass

    def fetch(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("SELECT * FROM student_marks")
        rows = c.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.Subject_1.set(row[1])
        self.Subject_2.set(row[2])
        self.Subject_3.set(row[3])
        self.Subject_4.set(row[4])
        self.Subject_5.set(row[5])
        self.Subject_6.set(row[6])

    def update_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("UPDATE student_marks SET english='{}', mathematics='{}', social_science='{}', sanskrit='{}', gujarati='{}', science='{}' where Roll_no= {}"
                    .format(self.Subject_1.get(),
                            self.Subject_2.get(),
                            self.Subject_3.get(),
                            self.Subject_4.get(),
                            self.Subject_5.get(),
                            self.Subject_6.get(),
                            self.Roll_No_var.get()
        ))

        conn.commit()
        self.fetch()
        self.clear()
        conn.close()

    def delete_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM student_marks where Roll_No = " + self.Roll_No_var.get())
        conn.commit()
        conn.close()
        self.fetch()
        self.clear()

    def clear(self):
        self.Roll_No_var.set("")
        self.Subject_1.set("")
        self.Subject_2.set("")
        self.Subject_3.set("")
        self.Subject_4.set("")
        self.Subject_5.set("")
        self.Subject_6.set("")

    def search_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_marks where Roll_No LIKE '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

