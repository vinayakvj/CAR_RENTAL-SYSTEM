from tkinter import *
import tkinter as tk

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
r.geometry("500x350")
r.title('Login Page')

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
    
def register():
    global f;global name;global specc;global amt;global cas;global op;global opno;global doc_name;global spec
    name=usern.get()
    n=str(name)
    passs=passw.get()
    print(passs);
    pa = str(passs)
    print(n);
    cur.execute("select * from log")
    f =cur.fetchall()
    print(f)
    for i in f:
        if i[0].strip() == n:
            import registerPop
    cur.execute("insert into log values('"+n+"','"+pa+"')")
    print("TUPLE INSERTED SUCCESSFULLY")
    conn.commit()
    conn.close()
    import CarMain
    r.destroy()

    return

def login():
    name = usern.get()
    na = str(name)
    cur.execute("select * from log")
    f = cur.fetchall()
    print(f)
    for i in f:
        if i[0].strip() == na:
            import CarMain
        else:
            import loginPop
    r.destroy()
    conn.commit()
    conn.close()

    return



Label(
    r,
    text="USER LOGIN",
).place(x = 210,y = 50)  

#username label and text entry box
usernameLabel = Label(r, text="USERNAME:").place(x = 150,y = 100)
usern = StringVar()
userna = str(usern)
usernameEntry = Entry(r, textvariable=usern).place(x = 220,y = 100)  

#password label and password entry box
passwordLabel = Label(r,text="PASSWORD:").place(x = 150,y = 130)  
passw = StringVar()
passwo = str(passw)
passwordEntry = Entry(r, textvariable=passw, show='*').place(x = 220,y = 130)  

validateLogin = partial(validateLogin, usern, passw)



#login button
loginButton = Button(r, text="Login", command=login).place(x = 150,y = 170)

loginButton = Button(r, text="Register", command=register).place(x = 275,y = 170)



r.mainloop()


