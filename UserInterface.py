from tkinter import *
from PIL import Image, ImageTk
import sqlite3


def userInterface(accountNo):
    
    db = sqlite3.connect("BankDB.db")
    cr = db.cursor()
    
    #Fetching data from database
    cr.execute("select name, address, city, state, pin, country,dob, panNo, aadharNo, emailId, mobileNo, accountNo, branchName, openingBalance from user where accountNo = ?",(accountNo,))
    '''
    1.  cr returns that is  [('name', 'branch', 'balance')] 
    2.  store it in crReturn = cr.fetchall()
    3.  data = crReturn[0]  that is  ('name', 'branch', 'balance')
    4.  data[0] that is name
    '''
    crReturn = cr.fetchall()
    data = crReturn[0]
    
    #define function for display profile and account summmery AND logout
    def summery():
        fProfile.place_forget()
        sProfile.place_forget()
        fSummery.place(x = 250, y = 151)

    def profile():
        fSummery.place_forget()
        fProfile.place(x = 250, y = 151)
    
    def nextProfile():
        fProfile.place_forget()
        sProfile.place(x = 250, y = 151)
    
    def previousProfile():
        sProfile.place_forget()
        fProfile.place(x = 250, y = 151)

    def logOut():
        window.destroy()
        from HomePage import homePage
        homePage()
        '''
        from MsgBox import msgBox
        sure = msgBox("Are you sure to logout",400,2)
        if sure == True:
            window.destroy()
            from HomePage import homePage
            homePage()'''

    window = Tk()
    window.geometry("1000x652+200+30")
    window.maxsize(1000,652)
    window.minsize(1000,652)
    window.title("User Interface")
    fWindow = Frame(window, width = 1000, height = 650, bg = "ivory")
    fWindow.pack()

    fTop = Frame(fWindow, width = 1000, height = 100, bg = "blue")
    fTop.place(x = 0, y = 0)

    #insert image
    img = Image.open("logo.png")
    rImg = img.resize((130,106))
    logoImg = ImageTk.PhotoImage(rImg)
    logo = Label(fTop, image = logoImg, bg = "#F6F4F1")
    logo.place(x = 0, y = 0)

    lBankName = Label(fTop,text = "Atlas Bank",fg = "black", bg = "#F6F4F1", font = ("times new roman", 40, "bold"))
    lBankName.place(x = 135, y = 18)

    # Home page    
    hLogo = ImageTk.PhotoImage(Image.open("logo.png").resize((500,500)))

    Label(fWindow, image = hLogo, bg="ivory").place(x = 320, y = 150)

    Label(fWindow, text = "Welcome to the User Page", font = ("times new roman", 40, "bold"), bg = "ivory", fg = "blue").place(x = 280, y = 150)


    fLeft = Frame(fWindow, width = 200, height = 550, bg = "ivory")#, highlightbackground = "blue", highlightthickness = 2 
    fLeft.place(x = 0, y = 100)

    # welcome user
    fWelcome = Frame(fTop, height = 100, width = 350, bg = "blue")
    fWelcome.place(x = 650, y = 0)
    lWelcome = Label(fWelcome, text = "Welcome", bg = "blue", fg = "white", font = ("times new roman", 20, "bold"))
    lWelcome.place(relx=.5, rely=.3,anchor= CENTER)

    lUserName = Label(fWelcome, text = data[0], bg = "blue", fg = "white", font = ("times new roman", 20, "bold"))
    lUserName.place(relx = .5, rely = .7, anchor = CENTER)

    # frame for summery button------------------------------------------
    fSummery = Frame(fWindow, height = 450, width = 700, bg = "beige")

    # labels for name of database's data for summery button difference 50
    lName = Label(fSummery, text = "Name", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lName.place(x = 90, y = 135)

    lAccountNo = Label(fSummery, text = "Account No", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lAccountNo.place(x = 90, y = 185)

    lBranch = Label(fSummery, text = "Branch Name", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lBranch.place(x = 90, y = 235)

    lBalance = Label(fSummery, text = "Available Balance", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lBalance.place(x = 90, y = 285)

    # labels for display  database's data  for summery button
    dName = Label(fSummery, text = data[0], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dName.place(x = 340, y = 135)

    dAccountNo = Label(fSummery, text = data[11], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dAccountNo.place(x = 340, y = 185)

    dBranch = Label(fSummery, text = data[12], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dBranch.place(x = 340, y = 235)

    dBalance = Label(fSummery, text = data[13], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dBalance.place(x = 340, y = 285)

    #labels for profile first page------------------------------------------

    fProfile = Frame(fWindow, height = 450, width = 700, bg = "beige")

    # labels for name of database's data for profile first page--------------------------------
    lName = Label(fProfile, text = "Name", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lName.place(x = 90, y = 35)

    lAddress = Label(fProfile, text = "Address", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lAddress.place(x = 90, y = 85)

    lCity = Label(fProfile, text = "City", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lCity.place(x = 90, y = 135)

    lState = Label(fProfile, text = "State", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lState.place(x = 90, y = 185)
    
    lPin = Label(fProfile, text = "Pin", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lPin.place(x = 90, y = 235)

    lCountry = Label(fProfile, text = "Country", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lCountry.place(x = 90, y = 285)

    # labels for display  database's data  for profile in first page ---------------------
    dName = Label(fProfile, text = data[0], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dName.place(x = 340, y = 35)

    dAddress = Label(fProfile, text = data[1], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dAddress.place(x = 340, y = 85)

    dCity = Label(fProfile, text = data[2], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dCity.place(x = 340, y = 135)

    dState = Label(fProfile, text = data[3], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dState.place(x = 340, y = 185)

    dPin = Label(fProfile, text = data[4], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dPin.place(x = 340, y = 235)

    dCountry = Label(fProfile, text = data[5], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dCountry.place(x = 340, y = 285)

    # button for go next in profile
    bNext = Button(fProfile, text = "Next >", width = 10, bg = "blue", fg = "white", font = ("times new roman", 15, "bold"), command = nextProfile)
    bNext.place(x = 295, y = 370)

    #labels for profile second page------------------------------------------

    sProfile = Frame(fWindow, height = 450, width = 700, bg = "beige")

    # labels for name of database's data for profile second page--------------------------------
    lDob = Label(sProfile, text = "Date of Birth", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lDob.place(x = 90, y = 35)

    lPanNo = Label(sProfile, text = "PAN No", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lPanNo.place(x = 90, y = 85)

    lAadharNo = Label(sProfile, text = "Aadhar No", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lAadharNo.place(x = 90, y = 135)

    lEmailId = Label(sProfile, text = "Email Id", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lEmailId.place(x = 90, y = 185)
    
    lMobileNo = Label(sProfile, text = "Mobile No", bg = "beige", fg = "blue", font = ("times new roman", 15, "bold"))
    lMobileNo.place(x = 90, y = 235)


    # labels for display  database's data  for profile in second page ---------------------
    dDob = Label(sProfile, text = data[6], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dDob.place(x = 340, y = 35)

    dPanNo = Label(sProfile, text = data[7], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dPanNo.place(x = 340, y = 85)

    dAadharNo = Label(sProfile, text = data[8], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dAadharNo.place(x = 340, y = 135)

    dEmailId = Label(sProfile, text = data[9], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dEmailId.place(x = 340, y = 185)

    dMobileNo = Label(sProfile, text = data[10], width = 22, fg = "blue", bg = "white", relief = "sunken", font = ("times new roman", 15, "bold"))
    dMobileNo.place(x = 340, y = 235)

    # button for go previous in profile
    bPrevious = Button(sProfile, text = "< Previous", width = 10, bg = "blue", fg = "white", font = ("times new roman", 15, "bold"), command = previousProfile)
    bPrevious.place(x = 295, y = 370)

    #buttons in left frame
    bSummery = Button   ( fLeft, text = "A/C Summery",bg = "blue", fg = "white", width = 12, font = ("times new roman", 15, "bold"), command = summery)
    bSummery.place(x = 0, y = 100)

    bProfile = Button(fLeft, text = "Profile", bg = "blue", fg = "white", width = 12, font = ("times new roman", 15, "bold"), command = profile)
    bProfile.place(x = 0, y = 250)

    bLogOut = Button(fLeft, text = "Log Out", bg = "blue", fg = "white", width = 12, font = ("times new roman", 15, "bold"), command = 
    logOut)
    bLogOut.place(x = 0, y = 400)


    window.mainloop()

# userInterface(1)
