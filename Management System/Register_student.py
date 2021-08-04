from tkinter import *
from tkinter import ttk

import sqlite3


class Registration:
    def __init__(self, root, ls, frame_old2):
        self.frame_old2 = frame_old2
        self.root = root
        self.ls = ls

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='Student Management System', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        # Assigning the variables.
        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Phone_var = StringVar()
        self.DOB_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Creating a Left-side Frame
        Manage_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="lightblue")
        Manage_Frame.place(x=ls[0]*20//1336, y=ls[1]*100//714, width=ls[0]*450//1336, height=ls[1]*580//714)

        # Labeling a manage frame.
        m_title = Label(Manage_Frame, text="Manage Students", bg="lightpink", fg="blue",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # Create a roll Number, name, email, and all things like form.
        lbl_roll = Label(Manage_Frame, text="Roll No", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 12), bd=2,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame, width=15, textvariable=self.Gender_var, font=("times new roman", 12),
                                    state="readonly")
        combo_Gender['values'] = ("Male", "Female", "Others")
        combo_Gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_Phone = Label(Manage_Frame, text="Phone", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_Phone.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Phone = Entry(Manage_Frame, textvariable=self.Phone_var, font=("times new roman", 12), bd=2,
                          relief=GROOVE)
        txt_Phone.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="LightBlue", fg="RED", font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, textvariable=self.DOB_var, font=("times new roman", 12), bd=2, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address",bg="LightBlue", fg="RED",
                            font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Manage_Frame, width=30, height=3, font=("", 10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Creating a second frame.
        btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        btn_frame.place(x=ls[0]*15//1336, y=ls[1]*500//714, width=ls[0]*420//1336)

        Addbtn = Button(btn_frame, text="ADD",bg='black',fg='white', width=10, command=self.add_data).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_frame, text="UPDATE",bg='black',fg='white', width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="DELETE",bg='black',fg='white', width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_frame, text="CLEAR",bg='black',fg='white', width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
        Detail_Frame.place(x=ls[0]*490//1336, y=ls[1]*100//714, width=ls[0]*830//1336, height=ls[1]*580//714)

        lbl_search = Label(Detail_Frame, text="Search By", bg="cornsilk", fg="blue",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.search_by, font=("times new roman", 12, "bold"), state="readonly")
        combo_search['values'] = ("Name", "Roll_No", "Phone")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame, width=20, textvariable=self.search_txt, font=("times new roman", 12, "bold"), bd=2, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(Detail_Frame, text="Search", command=self.search_data, width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Detail_Frame, text="Show All", command=self.fetch, width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="cornsilk")
        Table_Frame.place(x=ls[0]*10//1336, y=ls[1]*70//714, width=ls[0]*760//1336, height=ls[1]*500//714)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,
                                     columns=("Roll", "Name", "Email", "Gender", "Phone", "DOB", "Address"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll", text="Roll NO.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Phone", text="Phone")
        self.Student_table.heading("DOB", text="DOB")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Phone", width=100)
        self.Student_table.column("DOB", width=100)
        self.Student_table.column("Address", width=200)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch()
        pass

    def add_data(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("INSERT INTO student_data VALUES (?,?,?,?,?,?,?)",(self.Roll_No_var.get(),
                                                                 self.Name_var.get(),
                                                                 self.Email_var.get(),
                                                                 self.Gender_var.get(),
                                                                 self.Phone_var.get(),
                                                                 self.DOB_var.get(),
                                                                 self.txt_address.get('1.0',END)
                                                                 ))

        c.execute("INSERT INTO student_fees VALUES (?,?,?)", (self.Roll_No_var.get(), '0', '0'))
        c.execute("INSERT INTO student_attendance VALUES (?,?,?)", (self.Roll_No_var.get(), '0', '0'))
        conn.commit()
        self.fetch()
        self.clear()
        conn.close()

    def fetch(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cursor()

        c.execute("SELECT * FROM student_data")
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
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Phone_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("UPDATE student_data SET name='{}', email='{}', gender='{}', phone='{}', DOB='{}', Address='{}' where Roll_no= {}"
                    .format(self.Name_var.get(),
                            self.Email_var.get(),
                            self.Gender_var.get(),
                            self.Phone_var.get(),
                            self.DOB_var.get(),
                            self.txt_address.get("1.0", END),
                            self.Roll_No_var.get()
        ))

        conn.commit()
        self.fetch()
        self.clear()
        conn.close()

    def delete_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM student_data where Roll_No = "+ self.Roll_No_var.get())
        cur.execute("DELETE FROM student_fees where Roll_No = " + self.Roll_No_var.get())
        cur.execute("DELETE FROM student_attendance where Roll_No = " + self.Roll_No_var.get())
        conn.commit()
        conn.close()
        self.fetch()
        self.clear()

    def search_data(self):
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where " + str(self.search_by.get()) + " LIKE '%" + str(
            self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Gender_var.set("")
        self.DOB_var.set("")
        self.txt_address.delete("1.0", END)
        self.Email_var.set("")
        self.Name_var.set("")
        self.Phone_var.set("")

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old2.place(x=0, y=0, width=self.ls[0], height=self.ls[1])
