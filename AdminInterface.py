from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from MsgBox import msgBox

def adminInterface(adminId):
    
    db = sqlite3.connect("BankDB.db")
    cr = db.cursor()

    # fetch admin name
    cr.execute("select name from admin where adminId = ?",(adminId,))
    name = cr.fetchall()[0][0]

    # fetch all user's data for ViewAllUser
    cr.execute("select accountNo, name, address from user")
    allUser = cr.fetchall()

    def home():
        fRemoveUser.place_forget()
        fTransaction.place_forget()
        fFindUser.place_forget()
        fViewAllUser.place_forget()  
        fUpdateUser.place_forget()
        fUpdateUserNext.place_forget()
        fAccount.place_forget()
        fSelect.place_forget()
        fNext.pack_forget()
        
    def addUser():
        from UserRegistration import userRegistration
        userRegistration()      

    def removeUser():
        home()
        fRemoveUser.place(x = 250, y = 176)

        def close():
            home()

        def delete():
            db = sqlite3.connect("BankDB.db")
            cr = db.cursor()
            lvAccountNo = eAccountNo.get()
            cr.execute("select accountNo from user where accountNo = ?", (lvAccountNo,))

            try:        
                acc = cr.fetchone()[0][0] # if arrise error then account no is not exist
                concenmentMsg = Toplevel()
                concenmentMsg.title("Warning !!!")
                concenmentMsg.config(background="red")
                concenmentMsg.geometry("150x120+550+300")
                concenmentMsg.minsize(250,120)
                concenmentMsg.maxsize(250,120)
                lSurity = Label(concenmentMsg, text = "Are you sure ?",bg = "red", fg = "white", font = ("times new roman", 20, "bold"))

                lSurity.pack(pady = 10)
                    
                def yes():
                    concenmentMsg.destroy()
                    cr.execute("delete from user where accountNo = ?", (lvAccountNo,))
                    db.commit()
                    msgBox("Account No. is Deleted successfully",450,1)
                
                def no():
                    concenmentMsg.destroy()   

                frame = Frame(concenmentMsg, bg = "red", width = 300, height = 50)
                frame.pack()
                bYes = Button(frame, text = "Yes", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command = yes)
                bYes.pack(side = "left", pady = 10, padx=10, fill = X)    
                bNo = Button(frame, text = "No", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command =  no)
                bNo.pack(side = "left",pady = 10, padx=10, fill = Y)
                
            except:     
                msgBox("Account No. is not exist !!!",350,1)
        

        '''def clearEntry(): # textvar = gvAccountNo in bDelete
            gvAccountNo.set("")'''

        #gvAccountNo = StringVar()
        lAccountNo = Label(fRemoveUser, text = "Account No", bg = "#F3B600", fg = "black", font = ("times new roman", 20, "bold"))
        lAccountNo.place(x = 100, y = 50)

        eAccountNo = Entry(fRemoveUser, font = ("times new roman", 20, "bold"), border = 2)
        eAccountNo.place(x = 300, y = 50)

        bDelete = Button(fRemoveUser, text = "Delete User", width = 10, bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = delete)
        bDelete.place(x = 170, y = 315)

        bclose = Button(fRemoveUser, text = "Close", width = 10, bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = close)
        bclose.place(x = 370, y = 315)

    def updateUser():
        home()
        fUpdateUserNext.place_forget()
        fUpdateUser.place(x = 250, y = 150)

        fAccount.place(x = 0, y = 0)

        lAccountNo = Label(fAccount, text = "Account No", bg = "#F3B600", fg = "black", font = ("times new roman", 20, "bold"))
        lAccountNo.place(x = 100, y = 50)

        eAccountNo = Entry(fAccount, font = ("times new roman", 20, "bold"), border = 2)
        eAccountNo.place(x = 300, y = 50)

        def accNext():
            try:
                cr.execute("select accountNo from user where accountNo = ?",(eAccountNo.get(),))
                accountUpdate = cr.fetchall()[0][0]
                fAccount.place_forget()
                fSelect.place(x = 0, y = 0)
            except:
                msgBox("Invalid Account No",350,1)

        bAccNext = Button(fAccount, text = "Next", font = ("times new roman", 20, "bold"), width = 8, bg = "black", fg = "white", command = accNext)
        bAccNext.place(x = 290, y = 380)

        lTitle = Label(fSelect, text = "Select which You want to Update", font = ("times new roman", 25, "bold"), bg = "#F3B600", fg = "black")
        lTitle.place(x = 100, y = 20)
        
        # create checkbox
        vName = IntVar(fSelect)
        cName = Checkbutton(fSelect, text = "Name", variable = vName, font = ("times new roman", 15, "bold"), bg = "#F3B600", fg = "black")
        cName.place(x = 150, y = 100)

        vGuardianName = IntVar(fSelect)
        cGuardianName = Checkbutton(fSelect, text = "Guardian Name", variable = vGuardianName, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cGuardianName.place(x = 150, y = 150)

        vAddress = IntVar(fSelect)
        cAddress = Checkbutton(fSelect, text = "Address", variable = vAddress, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cAddress.place(x = 150, y = 200)

        vCity = IntVar(fSelect)
        cCity = Checkbutton(fSelect, text = "City", variable = vCity, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cCity.place(x = 150, y = 250)

        vState = IntVar(fSelect)
        cState = Checkbutton(fSelect, text = "State", variable = vState, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cState.place(x = 150, y = 300)

        vPin = IntVar(fSelect)
        cPin = Checkbutton(fSelect, text = "Pin No", variable = vPin, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cPin.place(x = 400, y = 100)

        vCountry = IntVar(fSelect)
        cCountry = Checkbutton(fSelect, text = "Country", variable = vCountry, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cCountry.place(x = 400, y = 150)

        vBranch = IntVar(fSelect)
        cBranch = Checkbutton(fSelect, text = "Branch", variable = vBranch, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cBranch.place(x = 400, y = 200)

        vMobile = IntVar(fSelect)
        cMobile = Checkbutton(fSelect, text = "Mobile No", variable = vMobile, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cMobile.place(x = 400, y = 250)

        vEmail = IntVar(fSelect)
        cEmail = Checkbutton(fSelect, text = "Email Id", variable = vEmail, font = ("times new roman", 15, "bold"), fg = "black", bg = "#F3B600")
        cEmail.place(x = 400, y = 300)

        def next():
            fSelect.place_forget()            
            fUpdateUserNext.place(x = 250, y = 150)
            fNext.pack()
            
            # determine which fields are selected if Name is selectd then vName.get() wil be 1
            selected = {"Name" : vName.get(), "Guardian Name" : vGuardianName.get(), "Address" : vAddress.get(), "City" : vCity.get(), "State" : vState.get(), "Pin No" : vPin.get(), "Country" : vPin.get(), "Branch" : vBranch.get(), "Mobile No" : vMobile.get(), "Email Id" : vEmail.get()
            }

            labels = []
            entrys = []

            s = [StringVar() for i in selected]
            r = 0 # for count index of s and it will help to put the exact values in table attribute
            xLabel = 160
            xEntry = 340
            yAx = 5
            for i in selected:
                if selected[i]:
                    labels.append(Label(fNext, text = i, width = 12, font = ("times new roman", 15, "bold"), bg = "#F3B600", fg = "black"))
                    labels[r].place(x = xLabel, y = yAx)

                    entrys.append(Entry(fNext, font = ("times new roman", 15, "bold"), textvar = s[r]))
                    entrys[r].place(x = xEntry, y = yAx)

                    yAx += 30
                    r += 1
            
            def UpdatePlaceForget():
                r = 0
                for i in selected:
                    if selected[i]:
                        labels[r].place_forget()
                        entrys[r].place_forget()
                        r += 1

            tableAttributes = ["name", "guardianName", "address", "city", "state", "pin", "country", "branchName", "mobileNo", "emailId"]

            
            def updateCheck():
                r = 0
                blankEntry = False
                for i in selected:
                    if selected[i]:
                        if entrys[r].get() == "":
                            blankEntry = True
                        r += 1
                if blankEntry:
                    msgBox("Please fill all the Box",350,1)
                else:
                    updateDb()

            def updateDb():
                fNext.pack_forget()
                UpdatePlaceForget()
                bUpdate.pack_forget()
                r = 0 
                for i in selected:
                    if selected[i]:
                        print(s[r].get(), "s")
                        r += 1
                r = 0
                for i in selected:
                    if selected[i]:
                        cr.execute(f"update user set {tableAttributes[r]} = ? where accountNo = ?",(s[r].get(),eAccountNo.get()))
                        r += 1
                db.commit()
                msgBox("Account is Updated successfully",400,1)
                home()
            
            bUpdate = Button(fNext, text = "Update", bg = "black", fg = "white", width = 12, font = ("times new roman", 15, "bold"), command = updateCheck)
            bUpdate.place(x = 270, y = 400)

        bNext = Button(fSelect, text = "Next >", font = ("times new roman", 20, "bold"), bg = "black", fg = "white", command = next)
        bNext.place(x = 300, y = 380)

    def findUser():     # enter to search user interface 
        home()
        def search():       #search for find user's details
            fTransaction.place_forget()

            cr.execute("select accountNo from user where accountNo = ?", (eFindUser.get(),))

            lvAccountNo = cr.fetchall()

            if lvAccountNo == []:
                msgBox("Account No is not exists",400,1)
            else:
                cr.execute("select * from user where accountNo = ?", (eFindUser.get(),))
                userDetails = cr.fetchall()[0]
                listUserDetails.delete(0,"end")
                j = 0
                for i in userDetails:
                    listUserDetails.insert(j+1, str(userFields[j]) + "  :  " + str(i))
                    j = j+1

        eFindUser = Entry(fFindUser, font = ("times new roman", 20, "bold"), width = 28)

        bSearch = Button(fFindUser, text = "Search", font = ("times new roman", 15, "bold"), bg = "black", fg = "white", command = search)

        # Define list for show user's information
        listUserDetails = Listbox(fFindUser, width = 48, height = 10, font = ("times new roman", 15))
    
        # Insert user's information in list box
        userFields = ["NAME", "GUARDIAN NAME", "RELATION WITH GUARDIAN" , "DOB" , "GENDER","MARITALSTATUS", "CASTE", "RELIGION", "ADDRESS", "CITY", "STATE", "PIN", "COUNTRY",'ANNUAL INCOME', "OCCUPATION", "BRANCHNAME","BALANCE", "ACCOUNT NO", "ACCOUNT TYPE","CUSTOMER ID", "MOBILE NO", "EMAIL ID", "PAN NO", "AADHAR NO", "USER ID", "PASSWORD"]    

        def click(event):
            eFindUser.config(state = NORMAL)
            eFindUser.delete(0,"end")

        eFindUser.insert(0,"Enter Account No")
        eFindUser.config(state = DISABLED)
        eFindUser.bind("<Button-1>", click)

        fFindUser.place(x = 250, y = 176)
        eFindUser.place(x= 100 ,y = 20)
        bSearch.place(x = 510, y = 19)
        listUserDetails.place(x = 100, y = 80)

    def transaction():
        '''
        eFindUser.place_forget()
        bSearch.place_forget()
        listUserDetails.place_forget()   =    fFindUser
        fFindUser.place_forget()'''
        home()

        fTransaction.place(x = 250, y = 176)

        lAcountNo = Label(fTransaction, text = "Account No", bg = "#F3B600", fg = "black", font = ("times new roman", 20, "bold"))
        lAcountNo.place(x = 100, y = 20)
        
        def getBalance(event):
            try:
                eBalance.destroy()
            except:
                print("not bal")
            cr.execute("select openingBalance from user where accountNo = ?", (eAccountNo.get(),))
            
            lBalance = Label(fTransaction, text = "Available Balance", bg = "#F3B600", fg = "black", font = ("times new roman", 20, "bold"))
            lBalance.place(x = 190, y = 150)
            eBalance = Entry(fTransaction, width = 15, border = 0, bg = "#F3B600", font = ("times new roman", 20, "bold"))
            eBalance.place(x = 420, y = 150)
            try:
                eBalance.delete(0,END)
                eBalance.insert(0, int(cr.fetchall()[0][0]))
            except:
                pass
            eBalance.config(state = "disabled", bg = "#F3B600")
            

        eAccountNo = Entry(fTransaction, font = ("times new roman", 20, "bold"))# ,textvar = gvAccountNo
        eAccountNo.place(x = 300, y = 20)
        eAccountNo.bind("<FocusOut>",getBalance)

        lAmount = Label(fTransaction, text = "Amount", bg = "#F3B600", fg = "black", font = ("times new roman", 20, "bold"))
        lAmount.place(x = 100, y = 70)

        eAmount = Entry(fTransaction, font = ("times new roman", 20, "bold")) # ,textvar = gvAmount
        eAmount.place(x = 300, y = 70)

        '''def clear():
            gvAccountNo.set("")
            gvAmount.set("")'''

        def deposit():
            cr.execute("select openingBalance from user where accountNo = ?", (eAccountNo.get(),))
            bal = int(cr.fetchall()[0][0])

            accountNo = eAccountNo.get()
            amount =  eAmount.get()
            if amount == "" or accountNo == "":
                msgBox("Please enter Account No and amount",460,1)
            else:
                amount = str(bal+int(amount))

                concenmentMsg = Toplevel()
                concenmentMsg.title("Warning !!!")
                concenmentMsg.config(background="red")
                concenmentMsg.geometry("150x120+550+300")
                concenmentMsg.minsize(250,120)
                concenmentMsg.maxsize(250,120)
                lSurity = Label(concenmentMsg, text = "Are you sure ?",bg = "red", fg = "white", font = ("times new roman", 20, "bold"))

                lSurity.pack(pady = 10)
                    
                def yes():
                    concenmentMsg.destroy()
                    cr.execute("update user set openingBalance = ? where accountNo = ?", (amount, accountNo))
                    db.commit()
                    msgBox(f"Deposite is successfull", 400,1)
                                        
                    #clear()
                
                def no():
                    concenmentMsg.destroy()   

                frame = Frame(concenmentMsg, bg = "red", width = 300, height = 50)
                frame.pack()
                bYes = Button(frame, text = "Yes", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command = yes)
                bYes.pack(side = "left", pady = 10, padx=10, fill = X)    
                bNo = Button(frame, text = "No", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command =  no)
                bNo.pack(side = "left",pady = 10, padx=10, fill = Y)
                      

        def withdraw():
            cr.execute("select openingBalance from user where accountNo = ?", (eAccountNo.get(),))
            bal = int(cr.fetchall()[0][0])
            
            accountNo = eAccountNo.get()
            amount =  int(eAmount.get())
            if amount == "" or accountNo == "":
                msgBox("Please enter Account No and amount",460,1)
            else:                
                if bal < amount:
                    msgBox("Account have not enough amount",400,1)
                else:
                    amount = str(bal-amount)
                    concenmentMsg = Toplevel()
                    concenmentMsg.title("Warning !!!")
                    concenmentMsg.config(background="red")
                    concenmentMsg.geometry("150x120+550+300")
                    concenmentMsg.minsize(250,120)
                    concenmentMsg.maxsize(250,120)
                    lSurity = Label(concenmentMsg, text = "Are you sure ?",bg = "red", fg = "white", font = ("times new roman", 20, "bold"))
                    #msg.place(x = 30, y = 10)
                    lSurity.pack(pady = 10)
                    def yes():
                        concenmentMsg.destroy()
                        cr.execute("update user set openingBalance = ? where accountNo = ?", (amount ,accountNo))
                        db.commit()
                        msgBox("Withdraw is successfull",400,1)
                        #clear()
                        
                    def no():
                        concenmentMsg.destroy()
                    
                    frame = Frame(concenmentMsg, bg = "red", width = 300, height = 50)
                    frame.pack()
                    bYes = Button(frame, text = "Yes", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command = yes)
                    bYes.pack(side = "left", pady = 10, padx=10, fill = X)    
                    bNo = Button(frame, text = "No", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command =  no)
                    bNo.pack(side = "left",pady = 10, padx=10, fill = Y) 

        bDeposit = Button(fTransaction, text = "Deposite", width = 9, bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = deposit)
        bDeposit.place(x = 170, y = 340)        
        
        bWithdraw = Button(fTransaction, text = "Withdraw", width = 9, bg = "black", fg = "white", font = ("times new roman", 20, "bold"), command = withdraw)
        bWithdraw.place(x = 370, y = 340)

    def viewAllUser():
        home()  #fFindUser.place_forget()
        fViewAllUser.place(x = 250, y = 176)
        
        # style treeview
        style = ttk.Style()
        style.theme_use('clam')
        '''
        style.configure("t.Treeview", font = ("times new roman", 50))
        style.configure("t.Treeview.Heading", font = ("times new roman", 20, "bold"))'''

        tViewAllUser = ttk.Treeview(fViewAllUser, column = ("Account No", "Name", "Address"), show = "headings", height = 18)#height means how many record

        vScrollbar = Scrollbar(fViewAllUser)
        vScrollbar.pack(side = RIGHT, fill = Y)

        tViewAllUser.tag_configure('odd', background='#E8E8E8')
        tViewAllUser.tag_configure('even', background='#DFDFDF')
    
        tViewAllUser.column("Account No", anchor = CENTER, width = 225)
        tViewAllUser.column("Name", anchor = CENTER, width = 225)
        tViewAllUser.column("Address", anchor = CENTER, width = 225)

        tViewAllUser.heading(text = "Account No", column = "Account No")
        tViewAllUser.heading(text = "Name", column = "Name")
        tViewAllUser.heading(text = "Address", column = "Address")

        for i in allUser:
            tViewAllUser.insert("", "end", values = (i[0], i[1], i[2]))
    
        tViewAllUser.pack()
        vScrollbar.config(command = tViewAllUser.yview)
        tViewAllUser.config(yscrollcommand = vScrollbar.set)

    def logOut():
        window.destroy()
        from main import homePage
        homePage()  #import Banking Home Page

    window = Tk()
    window.geometry("1000x650+200+30")
    window.config(background = "#f3b600")# 102762
    window.title("Admin")

    fWindow = Frame(window, width = 1000, height = 650, background = "#f3b600")   # A6D1E6
    fWindow.pack()

    fTop = Frame(fWindow, bg = "#f3b600", width = 1000, height = 100)   #102762
    fTop.place(x = 0, y = 0)

    logo = Image.open("./img/logo.png")
    rLogo = logo.resize((130,106))
    oLogo = ImageTk.PhotoImage(rLogo)

    fLogo = Label(fWindow,image = oLogo, bg = "#f3b600")
    fLogo.place(x = 0, y = 0)

    lBankName = Label(fTop,text = "ATLAS",fg = "black", bg = "#f3b600", font = ("times new roman", 40, "bold"))#102762
    lBankName.place(x = 140, y = 18)
    
    # start set Welcome admin
    fWelcome = Frame (fTop, height = 100, width = 400, bg = "#F3B600")
    fWelcome.place(x = 600, y = 0)

    lWelcome = Label(fWelcome, text = "Welcome", fg = "black", bg = "#f3b600",font = ("times new roman", 20, "bold"))
    lWelcome.place(relx = 0.5, rely = 0.3, anchor = CENTER)

    lName = Label(fWelcome, text = name, bg = "#f3b600", fg = "black", font = ("times new roman", 20, "bold"))
    lName.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    # end set welcome admin

    # Home page    
    hLogo = ImageTk.PhotoImage(Image.open("./img/logo.png").resize((500,500)))

    Label(fWindow, image = hLogo, bg="#f3b600").place(x = 320, y = 150)

    Label(fWindow, text = "Welcome to the Admin Page", font = ("times new roman", 40, "bold"), bg = "#f3b600", fg = "black").place(x = 280, y = 160)

    fLeft = Frame(fWindow, width = 200, height = 650, background = "#f3b600")#7F5283
    fLeft.place(x = 0, y = 100)
    
    # frame for View all user    
    fViewAllUser = Frame(fWindow, width = 700, height = 400)
    
    # frame for Update user
    fUpdateUser = Frame(fWindow, width = 700, height = 450, bg = "#F3B600")

    # click on next to open new frame in Update user
    fUpdateUserNext = Frame(fWindow, height = 450, width = 700, bg = "#F3B600")

    # for Enter account no step in update
    fAccount = Frame(fUpdateUser, height = 450, width = 700, bg = "#F3B600")

    # for select update fields stop in update
    fSelect = Frame(fUpdateUser, height = 450, width = 700, bg = "#F3B600")

    # for go next page where user enter their correct details in update_user
    fNext = Frame(fUpdateUserNext, bg = "#F3B600", height = 450, width = 700)

    # frame for Remove user
    fRemoveUser = Frame(fWindow, width = 700, height = 400, bg = "#F3B600")

    # Find user and using account number it is pack in findUser function
    fFindUser = Frame(fWindow, width = 700, height = 400, bg = "#F3B600")
    
    # Go to deposite and withdraw Frame
    bTransaction = Button(fFindUser, text = "Transaction", font = ("times new roman", 20, "bold"), width = 10, fg = "white", bg = "black", command = transaction)
    bTransaction.place(x = 260, y = 340)

    fTransaction = Frame(fWindow, width = 700, height = 400, bg = "#F3B600")

    #Difference between button --- 60
    bHome = Button(fLeft, text = "Home", bg = "black", width = 12, fg = "white", font = ("times new roman", 20, "bold"), command = home)
    bHome.place(x = 0, y = 30)

    bAddUser = Button(fLeft, text = "Add User", bg = "black", width = 12, fg = "white", font = ("times new roman", 20, "bold"), command = addUser)
    bAddUser.place(x = 0, y = 90)

    bRemoveUser = Button(fLeft, text = "Remove User", bg = "black", width = 12, fg = "white", font = ("times new roman", 20, "bold"), command = removeUser)
    bRemoveUser.place(x = 0, y = 150)

    bUpdateUser = Button(fLeft, text = "Update User", bg = "black", width = 12, fg = "white", font = ("times new roman", 20, "bold"), command = updateUser)
    bUpdateUser.place(x = 0, y = 210)

    bViewAllUser = Button(fLeft, text = "View All User", bg = "black", width = 12, fg = "white", font = ("times new roman", 20, "bold"), command = viewAllUser)
    bViewAllUser.place(x = 0, y = 270)

    bFindUser = Button(fLeft, text = "Search User", bg = "black", width = 12, fg = "white", font = ("times new roman", 20, "bold"), command = findUser)
    bFindUser.place(x = 0, y = 330)

    bTransaction = Button(fLeft, text = "Transaction", font = ("times new roman", 20, "bold"), width = 12, fg = "white", bg = "black", command = transaction)
    bTransaction.place(x = 0, y = 390)

    bLogOut = Button(fLeft, text = "Log Out", bg = "black", fg = "white", width = 12, font = ("times new roman", 20, "bold"), command = logOut)
    bLogOut.place(x = 0, y = 450)

    window.mainloop()
    

if __name__ == '__main__':
    adminInterface("b")
