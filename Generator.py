# yield keyword is used to return a generator
# generator gives an iterator

def topTen():
    yield 1
    yield 2
    yield 3
    
values = topTen()
for i in values:
    print(values)