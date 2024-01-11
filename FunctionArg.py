# Two concepts pass by reference -> address -> any chnage, change original value and pass by value -> value
# In python none of them is used.
# Python passes arguments neither by reference nor by value, but by assignment.
# This all is for arguements in functions
i = 6
i-=1

def f(arg=i):
    print(arg)
    print(id(arg))
i += 1
f(i)


# Variable length arguement
def sum(*b):
    ## Here b is a tuple which means while writing function we only have 2 agruements
    # When we are calling the function then besides a we can add many arguements
    # So 1 * means just variable length arguement
    c = 0
    for i in b:
        c += i
        # This i work in the form of an iterator
    print(c)
        
sum(5,4,6,8)

# Keyword variable length arguement

def person(name, **data):
    # Here 2 * means for keyword variable length arguement ---> Known as kwargs
    print(name)
    print(data)
    
    for i,j in data.items():
        print(f"{i} : {j}") 
    
person('Abhinav', age = 21, city = 'Chandigarh', mobile = 8837721062 )