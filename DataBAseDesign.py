from tkinter import *
import sqlite3


db = sqlite3.connect("BankDB.db")
cr = db.cursor()
   
try:
    cr.execute("create table user(name text, guardianName text, relationWithGuardian text, dob text, gender text,maritalStatus text, caste text, religion text, address text, city text, state text, pin text, country text,annualIncome text, occupation text, branchName text,openingBalance text, accountNo text primary key, accountType text,customerId text, mobileNo text, emailId text, panNo text, aadharNo text, userId text, password text)")  
except:
    pass

try:    
    cr.execute("create table admin(name text, dob text, gender text, caste text, religion text, address text, city text, state text, pin text, country text, branchName text, mobileNo text, emailId text, panNo text, aadharNo text, adminId text primary key, password text)")
except:
    pass

db.commit()

'''
def submit():
    lvAdminId = gvAdminId.get()
    lvPassword = gvPassword.get()
    lvConfrom = gvConfrom.get()
    
    if lvPassword == lvConfrom:
        cr.execute("insert into admin(adminId, password) values (?,?)", (lvAdminId, lvPassword))
        db.commit()
        window.destroy()
        
    else:
        print("Password and confrom password must be same")
        print(lvPassword, "and", lvConfrom, "is not same")   
'''    
  
window = Tk()
window.title("DataBase Design")
window.geometry("640x330+400+125")
window.config(background = "ivory")

design = Label(window, text ="DataBase Design is complete", font = ("times new roman",20,"bold"), bg = "ivory", fg = "blue")
design.place(x = 150, y = 120)


'''

fWindow = Frame (window, background = "ivory", width = 640, height = 330)
fWindow.place(x = 0, y = 0)

lAdminId = Label(fWindow, text = "New Admin Id", font = ("times new roman",20,"bold"), bg = "ivory", fg = "blue")
lAdminId.place(x = 50, y = 50)

lPassword = Label(fWindow, text = "New Password", font = ("times new roman", 20, "bold"), bg = "ivory", fg = "blue")
lPassword.place(x = 50, y = 100)

lConfrom = Label(fWindow, text = "Confrom Password", font = ("times new roman", 20, "bold"), bg = "ivory", fg = "blue")
lConfrom.place(x = 50, y = 150)

gvAdminId = StringVar()
gvPassword = StringVar()
gvConfrom = StringVar()

eAdminId = Entry(fWindow, font = ("times new roman", 20, "bold"), border = 3, textvar = gvAdminId)
eAdminId.place(x = 300, y = 50)

ePassword = Entry(fWindow, font = ("times new roman", 20, "bold"), border = 3, textvar = gvPassword)
ePassword.place(x = 300, y = 100)

eConfrom= Entry(fWindow, font = ("times new roman", 20, "bold"), border = 3, textvar = gvConfrom)
eConfrom.place(x = 300, y = 150)

bSubmit = Button(fWindow, text = "Submit", bg = "#102762", fg = "white", font = ("times new roman", 20, "bold"), command = submit)
bSubmit.place(x = 220, y = 230)
'''

window.mainloop()
