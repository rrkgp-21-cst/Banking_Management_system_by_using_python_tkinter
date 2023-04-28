import sqlite3
from turtle import home
from MsgBox import msgBox
from tkinter import *
from main import homePage

def createPassword(uniqueId, candidate):
        t = Tk()
        t.title("Create User's Password")
        t.minsize(560,470)
        t.maxsize(560,470)
        fCreatePassword = Frame(t, width = 560, height = 470, bg = "beige")
        fCreatePassword.pack()

        db = sqlite3.connect("BankDb.db")
        cr = db.cursor()
         

        Label(fCreatePassword, text = '''Create User Id and password and password will contain atleast 
a number, a special character(like @, %) a uppercase and a
lowercase character and its mininum length is 6''', bg = "beige", fg = "blue", font = ("times new roman", 15)).place(x = 25, y = 20)
        
        Label(fCreatePassword, text = candidate, bg = "beige", fg = "blue", font = ("times new roman", 20)).place(x = 25, y = 120)

        Label(fCreatePassword, text = "New Password", bg = "beige", fg = "blue", font = ("times new roman", 20)).place(x = 25, y = 170)
    
        Label(fCreatePassword, text = "Confrom Password", bg = "beige", fg = "blue", font = ("times new roman", 20)).place(x = 25, y = 220)

        eid = Entry(fCreatePassword, font = ("times new roman", 20))
        eid.place(x = 245, y = 120)
        
        eNewPassword = Entry(fCreatePassword, font = ("times new roman", 20))
        eNewPassword.place(x = 245, y = 170)

        eConfromPassword = Entry(fCreatePassword, font = ("times new roman", 20))
        eConfromPassword.place(x = 245, y = 220)

        def create():
            newPass = eNewPassword.get()
            conPass = eConfromPassword.get()
            id = eid.get()
            if id != "":
                if newPass != "" and conPass != "":
                
                    if newPass == conPass:
                        upper = any(i.isupper() for i in newPass)
                        lower = any(i.islower() for i in newPass)
                        numeric = any(i.isnumeric() for i in newPass)
                        if newPass.isalnum() == False and upper and lower and numeric and len(newPass) >= 6:
                            if candidate == "User Id":
                                cr.execute("select accountNo from user where userId = ?",(id,))
                                if cr.fetchall() == []:
                                    cr.execute("update user set userId = ? where accountNo = ?",(id,uniqueId))
                                    cr.execute("update user set password = ? where accountNo = ?",(newPass,uniqueId))
                                    db.commit()
                                    t.destroy()
                                    msgBox('''Your Id and Password is 
created successfully now you
can login using your id and
password''',400,1,200)
                                    
                                    
                                    homePage()
                                else:
                                    msgBox("User Id is exist",300,1)
                            '''elif candidate == "Admin Id":
                                cr.execute("select adminId from admin where adminId = ?",(id,))
                                if cr.fetchall() == []:
                                    pass
                                else:
                                    msgBox("Admin Id is exist",300,1)'''
                        else:
                            msgBox("Weak password",300,1)
                    else:
                        msgBox('''New Password and Confrom
Password must be same''',400,1,150)
                else:
                    msgBox('''New password or Confrom 
Password can not be Blank''',400,1,150)
            else:
                msgBox("User Id can not be blank",350,1)      
        
        Button(fCreatePassword, text = "Create", bg = "blue", fg = "white", width = 8, font = ("times new roman", 20), command = create).place(x = 225, y = 390)
        
        t.mainloop()
       



#createPassword("2", "User Id")