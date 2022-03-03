import tkinter as tk
from tkinter import *

r = tk.Tk()
r.geometry("500x200")
r.title('Counting Seconds')

def nextPage():
    r.destroy()
    import loginpage

user_name = Label(r, 
                  text = "CAR RENTAL").place(x = 230,
                                           y = 50)  
button = tk.Button(r, text='Login', width=25,command=nextPage).place(x = 170, y=100)

Button(
    r, 
    text="Login", 
    command=nextPage
    )
r.mainloop()