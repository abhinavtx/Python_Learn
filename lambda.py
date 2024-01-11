# Functions are also objects in python
# lambda expressions are used to make a function which is to be used only once

# So lambda is used to make a function for instantaneous use
# It is used within another functions
f = lambda a,b : a * b
result = f(5,6)
print(result) 

# Usage of filter function
# This function filters on the basis of 

nums = [1,4,5,6,7,8,9]
nums2 = [1,4,5,6,7,8,9]
even = list(filter(lambda n : n % 2 == 0, nums))
updateNum = list(map(lambda n : n + 2, nums2))
print(even)
print(updateNum)

## Now for using sorting we could also use lambda
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key= lambda i : i[1])
print(pairs)
