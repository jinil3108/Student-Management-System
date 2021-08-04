from tkinter import *
from tkinter import ttk

import sqlite3



class Class_ID:
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
        title = Label(self.frame, text='ID-Card Generator', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.roll))

        rows = cur.fetchall()

        self.name = str(rows[0][1])
        self.email = str(rows[0][2])
        self.gender = str(rows[0][3])
        self.phone = str(rows[0][4])
        self.dob = str(rows[0][5])
        self.address = str(rows[0][6])

        # Generating Bar Code.
        from PIL import Image, ImageDraw, ImageFont
        image = Image.new('RGB', (1000, 600), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('arial.ttf', size=45)
        import qrcode

        # Nirma Tag
        (x, y) = (230, 40)
        message = "Nirma University"
        company = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=70)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 190)
        name = "Name: " + self.name
        color = 'rgb(0, 0, 0)'  # black color
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), name, fill=color, font=font)

        (x, y) = (50, 260)
        message = "Gender: " + self.gender
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 330)
        message = "Phone: " + self.phone
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 400)
        message = "DOB: " + self.dob
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 470)
        message = "Address: " + self.address
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), message, fill=color, font=font)

        # save the edited image

        image.save(str("id_card") + '.png')

        img = qrcode.make(str(company) + str(self.roll))  # this info. is added in QR code, also add other things
        img.save(str("id_card") + '.bmp')

        til = Image.open(str("id_card") + '.png')
        im = Image.open(str("id_card") + '.bmp')  # 25x25
        til.paste(im, (640, 160))
        til.save(str("id_card") + '.png')

        self.photo_ID_Card = PhotoImage(file=r"id_card.png").subsample(2,2)

        image_id = Label(self.frame, image=self.photo_ID_Card, bg="white")
        image_id.place(x=ls[0]*420//1336, y=ls[1]*260//714)

    def exiting(self):
        self.frame.destroy()
        self.root.title("Student Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

