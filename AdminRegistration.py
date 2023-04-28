from tkinter import *
from tkcalendar import DateEntry

def adminRegistration():
    
    window = Tk()
    window.geometry("1300x600+30+35")
    window.title("Admin Registration")
  
    fWindow = Frame(window, height = 600, width = 1300, background = "#F3B600")
    fWindow.pack()

    details = Label(fWindow, text = "Fill the New Admin's details", bg = "#F3B600", fg = "black", font = ("times new roman",30,"bold"))
    details.place(x = 424, y = 1)

    #All Labels

    lName = Label(fWindow, text = "Name", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lName.place(x = 80, y = 80)

    lDob = Label(fWindow, text = "Date of Birth", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lDob.place(x = 80, y = 124)

    lGender = Label(fWindow, text = "Gender", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lGender.place(x = 80, y = 168)

    lCaste = Label(fWindow, text = "Caste", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lCaste.place(x = 80, y = 212)

    lReligion = Label(fWindow, text = "Religion", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lReligion.place(x = 80, y =256)

    lAddress = Label(fWindow, text = "Address", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lAddress.place(x = 80, y = 300)

    lCity = Label(fWindow, text = "City", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lCity.place(x = 80, y = 344)

    lState = Label(fWindow, text = "State", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lState.place(x = 80, y = 388)

    lPin = Label(fWindow, text = "Pin", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lPin.place(x = 80, y = 432)

    #Labels in Right Side

    lCountry = Label(fWindow, text = "Country", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lCountry.place(x = 700, y = 80)

    lBranch = Label(fWindow, text = "Branch Name", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lBranch.place(x = 700, y = 124)

    lMobile = Label(fWindow, text = "Mobile No", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lMobile.place(x = 700, y = 168)

    lEmailId = Label(fWindow, text = "Email Id", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lEmailId.place(x = 700, y = 212)

    lPanNo = Label(fWindow, text = "PAN No", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lPanNo.place(x = 700, y = 256)

    lAadharNo = Label(fWindow, text = "Aadhar No", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lAadharNo.place(x = 700, y = 300)

    lAdminId = Label(fWindow, text = "Admin Id", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lAdminId.place(x = 700, y = 344)

    lNewPassword = Label(fWindow, text = "New Password", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lNewPassword.place(x = 700, y = 388)

    lConfromPassword = Label(fWindow, text = "Confrom Password", bg = "#F3B600", fg = "black", font = ("times new roman", 17, "bold"))
    lConfromPassword.place(x = 700, y = 432)



    #Define globalvariable for take input from entry
    '''
    gvName = StringVar()
    gvDob = StringVar()
    gvGender = StringVar()
    gvCaste = StringVar()
    gvReligion = StringVar()
    gvAddress = StringVar()
    gvCity = StringVar()
    gvState = StringVar()
    gvPin = StringVar()
    gvCountry = StringVar()
    gvBranchName = StringVar()
    gvMobileNo = StringVar()
    gvEmailId = StringVar()
    gvPanNo = StringVar()
    gvAadharNo = StringVar()
    gvAdminId = StringVar()
    gvNewPassword = StringVar()
    gvConfromPassword = StringVar()
    '''

    #All Entry boxes

    eName = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eName.place(x = 350, y = 80)

    eDob = DateEntry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eDob.place(x = 350, y = 124)

    eGender = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eGender.place(x = 350, y = 168)

    eCaste = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eCaste.place(x = 350, y = 212)

    eReligion = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eReligion.place(x = 350, y = 256)

    eAddress = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eAddress.place(x = 350, y = 300)

    eCity = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eCity.place(x = 350, y = 344)

    eState = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eState.place(x = 350, y = 388)

    ePin = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    ePin.place(x = 350, y = 432)

    #Entry box in Right Side

    eCountry = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eCountry.place(x = 970, y = 80)

    eBranchName = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eBranchName.place(x = 970, y = 124)

    eMobileNo = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eMobileNo.place(x = 970, y = 168)

    eEmailId = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eEmailId.place(x = 970, y = 212)

    ePanNo = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    ePanNo.place(x = 970, y = 256)

    eAadharNo = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eAadharNo.place(x = 970, y = 300)

    eAdminId = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eAdminId.place(x = 970, y = 344)

    eNewPassword = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eNewPassword.place(x = 970, y = 388)

    eConfromPassword = Entry(fWindow, bg = "ivory", border = 3, font = ("times new roman", 17, "bold"))
    eConfromPassword.place(x = 970, y = 432)

    '''
    user(name text, address text, city text, state text, zip text, country text,
    dob text pan text, aadhar text, email text,
    mobile text, account text, branch text, balance text,

    # not has === userId text, password 
    '''
    import sqlite3

    

    def submit():
        db = sqlite3.connect("BankDb.db")
        cr = db.cursor()
        if eNewPassword.get() == eConfromPassword.get():
            cr.execute("insert into admin(name, dob, gender, caste, religion, address, city, state, pin, country, branchName,mobileNo, emailId, panNo, aadharNo, adminId, password)values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ( eName.get(),  eDob.get(),  eGender.get(),  eCaste.get(),  eReligion.get(),  eAddress.get(),  eCity.get(),  eState.get(),  ePin.get(),  eCountry.get(),  eBranchName.get(), eMobileNo.get(),  eEmailId.get(),  ePanNo.get(),  eAadharNo.get(),  eAdminId.get(),  eNewPassword.get()))
        
            window.destroy()
            db.commit()
            db.close()
        else:
            from MsgBox import msgBox
            msgBox("New Password and Confrom Password must be same",650,1)
        
    bSubmit = Button(fWindow, text = "Submit", bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = submit)
    bSubmit.place(x = 595, y = 510)
    window.mainloop()

adminRegistration()