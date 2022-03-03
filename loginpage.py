from tkinter import *
import tkinter as tk

import os
import urllib.parse as up
from click import password_option
import psycopg2 as psyco

""" up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["postgres://nunnuezw:O9gLgId1RahxEnc0X-jh76alUPSmYofs@jelani.db.elephantsql.com/nunnuezw"])
conn = psyco.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
) """

conn=psyco.connect(database = "gdqaunqg",user = "gdqaunqg",password = "Ftu_ftMT60OZSFCMFWhFKc8Cf0mHgVSd",host ="jelani.db.elephantsql.com",port = "5432")
cur = conn.cursor()
print("DATABASE CONNECTED")


from functools import partial

r = tk.Tk()
r.geometry("500x400")
r.title('Login Page')

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
    
def hosp():
    global f;global name;global specc;global amt;global cas;global op;global opno;global doc_name;global spec
    name=usern.get()
    n=str(name)
    passs=passw.get()
    print(passs);
    pa = str(passs)
    print(n);
    passwor=str(passs)
    cur.execute("insert into log values('"+n+"','"+pa+"')")
    print("TUPLE INSERTED SUCCESSFULLY")
    cur.execute("select * from log")
    f =cur.fetchall()
    print(f)
    conn.commit()
    conn.close()
    import CarMain
    r.destroy()




Label(
    r,
    text="USER LOGIN",
).place(x = 220,y = 100) 

#username label and text entry box
usernameLabel = Label(r, text="Username").grid(row=0, column=0)
usern = StringVar()
userna = str(usern)
usernameEntry = Entry(r, textvariable=usern).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(r,text="Password").grid(row=1, column=0)  
passw = StringVar()
passwo = str(passw)
passwordEntry = Entry(r, textvariable=passw, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, usern, passw)



#login button
loginButton = Button(r, text="Login", command=hosp).grid(row=4, column=0)

loginButton = Button(r, text="Register", command=hosp).grid(row=4, column=2)



r.mainloop()


