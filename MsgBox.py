from re import A
from tkinter import *

def msgBox(text, w = 250, noArg = 1,  h = 120):   
    msgBox = Tk()
    msgBox.title("Warning !!!")
    msgBox.geometry("100x120+550+300")
    msgBox.maxsize(w, h)
    msgBox.minsize(w, h)
    msgBox.config(background = "red")
    
    def no():
        global concenment
        msgBox.destroy()
        concenment = False

    def yes():
        global concenment
        msgBox.destroy()
        concenment = True
    
    msg = Label(msgBox, text = text,bg = "red", fg = "white", font = ("times new roman", 20, "bold"))
    #msg.place(x = 30, y = 10)
    msg.pack(pady = 10)

    if noArg == 1:
        ok = Button(msgBox, text = "OK", width = 5, bg = "cyan", fg = "black", font = ("times new roman", 15, "bold"), command = lambda : msgBox.destroy())
        ok.pack()
    else:
        frame = Frame(msgBox, bg = "red", width = 300, height = 50)
        frame.pack()
        bYes = Button(frame, text = "Yes", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command = yes)
        bYes.pack(side = "left", pady = 10, padx=10, fill = X)    
        bNo = Button(frame, text = "No", width = 5, bg = "cyan", font = ("times new roman", 15, "bold"), command = no)
        bNo.pack(side = "left",pady = 10, padx=10, fill = Y)


    msgBox.mainloop()
    
    try:
        return concenment
    except:
        pass

    
#print(msgBox("Are you sure ?"))
#print(msgBox("Are you sure ?",250,2,120))
#msgBox("Account No is Used",260,1)
#msgBox("New Password and Confrom Password must be same",650,1)
#h = msgBox("New Password and Confre",400,2)
#msgBox("Are you sure to logout",400,2)
#msgBox("Invalid User Id or Password", 400, 2)

#msgBox('''Your Id and Password is 
#created successfully now you
#can login using your id and
#password''',400,1,200)