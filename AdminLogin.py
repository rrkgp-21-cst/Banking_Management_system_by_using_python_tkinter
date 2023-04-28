from tkinter import *
import sqlite3
from PIL import Image, ImageTk


def adminLogin():


    def logIn():
        db = sqlite3.connect("BankDB.db")
        cr = db.cursor()
        lvAdminId = gvAdminId.get()
        lvPassword = gvPassword.get()
        cr.execute("select password from admin where adminId = ? and password = ?",(lvAdminId,lvPassword))
        password = str(cr.fetchall())
        if password[3:-4] == lvPassword and lvAdminId != "" and lvPassword != "":
            window.destroy() 
            db.close()
            from AdminInterface import adminInterface
            adminInterface(lvAdminId)  #change the place of  image at going > adminInterface > logout > homepage
        else:
            from MsgBox import msgBox
            msgBox("Invalid Admin Id or Password",450,1)
  
    def newAcc():
        from AdminRegistration import adminRegistration
        adminRegistration()

    window = Tk()
    window.title("Admin Login")
    window.geometry("540x450+400+125")
    window.maxsize(540,450)
    window.minsize(540,450)

    #header nab bar
    nab = Frame(window, bg = "#f3b600", width = 540, height = 100)
    nab.place(x = 0, y = 0)

    #Gitaram logo
    '''
    logo = PhotoImage(file = "4.png")
    logo = Label(image = logo)
    logo.place(x = 0, y = 18)
    '''
    logo = Image.open("./img/logo.png")
    rLogo = logo.resize((140,106))
    oLogo = ImageTk.PhotoImage(rLogo)

    fLogo = Label(image = oLogo, bg = "#f3b600")
    fLogo.place(x = 0, y = 0)

    lBankName = Label(nab,text = "ATLAS",bg = "#f3b600", fg = "black", font = ("algerian", 40, "bold"))
    lBankName.place(x = 140, y = 18)

    
    fWindow = Frame (window, background = "#F3B600", width = 540, height = 350)
    fWindow.place(x = 0, y = 100)

    lAdminId = Label(fWindow, text = "Admin Id",font = ("times new roman",20,"bold"), bg="#f3B600",fg = "black")
    lAdminId.place(x = 70, y = 100)

    lPassword = Label(fWindow, text = "Password",font = ("times new roman",20,"bold"), bg="#f3B600",fg = "black")
    lPassword.place(x = 70, y = 150)


    #Global variable for store user input
    gvAdminId = StringVar()
    gvPassword = StringVar()

    eAdminId = Entry(fWindow, font = ("times new roman", 20,"bold"),textvar = gvAdminId)
    eAdminId.place(x = 200, y = 100)

    ePassword = Entry(fWindow,show="*",font = ("times new roman", 20,"bold"),textvar = gvPassword)
    ePassword.place(x = 200, y = 150)


    bForgotPassword = Button(fWindow, text = "forget password",  font = ("times new roman",  15,"bold"), bg = "#F3B600", fg = "red", border = 0)
    bForgotPassword.place(x = 340, y = 190)

    bSubmit = Button(fWindow, text = "Login", bg = "black", fg = "white", font = ("times new roman", 18,"bold"), command = logIn)
    bSubmit.place(x = 200, y = 220)#102762


    # lLine = Label(fWindow, text = "----OR----",font = ("times new roman",7), bg = "#F6F4F1", fg = "black")
    # lLine.place(x = 255, y = 270)

    bNewAcc = Button(nab, text = "New Admin", bg = "black", fg = "white",width = 8, font = ("times new roman", 18,"bold"), command = newAcc)
    bNewAcc.place(x = 400, y = 18)



    window.mainloop()


#adminLogin()
