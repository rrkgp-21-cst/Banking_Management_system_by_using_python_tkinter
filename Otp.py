from tkinter import *
import random
import smtplib
from MsgBox import msgBox
from CreatePassword import createPassword

def otp(emailId, accountNo):

    otpWindow = Tk()
    otpWindow.geometry("450x450+390+125")
    otpWindow.minsize(450,450)
    otpWindow.maxsize(450,450)
    otpWindow.title("OTP")
    otpWindow.config(background="#f3b600")
    def sendOtp():
        try:
            global otp
            otp = "".join([str(random.randint(0,9)) for i in range(8)])

            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login("srbank02@gmail.com", "pverdkqiumtyiwhb")
            subject = "OTP"
            body = "Welcome to SR Bank \nYour OTP for is  "+str(otp)
            msg = "Subject: {}\n\n{}".format(subject, body)

            server.sendmail("srbank02@gmail.com", emailId, msg)
        except:
            msgBox("Check your internet connection", 400, 1)

    def submit():
        global authorize
        global tried
        if otp == eOtp.get():
            otpWindow.destroy()
            createPassword(accountNo, "User Id")
        else:
            try:
                tried += 1
            except:
                tried = 1

            if tried == 3:
                otpWindow.destroy()
                msgBox("You are not eligible",350,1)
            
            if tried != 3:
                msgBox("Invalid OTP", 300, 1)
            

    Label(otpWindow, text = "Enter the OTP that is send to your \nregistered Email Id", fg = "black", bg = "#f3b600", font = ("times new roamn", 15)).place(x = 80, y = 50)

    eOtp = Entry(otpWindow, font = ("times new roman",20))
    eOtp.place(x = 90, y = 130)

    bSendOtp = Button(otpWindow, text = "Send OTP", font = ("times new roman",  18,"bold"), fg = "black", bg = "#f3b600", border = 0, command = sendOtp).place(x = 165, y = 310)

    bSubmit = Button(otpWindow, text = "Submit",width = 8, bg = "black", fg = "white", font = ("times new roman", 20), command = submit).place(x = 160, y = 350)

    otpWindow.mainloop()





# otp("dassweety140@gmail.com",789456)