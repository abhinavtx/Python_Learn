#capability of one class to derive or inherit the properties from another class
#Types: 1.Single 2.Multilevel 3.Hierarchical 4.Multiple Inheritance

class Vehicle(object):
    def __init__(self, ids):
        self.tyres = 4
        self.ids = ids
        
    def details(self):
        print(f'The id of vehicle is: {self.id}')
        print(f'The number of tyres are : {self.tyres}')
        
        
# ----note-> We have to use 
        
class Car(Vehicle):
    def __init__(self, model):
        self.model = model
        
        super().__init__(45)
        # This is the syntax for inherited class
        # Where Vehicle is the parent of Car class
         
    def printDetails(self):
        print(f'The id is: {self.ids}')       
        print(f'The model is: {self.model}')       
        print(f'The number of tyres are: {self.tyres}') 
    
crv = Car(2009)
Vehicle1 = Vehicle(1234)

Vehicle1.details()
crv.printDetails()


## Creation of private member
# Use command: While making constructor and initialising value
# self.__d = 456

class school(object):
    def __init__(self, name) :
        self.name = name
        self.__id = 45