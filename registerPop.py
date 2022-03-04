import tkinter as tk
from tkinter import *

r = tk.Tk()
r.geometry("500x200")
r.title('Error')

def nextPage():
    r.destroy()

ser_name = Label(r, 
                  text = "USER ALREADY LOGGED IN!!!").place(x = 170,
                                           y = 80)  
button = tk.Button(r, text='OK', width=25,command=nextPage).place(x = 170, y=100)


r.mainloop()