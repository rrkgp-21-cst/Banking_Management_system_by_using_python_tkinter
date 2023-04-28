from tkinter import *
from PIL import Image, ImageTk
 

def homePage():
    def adminLogin():
        window.destroy()
        from AdminLogin import adminLogin
        adminLogin()

    def userLogin():
        window.destroy()
        from UserLogin import userLogin
        userLogin()
    

    window = Tk()
    window.geometry("1000x650+200+30")

    window.maxsize(1000,650)
    window.minsize(1000,650)


    window.title("Banking Management System")
    window.config(background = "ivory")


    #header nab bar
    nab = Frame(window, bg = "#f3b600", width = 1000, height = 100)
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

    #ulogimg = PhotoImage(file = r"./image/UserLogin.png")
    bAdminLogin = Button(nab, relief=RAISED,text = "Admin Login", bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = adminLogin)
    #bAdminLogin = Button(nab,relief=FLAT, borderwidth=0, image=ulogimg,bg='#f3b600', command = adminLogin)
    bAdminLogin.place(x = 794, y = 25)

    bUserLogin = Button(nab, text = "User Login", bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = userLogin)
    bUserLogin.place(x = 614, y = 25)
    
    #Create Image
    img = Image.open("./img/homepage.png")
    rImg = img.resize((1000,550))
    oImg = ImageTk.PhotoImage(rImg)

    fImg = Label(image = oImg, border=0)
    fImg.place(x = 0, y = 100)


    window.mainloop()

if __name__ == '__main__':
    homePage()
