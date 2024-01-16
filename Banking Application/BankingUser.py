# In this file we are creating a small interface for user to perform banking by giving input of numbers in terminal
from BankingMain import *

class bankChoose:
    def greetingHQ(self):
        print("Welcome to online banking system!")
        self.bName = str(input("Enter the name of your bank: "))
        self.bCity = str(input("Enter your city name: "))
        
        self.bankHQ = BankHead(self.bName, self.bCity)
        self.bankHQ.insertNewBranch()
        self.bankHQ.giveDetails()
        
        self.greetBranch()
    
    def newUserReg(self):
        print("Welcome New User")
        passw = int(input("Enter password in form of numbers: "))
        cPassw = int(input("Confirm password again: "))
        name = str(input("Enter your name: "))
        self.password = passw
        self.cPassword = cPassw
        self.Name = name
        self.bankBranch = BankBranch(self.password , self.cPassword, self.Name)
        
        if(self.bankBranch.passwordCheck()):
            self.bankBranch.insertNewAccount()
            self.bankBranch.Register()
            print("Now please login again!")
            self.greetUser()
        else:
            "Print incorrect credentials, try again"
            self.newUserReg()
            
    def greetBranch(self):
        print(f'Welcome to {self.bName} bank in {self.bCity} with branch code {self.bankHQ.newBranch}')
        n = int(input("Enter 1 for new user registration, 2 for existing user registration, 3 for city selection again and others for exit: "))

        if(n == 1):
            self.newUserReg()
        elif(n == 2):
            self.greetUser()
        elif(n == 3):
            self.greetingHQ()
        else:
            pass
    
    def greetUser(self):
        print("Welcome existing user")
        accNumber = str(input("Enter your account number: "))
        password = int(input("Enter your pasword: "))
        self.passw = password
        self.accNumber = accNumber
        
        while True:
            print("Input 1 for getting user details")
            print("Input 2 for deposit of money")
            print("Input 3 for withdrawl of money")
            print("Input 4 for taking loan")
            print("Input 5 for transfering money to a different account")
            print("Input any other number for exiting online banking")
            
            n = int(input("Enter a number for doing banking operations: "))
            if n == 1:
                print("---------------------------------------------------------")
                self.userActivity1 = UserTransaction(self.accNumber ,self.passw)
                self.userActivity1.printDetails()
                print("---------------------------------------------------------")
            elif n == 2:
                print("---------------------------------------------------------")
                addMoney = int(input("Input the amount of money to be added: "))
                self.addMoney = addMoney
                self.userActivity2 = UserTransaction(self.accNumber ,self.passw, self.addMoney)
                self.userActivity2.deposit()
                print("---------------------------------------------------------")
            elif n == 3:
                print("---------------------------------------------------------")
                withdrawMoney = int(input("Input the amount of money to be deducted: "))
                self.addMoney = -1* withdrawMoney
                self.userActivity3 = UserTransaction(self.accNumber ,self.passw, self.addMoney)
                if(not self.userActivity3.canWithdarw()):
                    print("Give a correct amount again: ")
                    continue
                self.userActivity3.withdraw()
                print("---------------------------------------------------------")
            elif n == 4:
                print("---------------------------------------------------------")
                takeLoan = int(input("Enter the amount of loan to be taken"))
                self.addLoan = takeLoan
                self.userActivity4 = UserTransaction(self.accNumber, self.passw, None, self.addLoan)
                if(not self.userActivity4.canTakeLoan()):
                    print("Give a correct loan amount")
                    continue
                self.userActivity4.takeLoan()
                print("---------------------------------------------------------")
            elif n == 5:
                print("---------------------------------------------------------")
                payeaeAcc = str(input("Enter the account number of payee: "))
                payeeMoney = int(input("Enter the amount of money to be transferred: "))
                self.userActivity5 = UserTransaction(self.accNumber ,self.passw, None, None, self.payeeAccount, self.payyeMoney)
                self.payeeAccount = payeaeAcc
                self.payyeMoney = payeeMoney
                if(not self.userActivity5.canTransfer()):
                    print("Can't transfer give correct credentials")
                self.userActivity5.transfer()
                print("---------------------------------------------------------")
            else:
                print("Happy Banking")
                break

if __name__ == '__main__':
    solutionBank = bankChoose()
    solutionBank.greetingHQ()