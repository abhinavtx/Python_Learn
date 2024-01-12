# 1. TypeError
# Operation on different data types


x = 5
zt = 4
y = 'Hello'



try:
    # This section contains the segment which might contain an error
    zt /= 0  
    z = x + y
    c = x + 10

except Exception as e:
    print("The error is: ", e)
    # By this way we can know what the error was 
    """"
    except TypeError as te:
        print("TypeError, the reason is: ", te)
        
    except ZeroDivisionError as ze:
        print(ze)
    """   
else:   
    print(c)
    # Else is used to do the control if no error or no that type of error
finally:
    print("Abhinav is jod")   
    #  This will always be executed whether there is error or no error 
# Here we can just write except if we don't know what the error may be
# We can also have multiple types of exceptions     

# raise statement is used to explicitly raise an error 