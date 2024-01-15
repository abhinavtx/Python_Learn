# Using interator function

nums = [7,8,9,5]
it = iter(nums)
print(it.__next__()) # Start from index = 0
print(it.__next__()) # Now on index = 1
print(next(it))

class TopTen:
    def __init__(self):
        self.num = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        # If we don't use StopIteration command this will keep iterating till end
        if self.num <= 10:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration
    
values = TopTen()
for i in values:
    print(i)
 
    