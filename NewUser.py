import sqlite3
from tkinter import *
from MsgBox import msgBox
from Otp import otp
from tkcalendar import DateEntry


def newUser():
    db = sqlite3.connect("BankDB.db")
    cr = db.cursor()
        

    window = Tk()
    window.title("New User")
    window.geometry("560x470+390+125")
    window.minsize(560,470)
    window.maxsize(560,470)

    
    fWindow = Frame(window, width = 560, height = 470, bg = "#F3B600")
    fWindow.pack()


    Label(fWindow, text = "Name", bg = "#F3b600", fg = "black", font = ("times new roman", 20,"bold")).place(x = 50, y = 50)
    
    Label(fWindow, text = "Account No.", bg = "#F3b600", fg = "black", font = ("times new roman", 20,"bold")).place(x = 50, y = 100)

    Label(fWindow, text = "Date of Birth", bg = "#F3b600", fg = "black", font = ("times new roman", 20,"bold")).place(x = 50, y = 150)

    Label(fWindow, text = "Branch Name", bg = "#F3b600", fg = "black", font = ("times new roman", 20,"bold")).place(x = 50, y = 200)

    Label(fWindow, text = "Email Id", bg = "#F3b600", fg = "black", font = ("times new roman", 20,"bold")).place(x = 50, y = 250)

    Label(fWindow, text = "Mobile No.", bg = "#F3b600", fg = "black", font = ("times new roman", 20,"bold")).place(x = 50, y = 300)


    eName = Entry(fWindow, font = ("times new roman", 20,"bold"))
    eName.place(x = 220, y = 50)

    eAccountNo = Entry(fWindow, font = ("times new roman", 20,"bold"))
    eAccountNo.place(x = 220, y = 100)

    eDob = DateEntry(fWindow, font = ("times new roman", 20))
    eDob.place(x = 220, y = 150)

    eBranchName = Entry(fWindow, font = ("times new roman", 20,"bold"))
    eBranchName.place(x = 220, y = 200)

    eEmailId = Entry(fWindow, font = ("times new roman", 20,"bold"))
    eEmailId.place(x = 220, y = 250)

    eMobileNo = Entry(fWindow, font = ("times new roman", 20,"bold"))
    eMobileNo.place(x = 220, y = 300)

    def next():
        cr.execute("select name, accountNo, dob, emailId, mobileNo from user where accountNo = ?",(eAccountNo.get(),))
        userData = cr.fetchall()        
        
        # if data is not found then cr.fetchall()[0][0] will generate error that means account no is not exist in db
        if userData != []:
            if eName.get() == userData[0][0] and eDob.get() == userData[0][2] and eEmailId.get() == userData[0][3] and eMobileNo.get() == userData[0][4]:

                    window.destroy()
                    otp(userData[0][3], userData[0][1])

            else:
                    msgBox("Incorrect User's Details", 400, 1)

        else:
            msgBox("Invalid Account NO", 300, 1)
        
  

    Button(fWindow, text = "Next", bg = "Black", fg = "white", width = 8, font = ("times new roman", 20,"bold"), command = next).place(x = 225, y = 390)

    window.mainloop()

# newUser()
