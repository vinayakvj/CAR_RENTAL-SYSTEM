from cmath import log
from distutils.sysconfig import customize_compiler
import tkinter as tk
from tkinter import *

r = tk.Tk()
r.geometry("500x400")
r.title('CUSTOMER DETAILS')




def Cust():
    r.destroy()
    import Customer
    

def Rute():
    r.destroy()
    import ReturnACar
    

def logOut():
    r.destroy()
    import loginpage
    

button = tk.Button(r, text='RENT A CAR', width=25,command=Cust).place(x = 170, y=100)

button = tk.Button(r, text='RETURN A CAR', width=25,command=Rute).place(x = 170, y=150)

button = tk.Button(r, text='LOG OUT', width=25,command=logOut).place(x = 170, y=200)

r.mainloop()