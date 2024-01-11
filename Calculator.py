def add(a,*b):
    c = a
    for i in b:
        c += i
    return c

def multiply(a,*b):
    c = a
    for i in b:
        c *= i
    return c

def subtract(a,*b):
    c = a
    for i in b:
        c -= i
    return c

def division(a,*b):
    c = a
    for i in b:
        c /= i
    return c
