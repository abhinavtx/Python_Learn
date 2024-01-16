from BankData import *
import random
import string
from datetime import datetime

class BankHead:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        
    def makeNewBranch(self):
        num = 0
        random_alphabet = random.choice(string.ascii_letters)
        for i in range(2):
            random_number = random.randint(1, 9)
            num +=  10**(1-i) * random_number
        bBranch = str(random_alphabet) + str(num)
        return bBranch
    
    def insertNewBranch(self):
        newBranch = self.makeNewBranch()
        while(newBranch in BankBranch):
            newBranch = self.makeNewBranch()    
        BankBranch.update({self.city : newBranch})
        print(BankBranch)
    
    def giveDetails(self):
        print(f'The details of bank are {self.name} and it has its branches in {BankBranch[self.city]}')


class BankBranch:
    newAccount = ''
    def __init__(self, name, city, password = None, cPassword = None, Name = None) :
        self.__password = password
        self.__cPassword = cPassword
        self.Name =Name
        BankHead().__init__(name, city)
    
    def makeNewAccount(self):
        num = 0
        random_alphabet = random.choice(string.ascii_letters)
        for i in range(3):
            random_number = random.randint(1, 9)
            num +=  10**(2-i) * random_number
        newAccount = str(random_alphabet) + str(num)
        return newAccount
    
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
        if(self.passwordCheck()):
            loginDetails.update({self.newAccount : self.__password})
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            userDetails = {'Name' : str(self.Name), 'balance' : 0, 'Loan' : 0, 'time' : formatted_datetime}
            UserAccount.update({self.newAccount : userDetails})
            
        else:
            print("Registration not done please check if password and confirm Password are same")
    
class UserTransaction:
    def __init__(self, accNumber, password, addMoney, payeeAccount, payeeMoney, addLoan) :
        self.__password = password
        self.accNumber = accNumber
        self.__addMoney = addMoney
        self.__payeeAccount = payeeAccount
        self.__payeeMoney = payeeMoney
        self.__addLoan = addLoan
        
    def login(self):
        if self.accNumber not in UserAccountCode:
            return False
        elif loginDetails[self.accNumber] != self.__password :
            return False
        else:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            UserAccount[self.accNumber['time']] = formatted_datetime
            return True
    
    def register(self):
        loginDetails.update({self.accNumber : self.__password})
        
    def deposit(self):
        UserAccount[self.accNumber['balance']] += self.__addMoney
        # We are also keeping a track of loan for bank
        # So taking 10% of the deposit for bank loan but not deducting that money
        bankLoan += (0.1 *self.__addMoney)
    
    def canWithdarw(self):
        return (UserAccount[self.accNumber['balance']] < self.__addMoney)
    
    def withdraw(self):
        if(self.canWithdarw()):
            UserAccount[self.accNumber['balance']] -= self.__addMoney
            # We are also keeping a track of loan for bank
            # So taking 10% of the deposit for bank loan but not deducting that money
            bankLoan -= (0.1 *self.__addMoney)
        else:
            print("Withdrawl not performed please check the withdrwal money")
    def canTransfer(self):
        if (self.__payeeAccount not in UserAccountCode):
            return False
        elif self.__payeeMoney > UserAccount[self.accNumber['balance']]:
            return False
        return True
    
    def canTakeLoan(self):
        if(self.__addLoan > UserAccount[self.accNumber['balance']]):
            return False
        return True
    
    def takeLoan(self):
        if(self.canTakeLoan()):
            UserAccount[self.accNumber['loan']] += self.__addLoan
            print("Loan money of {} added in your loan account".format(self.__addLoan))
        else:
            print("Loan not granted, give some eligible ")
    
    def transfer(self):
        if self.canTransfer():
            UserAccount[self.accNumber['balance']] -= self.__payeeMoney
            UserAccount[self.__payeeAccount['balance']] += self.__payeeMoney
            print("The transaction is done")
        else:
            print("Transaction not done check credentials or the transfer money")
        
    def printDetails(self):
        print(f'The name of Account holder is {UserAccount[self.accNumber['Name']]} and balance is {UserAccount[self.__payeeAccount['balance']]}')
        print(f'The loan taken by Account holder is {UserAccount[self.accNumber['Loan']]}')
        print(f'The amount in bankloan now is {bankLoan}')
        print(f'The last login time of account holder was {UserAccount[self.accNumber['time']]}')

