from tkinter import *
from tkinter import messagebox


#4
def enter():
    username = username_entry.get()
    password = Password_entry.get()
    if username == "Bogdan" and password == "123":
        messagebox.showinfo(title="Login", message="Login successful")
        old_window.destroy()
#5
        from window2 import new_window



    else:
        messagebox.showerror(title="Error login", message="Try again!")


old_window = Tk()

info_label = Label(old_window, text="Login profile", font=("Arial",25), fg="black", bg="light blue")
info_label.grid(row=0, column=0, columnspan=2)

#1
old_window.geometry("250x150")
old_window.title("Login Page")
old_window.config(background="light blue")
icon = PhotoImage(file="login.png")
old_window.iconphoto(True, icon)

#2
username_label = Label(old_window, text="Username", font=("Italic", 15), fg="black", bg="light blue")
username_label.grid(row=3, column=0)
username_entry = Entry(old_window)
username_entry.grid(row=3, column=1)
Password_label = Label(old_window, text="Password", font=("Italic", 15), fg="black", bg="light blue")
Password_label.grid(row=4, column=0)
Password_entry = Entry(old_window, show="*")
Password_entry.grid(row=4, column=1)

#3
enter_button = Button(old_window, text="Enter", command=enter)
enter_button.grid(row=5, column=0, columnspan=2)

old_window.mainloop()



