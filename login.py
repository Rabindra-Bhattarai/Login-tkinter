from tkinter import *
from tkinter import messagebox


def on_submit():
    messagebox.showinfo("Success", "You have successfully Login.")
#     password=e1.get()
#     conform_password=e2.get()
#     if password==conform_password:
#         messagebox.showinfo("Success", "You have successfully Login.")
#     else:
#         messagebox.showerror("Error", "Incorrect Password.")

Login=Tk()

Login.title("Log in")
Login.iconbitmap("D:\\python\\logo.ico")
Login.geometry("600x300")

title=Label(Login, text="Hospital Management", width=20, font=("bold",20))
title.grid(row=0, column=1)

name=Label(Login,text="Email or Username").grid(row=5, column=0)
e1=Entry(Login).grid(row=5, column=1)


Password=Label(Login,text="Password").grid(row=25, column=0)
e1=Entry(Login).grid(row=25, column=1)




submit=Button(Login, text="Log in", command=on_submit).grid(row=35, column=1)
submit=Button(Login, text="Forgot Password?").grid(row=40, column=1)
submit=Button(Login, text="Create New Id").grid(row=55, column=1)


Login.mainloop()
