# An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values.

class computer:
    
    def __init__(self):
        # The work of __init__ is for constructor
        # Every time an object is made then the constructor will be called
        # self is used as an instance to the class
        self.cpu = "i5"
        self.ram = 16
        print("Constructor Called")
        
    def compare(self, other):
        return (self.cpu == other.cpu)
    
    def config(self):
        print(self.cpu)
        
    def updateCpu(self):
        temp = input("Enter the CPU:")
        self.cpu = temp
    
    def __del__(self):
        print("Destructor Called")
        
com1 = computer() # Intitalised the object using default Constructor
com2 = computer() 

print(com1.compare(com2))
com2.updateCpu()
print(com1.compare(com2))
# Destructor called automatically after program execution
# Explicitly calling Destructor command -> del com2
    