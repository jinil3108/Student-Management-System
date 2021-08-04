from tkinter import *
from tkinter import ttk

import HomePage

if __name__ == '__main__':
    # Getting the screensize in list.
    ls = list([1336, 714])
    #print(ls)
    # Creating a fixed window.
    root = Tk()
    background_image = PhotoImage("Images/logo.jpg")
    background_label = Label(root, image=background_image)
    background_label.place(x=170, y=40, relwidth=1, relheight=1)

    # Creating a bit icon.
    root.iconbitmap("logo.ico")

    # Title and Screen Setting.
    root.title("Student Management System")  # Sets-up the title of the window.
    root.geometry(f"{ls[0]}x{ls[1]}+0+0")  # Width Height Left-padding Top-padding.
    root.minsize(ls[0], ls[1])  # Locking min-sized window.
    root.maxsize(ls[0], ls[1])  # Locking max-sized window.
    root.configure(bg='#163148')  # Setting the background.

    # Starting the first window.
    firster = HomePage.Main_Page(root, ls)

    # Starting a main window.
    root.mainloop()
