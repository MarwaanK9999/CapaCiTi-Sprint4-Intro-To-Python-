import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Listbox, Message, messagebox
from tkinter import *
from tkinter.constants import BOTTOM, END, LEFT, RIGHT, TOP
import tkinter.font as tkFont
from PIL import ImageTk,Image
import datetime
import random
import re

datetime_object = datetime.datetime.now()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def authorizeUser(self):
        username = usernameEntry.get()
        PINNo = PINEntry.get()
        global retainUsername
        f = open("User Data.txt","r")
        info = f.read()
        info = info.split()
        if username in info:
            index = info.index(username) + 1
            usr_password = info[index]
            
            if usr_password == PINNo:
                retainUsername = username
                self.switch_frame(MenuPage)
                messagebox.showinfo(title="Welcome",message="Welcome, " + username)
                    
            else:
                messagebox.showerror(title="error",message="Enter correct password.")
                PINEntry.focus()
                
        else:
            messagebox.showerror(title="error",message="Enter an existing username.")
            usernameEntry.focus()

class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #setting title
        master.title("Main")
        master.geometry("600x343")
        master.resizable(width=False, height=False)

        ft1 = tkFont.Font(family='Times', size=28)

        ft2 = tkFont.Font(family='Times', size=16)

        Message1 = Message(self, borderwidth="4px", font=ft2, fg="#333333", justify="left", text="Welcome to our banking application, making your life easier!", width=550)
        Message1.grid(row=0, column=0, ipady=70)
        
        loginbutton = Button(self, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="Login", command=lambda: master.switch_frame(LoginPage))
        loginbutton.grid(row=1, column=0, ipadx=237)  

        registerbutton = Button(self, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="Register", command=lambda: master.switch_frame(RegistrationPage))
        registerbutton.grid(row=2, column=0, ipadx=220)

class RegistrationPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #setting title
        master.title("Registration")
        master.geometry("300x300")

        global userEntry
        global balanceEntry
        global passwordEntry
        global passwordConfirmEntry

        ft1 = tkFont.Font(family='Times', size=10)
        ft2 = tkFont.Font(family='Times',size=18)

        userLabel = Label(self, borderwidth="4px", font=ft1, fg="#333333", justify="left", text="Enter Username:")
        userLabel.grid(row = 0, column = 0, ipadx= 2, ipady= 15)

        userEntry = Entry(self, bg="#ffffff", borderwidth="1px", font=ft1, fg="#333333", justify="center")
        userEntry.grid(row = 0, column = 1, ipady= 15)

        balanceLabel = Label(self, borderwidth="4px", font=ft1, fg="#333333", justify="left", text="Enter Initial Balance:")
        balanceLabel.grid(row = 1, column = 0, ipadx= 2, ipady= 15)

        balanceEntry = Entry(self, bg="#ffffff", borderwidth="1px", font=ft1, fg="#333333", justify="center")
        balanceEntry.grid(row = 1, column = 1, ipady= 15)

        passwordLabel = Label(self, borderwidth="4px", font=ft1, fg="#333333", justify="left", text="Enter PIN:")
        passwordLabel.grid(row = 2, column = 0, ipadx= 2, ipady= 15)

        passwordEntry = Entry(self, bg="#ffffff", borderwidth="1px", font=ft1, fg="#333333", justify="center", show= "*")
        passwordEntry.grid(row = 2, column = 1, ipady= 15)

        passwordConfirmLabel = Label(self, borderwidth="4px", font=ft1, fg="#333333", justify="left", text="Confirm PIN:")
        passwordConfirmLabel.grid(row = 3, column = 0, ipadx= 2, ipady= 15)

        passwordConfirmEntry = Entry(self, bg="#ffffff", borderwidth="1px", font=ft1, fg="#333333", justify="center", show= "*")
        passwordConfirmEntry.grid(row = 3, column = 1, ipady= 15)
        
        confirmButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Register", command=lambda: self.captureData())
        confirmButton.grid(row = 4, column = 0, ipadx= 20)

        backButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Back", command=lambda: master.switch_frame(MainPage))
        backButton.grid(row = 4, column = 1, ipadx= 25)

    def captureData(self):
        username = str(userEntry.get())
        balance = str(balanceEntry.get())
        PINno = str(passwordEntry.get())
        confirmPass = str(passwordConfirmEntry.get())

        #regexuser = re.search("[A-Za-z0-9] {6,18}", username)
        #regexbalance = re.match("[0-9]", balance)
        #regexpassword = re.match("[0-9]{4,8}", PINno)

        fileobject = open("User Data.txt","r")
        info = fileobject.read()
        info = info.split()
        fileobject.close()
        if username in info:
            messagebox.showerror(title="error",message="Username already exists.")
            userEntry.focus()
        elif username.isalnum() == False or username == "" or len(username) < 6 or len(username) > 18:
            messagebox.showerror(title="error",message="Enter an alphanumeric username, between 6-18 characters.")
            userEntry.focus()
        elif balance.isnumeric() == False or balance == "":
            messagebox.showerror(title="error",message="Enter a numeric balance.")
            balanceEntry.focus()
        elif PINno.isnumeric() == False or PINno == "" or len(PINno) > 8 or len(PINno) < 4:
            messagebox.showerror(title="error",message="Enter a numeric PIN Number between 4-8 characters.")
            passwordEntry.focus()
        elif confirmPass != PINno:
            messagebox.showerror(title="error",message="PIN number must match the PIN number provided before.")
            passwordConfirmEntry.focus()
        else:
            fileobject = open("User Data.txt", "a+")
            fileobject.write(username)
            fileobject.write("\n")
            fileobject.write(PINno)
            fileobject.write("\n")
            fileobject.write(str("R" + "%.2f" %  float(balance)))
            fileobject.write("\n")
            fileobject.close()
            with open("Transactions/" + username + " Transaction Log.txt", "w") as f2:
                f2.close()
            messagebox.showinfo(title="Success",message="Registration successful!.")

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #setting title
        master.title("Login")
        master.geometry("351x270")
        master.resizable(width=False, height=False)

        global usernameEntry
        global PINEntry

        ft1 = tkFont.Font(family='Times', size=12)
        ft2 = tkFont.Font(family='Times',size=16)

        headingLabel = Label(self, font=ft2, fg="#333333", justify="center", text="Enter Login Details")
        headingLabel.grid(row= 0, columnspan= 2, ipadx= 2, ipady= 15)

        usernameLabel = Label(self, font=ft1, fg="#333333", justify="center", text="Username:")
        usernameLabel.grid(row = 1, column = 0, ipadx= 2, ipady= 15)

        usernameEntry = Entry(self, bg="#ffffff", borderwidth="1px", font=ft1, fg="#333333", justify="center")
        usernameEntry.grid(row = 1, column = 1, ipadx= 2, ipady= 15)

        PINLabel = Label(self, font=ft1, fg="#333333", justify="center", text="PIN:")
        PINLabel.grid(row = 2, column = 0, ipadx= 2, ipady= 15)

        PINEntry = Entry(self, bg="#ffffff", borderwidth="1px", font=ft1, fg="#333333", justify="center", show= "*")
        PINEntry.grid(row = 2, column = 1, ipadx= 2, ipady= 15)

        confirmDetailsButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Confirm Login", command=lambda: master.authorizeUser())
        confirmDetailsButton.grid(row = 3, column = 0, pady=3, ipadx=12, ipady= 15)

        backButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Back To Start", command=lambda: master.switch_frame(MainPage))
        backButton.grid(row = 3, column = 1, pady=3, ipadx=12, ipady= 15)
        
class MenuPage(tk.Frame):
    def __init__(self, master):    
        tk.Frame.__init__(self, master)
        #setting title
        master.title("Menu")
        master.geometry("445x534")
        master.resizable(width=False, height=False)

        ft1 = tkFont.Font(family='Times', size=12)
        ft2 = tkFont.Font(family='Times',size=16)

        headingLabel = Label(self, font=ft2, fg="#333333", justify="center", text="What would you like to do?")
        headingLabel.grid(row= 0, column= 0, pady=3, ipadx= 2, ipady= 15)

        viewBalanceButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="View Balance", command=lambda: master.switch_frame(Balance))
        viewBalanceButton.grid(row= 1, column= 0, pady=3, ipadx= 65, ipady= 25)

        transactionsButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="View Transactions", command=lambda: master.switch_frame(Transactions))
        transactionsButton.grid(row= 2, column= 0, pady=3, ipadx= 45, ipady= 25)

        depwithButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Deposit/Withdraw", command=lambda: master.switch_frame(DepositAndWithdraw))
        depwithButton.grid(row= 3, column= 0, pady=3, ipadx= 45, ipady= 25)

        signOutButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Sign Out", command=lambda: master.switch_frame(MainPage))
        signOutButton.grid(row= 4, column= 0, pady=3, ipadx= 85, ipady= 25)

class Balance(tk.Frame):
    def __init__(self, master):    
        tk.Frame.__init__(self, master)
        #setting title
        master.title("Balance")
        master.geometry("350x250")
        master.resizable(width=False, height=False)

        ft1 = tkFont.Font(family='Times', size=18)
        ft2 = tkFont.Font(family='Times',size=14)

        global balanceDisplay

        balanceLabel = Label(self, font=ft2, fg="#333333", justify="right", text="Current Available Balance for " + retainUsername + ":")
        balanceLabel.grid(row= 0, columnspan= 2, ipadx= 2, ipady= 15)

        balanceDisplay = Label(self, font=ft1, fg="#333333", justify="center")
        balanceDisplay.grid(row= 1, columnspan= 2, ipadx= 50, ipady= 15)

        viewBalanceButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="View Balance", command=lambda: self.viewBalance())
        viewBalanceButton.grid(row= 2, column= 0, pady= 10, ipadx= 12, ipady= 15)

        BackButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Back", command=lambda: master.switch_frame(MenuPage))
        BackButton.grid(row= 2, column= 1, pady= 10, ipadx= 43, ipady= 15)

    def viewBalance(self):
        f = open("User Data.txt","r")
        info = f.read()
        info = info.split()
        if retainUsername in info:
            index = info.index(retainUsername) + 2
            balanceAmount = info[index]
            balanceDisplay.config(text=balanceAmount)

class Transactions(tk.Frame):
    def __init__(self, master):    
        tk.Frame.__init__(self, master)
        #setting title
        master.title("Transactions")
        master.geometry("553x470")
        master.resizable(width=False, height=False)

        ft1 = tkFont.Font(family='Times', size=12)
        ft2 = tkFont.Font(family='Times',size=14)

        global transactionsBox

        transactionsBox = Listbox(self, font=ft2, justify="left")
        transactionsBox.grid(row= 0, columnspan= 2, pady=10, ipadx= 110, ipady= 60)

        viewTransactionsButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="View Transactions", command=lambda: self.viewTransactions())
        viewTransactionsButton.grid(row= 1, column= 0, ipadx= 20, ipady= 15)

        BackButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Back", command=lambda: master.switch_frame(MenuPage))
        BackButton.grid(row= 1, column= 1, ipadx= 70, ipady= 15)

    def viewTransactions(self):
        f = open("User Data.txt","r")
        info = f.read()
        info = info.split()
        f.close()
        f2 = open("Transactions/" + retainUsername + " Transaction Log.txt", "r")
        for x in f2:
            transactionsBox.insert(END, x)
        f.close()

class DepositAndWithdraw(tk.Frame):
    def __init__(self, master):    
        tk.Frame.__init__(self, master)
        #setting title
        master.title("Deposits And Withdrawals")
        master.geometry("410x370")
        master.resizable(width=False, height=False)

        ft1 = tkFont.Font(family='Times', size=20)
        ft2 = tkFont.Font(family='Times',size=14)

        global AmountEntry

        AmountLabel = Label(self, font=ft2, fg="#333333", justify="right", text="Enter Amount:")
        AmountLabel.grid(row= 0, columnspan= 2, pady=10, ipadx= 50, ipady= 10)

        AmountEntry = Entry(self, bg="#ffffff", borderwidth="1px", font=ft1, fg="#333333", justify="center")
        AmountEntry.grid(row= 1, columnspan= 2, pady=10, ipadx= 40, ipady= 40)

        depositButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Deposit Amount", command=lambda: self.depositMoney())
        depositButton.grid(row= 2, column= 0, ipadx= 27, ipady= 20)

        withdrawButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Withdraw Amount", command=lambda: self.withdrawMoney())
        withdrawButton.grid(row= 2, column= 1, ipadx= 23, ipady= 20)

        BackButton = Button(self, bg="#01aaed", borderwidth="4px", font=ft2, fg="#000000", justify="center", text="Back", command=lambda: master.switch_frame(MenuPage))
        BackButton.grid(row= 3, columnspan= 2, ipadx= 172, ipady= 20)

    def depositMoney(self):
        transactionType = "Deposit"
        depositAmount = str(AmountEntry.get())
        if depositAmount.isnumeric() == False:
            messagebox.showerror(title="error",message="Please enter an appropriate numeric amount.")
            AmountEntry.focus()
        
        else:
            f = open("User Data.txt","r")
            info = f.read()
            info = info.split()
            if retainUsername in info:
                index = info.index(retainUsername) + 2
                oldAmount = info[index].replace("R","")
            accountHolder = retainUsername
            transactionNumber = str(random.randint(000000, 999999))
            f.close()
            
            newAmount = float(oldAmount) + float(depositAmount)
            f = open("User Data.txt", "w")
            info[index] = str("R" + "%.2f" % float(newAmount))
            info = "\n".join(info)
            f.writelines(info)
            f.close()
                
            f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "r")
            info2 = f2.read()
            f2.seek(0)
            f2.close()              
                      
            f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "a+")
            if len(info2) > 0 :
                f2.write("\n" + "\n")
            log_string = str("Transaction Type: " + str(transactionType) + "\n" + "Transaction Number: " + str(transactionNumber) + "\n" + "Account Owner: " + str(accountHolder) + "\n" + "Date of Transaction: " + str(datetime_object) + "\n" + "Previous Amount: R" + "%.2f" % float(oldAmount) + "\n" + "Deposited Amount: R" + "%.2f" % float(depositAmount) + "\n" + "New Amount: R" + "%.2f" % float(newAmount))
            f2.write(str(log_string))
            f2.close()
            messagebox.showinfo(title="Welcome",message="Deposit successful, check balance and transactions for updated details.")
        

    def withdrawMoney(self):
        transactionType = "Withdrawal"
        withdrawAmount = str(AmountEntry.get())
        if withdrawAmount.isnumeric() == False:
            messagebox.showerror(title="error",message="Please enter an appropriate numeric amount.")
            AmountEntry.focus()

        else:

            f = open("User Data.txt","r")
            info = f.read()
            info = info.split()
            if retainUsername in info:
                index = info.index(retainUsername) + 2
                oldAmount = info[index].replace("R","")
            if float(withdrawAmount) > float(oldAmount):
                messagebox.showerror(title="error",message="Insufficient balance, please enter a sufficient balance.")
                AmountEntry.focus()
            else:
                accountHolder = retainUsername
                transactionNumber = str(random.randint(000000, 999999))
                f.close()
                
                newAmount = float(oldAmount) - float(withdrawAmount)
                f = open("User Data.txt", "w")
                info[index] = str("R" + "%.2f" % float(newAmount))
                info = "\n".join(info)
                f.writelines(info)
                f.close()

                f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "r")
                                
                info2 = f2.read()
                f2.seek(0)
                f2.close()
                                
                f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "a+")
                if len(info2) > 0 :
                    f2.write("\n" + "\n")
                log_string = str("Transaction Type: " + str(transactionType) + "\n" + "Transaction Number: " + str(transactionNumber) + "\n" + "Account Owner: " + str(accountHolder) + "\n" + "Date of Transaction: " + str(datetime_object) + "\n" + "Previous Amount: R" + "%.2f" % float(oldAmount) + "\n" + "Withdrawal Amount: R" + "%.2f" % float(withdrawAmount) + "\n" + "New Amount: R" + "%.2f" % float(newAmount))
                f2.write(str(log_string))
                f2.close()
                messagebox.showinfo(title="Welcome",message="Withdrawal successful, check balance and transactions for updated details.")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()