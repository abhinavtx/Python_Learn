# 1. OS module for interacting with  OS
import os
pid = os.getpid()
print(pid)
#print(dir(os))

# 2. Usage of glob library for wildcard matching
import glob

# Example: Get a list of all text files in the current directory
text_files = glob.glob('*.txt')
print("These are all the text files in the current directory", end= ' ')
print(text_files)

#3. Usage of re (regular expression) module which helps in pattern seaching
import re

pattern = r'\b\w{3}\b'  # Matches three-letter words
pattern2 = r'The' #Matches the word the
text = 'The cat is on the mat.'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern2, text)
print("The macthes are respectively {} and {}".format(matches, matches2))

#4. Usage of Math library
from math import *
print(ceil(pi))
print(log(1024,155))

# Usage of random library -> For choosing random selections
# Creating a unique user id 
import random
import string
def NewUser():
    num = 0
    random_alphabet = random.choice(string.ascii_letters)
    for i in range(3):
        random_number = random.randint(1, 9)
        num +=  10**(2-i) * random_number
    user = random_alphabet + str(num)
    return user
  
userData = set()

abc = NewUser()
while(abc in userData):
    abc = NewUser
userData.add(abc)
print(abc)
print(userData)

# Usage of date and time lbrary python
import datetime
currDate = datetime.datetime.now()
print(currDate)