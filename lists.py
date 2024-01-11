list1 = [1,5,6,7,5,8]
list1.insert(4,21)
# Insert 21 at 4th index
# For using extend it is used to concatenate 2 lists
## By default list perform like stack --> Using append and pop functions
list1.pop()
print(list1)



list1.pop(1)
# But for this function it removes first 1 from the front
# Similarly for list1.remove(1). If not there gives ValueError
print(list1)

list2 = list1.copy()  ## Returns a shallow copy of the list
# For updation of whole list use map function with lambda

# -- List Comprehension --
# making a list using loop
temp = [(x, x**2) for x in range(1,6)]
print(temp)