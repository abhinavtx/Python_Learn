from BankData import *
import random
import string


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
    def __init__(self, name, city) :
        BankHead().__init__(name, city)
        self.userName = userName
        
    def makeNewAccount(self):
        num = 0
        random_alphabet = random.choice(string.ascii_letters)
        for i in range(3):
            random_number = random.randint(1, 9)
            num +=  10**(2-i) * random_number
        newAccount = str(random_alphabet) + str(num)
        return newAccount
    
    def insertNewAccount(self):
        newAccount = self.makeNewAccount()
        while(newAccount in UserAccount):
            newAccount = self.makeNewAccount()    
        UserAccountCode.add(newAccount)
        #BankBranch.update({self.city : newAccount})
        print(BankBranch)
    

class UserTransaction:
    def __init__(self, userName, balance, loan) :
        self.userName = userName
        self.balance = balance
        self.loan = loan
        