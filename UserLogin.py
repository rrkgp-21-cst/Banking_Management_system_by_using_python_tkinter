import sqlite3
from tkinter import *
from MsgBox import msgBox
from UserInterface import userInterface
from Otp import otp
from NewUser import newUser
from PIL import Image, ImageTk

def userLogin():

    db = sqlite3.connect("BankDB.db")
    cr = db.cursor()

    def submit():
        cr.execute("select accountNo from user where userId = ? and password = ?",(eUserId.get(), ePassword.get()))

        # if data is not found then cr.fetchall()[0][0] will generate error
        try:    
            accountNo = cr.fetchall()[0][0]
            window.destroy()
            userInterface(accountNo)
        except:
            msgBox("Invalid User Id or Password", 400, 1)
    
    def newAcc():
        #window.destroy()
        newUser()

    def forgetPassword():
        window.destroy()
        newUser()
                   
          

    window = Tk()
    window.title("User Login")
    window.geometry("540x450+400+125")
    window.maxsize(540, 450)
    window.minsize(540, 450)
    
    
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

    fWindow = Frame (window, background = "#F3B600", width = 1366, height = 680)
    fWindow.place(x = 0, y = 100)

    '''img = Image.open("login.jpg")
    rImg = img.resize((540,450))
    oImg = ImageTk.PhotoImage(rImg)

    fImg = Label(image = oImg, border=0)
    fImg.place(x = 0, y = 0)'''
    

    lUserId = Label(fWindow, text = "User Id", font = ("times new roman",20,"bold"), bg="#f3B600",fg = "black")
    lUserId.place(x = 70, y = 100)

    lPassword = Label(fWindow, text = "Password", font = ("times new roman", 20,"bold"),bg="#F3B600", fg = "black")
    lPassword.place(x = 70, y = 150)

    eUserId = Entry(fWindow, font = ("times new roman", 20,"bold"))
    eUserId.place(x = 200, y = 100)

    ePassword = Entry(fWindow,show="*", font = ("times new roman", 20,"bold"))
    ePassword.place(x = 200, y = 150)

    bForgotPassword = Button(fWindow, text = "Forget Password?", font = ("times new roman",  15,"bold"), bg = "#F3B600", fg = "red", border = 0, command = forgetPassword)
    bForgotPassword.place(x = 320, y = 190)

    bSubmit = Button(fWindow, text = "Login", bg = "black", fg = "white", font = ("times new roman", 18,"bold"), command = submit)
    bSubmit.place(x = 200, y = 220)#102762

    # lLine = Label(fWindow, text = "----OR----",font = ("times new roman",7), bg = "#F6F4F1", fg = "black")
    # lLine.place(x = 255, y = 270)

    bNewAcc = Button(nab, text = "New User", bg = "black", fg = "white", font = ("times new roman", 18,"bold"), command = newAcc)
    bNewAcc.place(x =400, y = 18)


    window.mainloop()


#userLogin()