from BankData import *
import random
import string
from datetime import datetime

class BankHead:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    newBranch = ''
    def makeNewBranch(self):
        num = 0
        random_alphabet = random.choice(string.ascii_letters)
        for i in range(2):
            random_number = random.randint(1, 9)
            num +=  10**(1-i) * random_number
        bBranch = str(random_alphabet) + str(num)
        return bBranch
    
    def insertNewBranch(self):
        self.newBranch = self.makeNewBranch()
        while(self.newBranch in BankBranches):
            self.newBranch = self.makeNewBranch()    
        BankBranches.update({self.city : self.newBranch})
        print(self.newBranch)
    
    def giveDetails(self):
        print(f'The details of bank are {self.name} and it has its branches in {BankBranches[self.city]}')


class BankBranch:
    newAccount = ''
    def __init__(self, password = None, cPassword = None, Name = None) :
        self.__password = password
        self.__cPassword = cPassword
        self.Name =Name
        #BankHead().__init__(name, city)
    
    def makeNewAccount(self):
        num = 0
        random_alphabet = random.choice(string.ascii_letters)
        for i in range(3):
            random_number = random.randint(1, 9)
            num +=  10**(2-i) * random_number
        accountNum = str(random_alphabet) + str(num)
        return accountNum
    
    def insertNewAccount(self):
        self.newAccount = self.makeNewAccount()
        while(self.newAccount in UserAccount):
            self.newAccount = self.makeNewAccount()    
        UserAccountCode.add(self.newAccount)
        print(f'New Account registered with account number as {self.newAccount}')
    
    def passwordCheck(self):
        if self.__password == self.__cPassword:
            return True
        return False
    
    def Register(self):
        if(self.passwordCheck() and self.newAccount != ''):
            loginDetails.update({self.newAccount : self.__password})
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            userDetails = {'Name' : str(self.Name), 'balance' : 0, 'Loan' : 0, 'loginTime' : formatted_datetime}
            UserAccount.update({self.newAccount : userDetails})
            print("Registration successfuly done!")
            for k,v in UserAccount[self.newAccount].items():
                print(f'{k} is {v}', end =' and ')
            print('')
        else:
            print("Registration not done please check if password and confirm Password are same")
    
class UserTransaction:
    bankLoan = 1000000
    def __init__(self, accNumber, password, addMoney = None, addLoan = None, payeeAccount = None, payeeMoney= None) :
        self.__password = password
        self.accNumber = accNumber
        self.__addMoney = addMoney
        self.__payeeAccount = payeeAccount
        self.__payeeMoney = payeeMoney
        self.__addLoan = addLoan
        
    def login(self):
        if self.accNumber not in UserAccountCode:
            print("Login failed, try again")
            return False
        elif loginDetails[self.accNumber] != self.__password :
            print("Login failed, try again")
            return False
        else:
            print("Successfully logged in")
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            UserAccount[self.accNumber]['loginTime'] = formatted_datetime
            return True
        
        
    def deposit(self):
        UserAccount[self.accNumber]['balance'] += self.__addMoney
        # We are also keeping a track of loan for bank
        # So taking 10% of the deposit for bank loan but not deducting that money
        self.bankLoan += (0.1 *self.__addMoney)
        print(f'Deposited {self.__addMoney} into {self.accNumber} account, updated balance is {UserAccount[self.accNumber]['balance']}')
    
    def canWithdarw(self):
        return (UserAccount[self.accNumber]['balance'] > (-1*self.__addMoney))
    
    def withdraw(self):
        if(self.canWithdarw()):
            UserAccount[self.accNumber]['balance'] += self.__addMoney
            # We are also keeping a track of loan for bank
            # So taking 10% of the deposit for bank loan but not deducting that money
            self.bankLoan += (0.1 *self.__addMoney)
            temp = -1* self.__addMoney
            print(f'Withdrawl of {temp} money done from {self.accNumber} account, updated balance is {UserAccount[self.accNumber]['balance']}')
        else:
            print("Withdrawl not performed please check the withdrwal money")
            
    def canTransfer(self):
        if (self.__payeeAccount not in UserAccountCode):
            return False
        elif self.__payeeMoney > UserAccount[self.accNumber]['balance']:
            return False
        return True
    
    def canTakeLoan(self):
        return (self.__addLoan < UserAccount[self.accNumber]['balance'] and self.__addLoan != None)
    
    def takeLoan(self):
        if(self.canTakeLoan()):
            UserAccount[self.accNumber]['loan'] += self.__addLoan
            self.bankLoan -= self.__addLoan
            print("Loan money of {} added in your loan account with account number {}".format(self.__addLoan, self.accNumber))
        else:
            print("Loan not granted, give some eligible money amount")
    
    def transfer(self):
        if self.canTransfer():
            UserAccount[self.accNumber]['balance'] -= self.__payeeMoney
            UserAccount[self.__payeeAccount]['balance'] += self.__payeeMoney
            print("The transaction is done")
            print(f'Deducted {self.__payeeMoney} from {self.accNumber} and transferred to {self.__payeeAccount}, updated balance is {UserAccount[self.accNumber]['balance']}')
        else:
            print("Transaction not done, check credentials or check the amount of transfer money")
        
    def printDetails(self):    
        for k,v in UserAccount[self.accNumber].items():
            print(f'{k} is {v}', end =' and ')
        print('')
        if(self.__payeeAccount != None):
            for k,v in UserAccount[self.__payeeAccount].items():
                if(k == 'loginTime'):
                    print(f'{k} is {v}')
                    continue
                print(f'{k} is {v}', end =' and ')
    
if __name__ == "__main__":
    bankBranch1 = BankBranch(1234, 1234, 'Ram')
    bankBranch1.insertNewAccount()
    bankBranch1.Register()
        
    userTransact = UserTransaction('R123', 1234, -100, )
    userTransact.login()
    userTransact.moneyOperation()
    userTransact.printDetails()
    for k,v in UserAccount.items():
        print(k,v)