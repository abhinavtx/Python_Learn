
BankBranchcode = {'x52', 'x23'}
BankBranch = {'Chandigarh' : 'x52', 'Delhi' : 'd23'}
UserAccountCode = {'R123', 'A456'}
UserAccount = {'R123' : { 'Name' : 'Abhinav', 'balance' :100000, 'Loan' : 0, 'time' : '2024-01-16 11:59:25'}, 'A456' : { 'Name' : 'Rahul', 'Balance' :1000, 'Loan' : 100, 'time' : '2024-01-15 10:59:25'}}
loginDetails = {'R123' : 1234, 'A456' : 2315}
bankLoan = 1000000

from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the current date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", formatted_datetime)
print(type(formatted_datetime))
print(type('Abhinav'))
