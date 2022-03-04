import tkinter as tk
from tkinter import *
import psycopg2 as psyco

r = tk.Tk()
r.geometry("500x200")
r.title('RENT A CAR')



conn=psyco.connect(database = "gdqaunqg",user = "gdqaunqg",password = "Ftu_ftMT60OZSFCMFWhFKc8Cf0mHgVSd",host ="jelani.db.elephantsql.com",port = "5432")
cur = conn.cursor()
print("DATABASE CONNECTED")

def success():
    use=usern.get()
    n=str(use)
    nam=namen.get()
    na=str(nam)
    carna=carnamen.get()
    car=str(carna)
    phno=phonen.get()
    ph=str(phno)
    cur.execute("insert into car_rent values('"+n+"','"+na+"','"+car+"','"+ph+"')")
    print("TUPLE INSERTED SUCCESSFULLY")
    cur.execute("select * from car_rent")
    f =cur.fetchall()
    print(f)
    conn.commit()
    conn.close()
    r.destroy()
    import CarMain

usernameLabel = Label(r, text="USERNAME").grid(row=0, column=0)
usern = StringVar()
userna = str(usern)
usernameEntry = Entry(r, textvariable=usern).grid(row=0, column=1)
                                         
nameLabel = Label(r, text="NAME").grid(row=1, column=0)
namen = StringVar()
namena = str(namen)
nameEntry = Entry(r, textvariable=namen).grid(row=1, column=1)

carnameLabel = Label(r, text="CAR NAME").grid(row=2, column=0)
carnamen = StringVar()
carnamena = str(carnamen)
carnameEntry = Entry(r, textvariable=carnamen).grid(row=2, column=1)

phoneLabel = Label(r, text="PHONE NUMBER").grid(row=3, column=0)
phonen = StringVar()
phonena = str(phonen)
phoneEntry = Entry(r, textvariable=phonen).grid(row=3, column=1)

loginButton = Button(r, text="RENT", command=success).grid(row=4, column=0)


r.mainloop()