from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
from MsgBox import msgBox

def userRegistration():
        # create list for add in Dob value
        dd = [str(i) for i in range(1,32)]
        mm = [str(i) for i in range(1,13)]
        yy = [str(i) for i in range(2022,1900,-1)]

        db = sqlite3.connect("BankDb.db")
        cr = db.cursor()

        window = Tk()
        window.geometry("1300x680+30+5")
        window.title("Open New User's Account")

        fWindow = Frame(window, height = 680, width = 1300, background = "#F3B600")
        fWindow.pack()

        details = Label(fWindow, text = "Fill the New User's details", bg = "#f3b600", fg = "Black", font = ("times new roman",30,"bold"))
        details.place(x = 424, y = 1)

        #All Labels

        lName = Label(fWindow, text = "Name", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lName.place(x = 80, y = 80)

        lGuardianName = Label(fWindow, text = "Guardian Name", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lGuardianName.place(x = 80, y = 124)

        lRelationWithGuardian = Label(fWindow, text = "Relation with Guardian", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lRelationWithGuardian.place(x = 80, y = 168)

        lDob = Label(fWindow, text = "Date of Birth", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lDob.place(x = 80, y = 212)

        lGender = Label(fWindow, text = "Gender", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lGender.place(x = 80, y = 256)

        lMaritalStatus = Label(fWindow, text = "Marital Status", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lMaritalStatus.place(x = 80, y = 300)

        lCaste = Label(fWindow, text = "Caste", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lCaste.place(x = 80, y = 344)

        lReligion = Label(fWindow, text = "Religion", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lReligion.place(x = 80, y = 388)

        lAddress = Label(fWindow, text = "Address", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lAddress.place(x = 80, y = 432)

        lCity = Label(fWindow, text = "City", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lCity.place(x = 80, y = 476)

        lState = Label(fWindow, text = "State", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lState.place(x = 80, y = 520)

        lPin = Label(fWindow, text = "Pin", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lPin.place(x = 80, y = 564)

        #Labels in Right Side

        lCountry = Label(fWindow, text = "Country", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lCountry.place(x = 700, y = 80)

        lAnnualIncome = Label(fWindow, text = "Annual Income", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lAnnualIncome.place(x = 700, y = 124)

        lOccupation = Label(fWindow, text = "Occupation", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lOccupation.place(x = 700, y = 168)
        
        lBranch = Label(fWindow, text = "Branch Name", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lBranch.place(x = 700, y = 212)

        lBalance = Label(fWindow, text = "Opening Balance", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lBalance.place(x = 700, y = 256)

        lAccount = Label(fWindow, text = "Account No", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lAccount.place(x = 700, y = 300)

        lAccountType = Label(fWindow, text = "Account Type", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lAccountType.place(x = 700, y = 344)

        lCustomerId = Label(fWindow, text = "Customer Id", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lCustomerId.place(x = 700, y = 388)

        lMobile = Label(fWindow, text = "Mobile No", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lMobile.place(x = 700, y = 432)

        lEmailId = Label(fWindow, text = "Email Id", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lEmailId.place(x = 700, y = 476)

        lPanNo = Label(fWindow, text = "PAN No", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lPanNo.place(x = 700, y = 520)

        lAadharNo = Label(fWindow, text = "Aadhar No", bg = "#f3b600", fg = "black", font = ("times new roman", 17, "bold"))
        lAadharNo.place(x = 700, y = 564)


        #All Entry boxes

        eName = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eName.place(x = 350, y = 80)

        eGuardianName = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eGuardianName.place(x = 350, y = 124)

        eRelationWithGuardian = ttk.Combobox(fWindow, width = 17, values = ["Father", "Mother", "Uncle", "Aunt", "Brother"], font = ("times new roman", 17, "bold"))
        eRelationWithGuardian.place(x = 350, y = 168)

        eDob = DateEntry(fWindow, width=19, font = ("times new roman", 17))
        eDob.place(x = 350, y = 212)

        eGender = ttk.Combobox(fWindow, width = 17 ,values = ["Male","Female","Others"], font = ("times new roman", 17, "bold"))
        eGender.place(x = 350, y = 256)

        eMaritalStatus = ttk.Combobox(fWindow, width = 17, font = ("times new roman", 17, "bold"), values = ["Married","Unmarried"])
        eMaritalStatus.place(x = 350, y = 300)

        eCaste = ttk.Combobox(fWindow, width = 17, font = ("times new roman", 17, "bold"), values = ["Gen","SC","ST","OBC"])
        eCaste.place(x = 350, y = 344)

        eReligion = ttk.Combobox(fWindow, width = 17, font = ("times new roman", 17, "bold"), values = ["Hindu","Muslim","Others"])
        eReligion.place(x = 350, y = 388)

        eAddress = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eAddress.place(x = 350, y = 432)

        eCity = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eCity.place(x = 350, y = 476)

        eState = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eState.place(x = 350, y = 520)

        ePin = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        ePin.place(x = 350, y = 564)

        #Entry box in Right Side

        eCountry = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eCountry.place(x = 970, y = 80)

        eAnnualIncome = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eAnnualIncome.place(x = 970, y = 124)

        eOccupation = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eOccupation.place(x = 970, y = 168)

        eBranchName = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eBranchName.place(x = 970, y = 212)

        eOpeningBalance = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eOpeningBalance.place(x = 970, y = 256)

        eAccountNo = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eAccountNo.place(x = 970, y = 300)

        eAccountType = ttk.Combobox(fWindow, width = 17, font = ("times new roman", 17, "bold"),values = ["Savings","Current","Credit"])
        eAccountType.place(x = 970, y = 344)

        eCustomerId = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eCustomerId.place(x = 970, y = 388)

        eMobileNo = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eMobileNo.place(x = 970, y = 432)

        eEmailId = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eEmailId.place(x = 970, y = 476)

        ePanNo = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        ePanNo.place(x = 970, y = 520)

        eAadharNo = Entry(fWindow, width = 19, font = ("times new roman", 17, "bold"))
        eAadharNo.place(x = 970, y = 564)

        def submit():
            if eName.get() == "" or eGuardianName.get() == "" or eRelationWithGuardian.get() == "" or  eDob.get() == "" or  eGender.get() == "" or  eMaritalStatus.get() == "" or   eCaste.get() == "" or   eReligion.get() == "" or   eAddress.get() == "" or   eCity.get() == "" or   eState.get() == "" or  ePin.get() == "" or   eCountry.get() == "" or  eAnnualIncome.get() == "" or   eOccupation.get() == "" or   eBranchName.get() == "" or   eOpeningBalance.get() == "" or eAccountNo.get() == "" or eAccountType.get() == "" or   eCustomerId.get() == "" or   eMobileNo.get() == "" or  eEmailId.get() == "" or ePanNo.get() == "":
                msgBox("Fill all the entries",300,1)
            else:
                cr.execute("select accountNo from user where accountNo = ?", (eAccountNo.get(),))
                acc = str(cr.fetchall())
                print(acc[3:-4])
                if acc[3:-4] == eAccountNo.get():
                
                    msgBox("Account No is Used !!!",280,1)
                else:  
                    cr.execute("insert into user(name, guardianName, relationWithGuardian, dob, gender, maritalStatus, caste, religion, address, city, state, pin, country, annualIncome, occupation, branchName,openingBalance, accountNo, accountType, customerId, mobileNo, emailId, panNo, aadharNo) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(eName.get(), eGuardianName.get(),eRelationWithGuardian.get(),  eDob.get(),  eGender.get(),  eMaritalStatus.get(),  eCaste.get(),  eReligion.get(),  eAddress.get(),  eCity.get(),  eState.get(),  ePin.get(),  eCountry.get(), eAnnualIncome.get(),  eOccupation.get(),  eBranchName.get(),  eOpeningBalance.get(),  eAccountNo.get(),  eAccountType.get(),  eCustomerId.get(),  eMobileNo.get(), eEmailId.get(),  ePanNo.get(), 
                    eAadharNo.get()))
                    db.commit()
                    window.destroy()
                db.close()
        

        bSubmit = Button(fWindow, text = "Submit", bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = submit)
        bSubmit.place(x = 595, y = 610)
        window.mainloop()

# userRegistration()
