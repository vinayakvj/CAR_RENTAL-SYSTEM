import tkinter as tk
from tkinter import *

r = tk.Tk()
r.geometry("500x200")
r.title('RENT A CAR')

""" bg = PhotoImage(file = "bg1.jpg") """

def nextPage():
    r.destroy()
    import loginpage

user_name = Label(r, 
                  text = "WELCOME TO CAR RENTAL SYSTEM").place(x = 163,
                                           y = 50)  
button = tk.Button(r, text='Login', width=25,command=nextPage).place(x = 170, y=100)

Button(
    r, 
    text="Login", 
    command=nextPage
    )
r.mainloop()