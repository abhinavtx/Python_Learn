## Method Overloading
# In this same function can have different number of arguements
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self, a = None, b = None, c = None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s
    # Here None means even if we don't put a value in these, they will be replaced by None
    
s1 = Student(58,65)

a = s1.sum(4,5)
b = s1.sum(4,5,6)

print("The first is {} and second is {}".format(a, b))


# Now doing Method Overriding
# Process of re-implementing a method in the child class is known as Method Overriding. 
class Bird:
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
        
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
