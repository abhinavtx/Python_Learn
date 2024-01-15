class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):
        # Here self is for s1 meaning self class object
        # Here other means other class object
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        
        return s3
    
    # Similarly we can define these operator for other things like greater than
    def __gt__ (self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        return m1 > m2           
    
    def __str__(self) :
        return ("{} and {}".format(self.m1, self.m2))
s1 = Student(58,60)
s2 = Student(55,65)
s3 = s1 + s2
print(s3.m1)
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
    
print(s1)