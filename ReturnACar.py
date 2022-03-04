import tkinter as tk
from tkinter import *
import psycopg2 as psyco

r = tk.Tk()
r.geometry("500x400")
r.title('RETURN A CAR')


conn=psyco.connect(database = "gdqaunqg",user = "gdqaunqg",password = "Ftu_ftMT60OZSFCMFWhFKc8Cf0mHgVSd",host ="jelani.db.elephantsql.com",port = "5432")
cur = conn.cursor()
print("DATABASE CONNECTED")



def returncar():

    global f;global name;global specc;global amt;global cas;global op;global opno;global doc_name;global spec
    cname = carw.get()
    cn = str(cname)
    cur.execute("select * from cars where carname='"+cn+"'")
    f =cur.fetchall()
    print(f)
    cur.execute("update cars set status='Availabe' where carname='"+cn+"'")
    conn.commit()
    conn.close()
    import CarMain
    return





usernameLabel = Label(r, text="USERNAME:").place(x = 150,y = 100)
usern = StringVar()
userna = str(usern)
usernameEntry = Entry(r, textvariable=usern).place(x = 220,y = 100)  

#password label and password entry box
carLabel = Label(r,text="CAR NAME:").place(x = 150,y = 130)  
carw = StringVar()
carwo = str(carw)
passwordEntry = Entry(r, textvariable=carw).place(x = 220,y = 130)  



loginButton = Button(r, text="RETURN", command=returncar).place(x = 220,y = 150)


r.mainloop()