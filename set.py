s = {1,5,7,8,9}
print(s)
# Indexing is not supported in set
# They are unordered
# It contains only unique values

# But in sets we can iterate in set using a loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# This print will not be in the exact order as of set
# Checking if an item in set
print("banana" in thisset)

thisset.add("Orange")
#Adding element in set
thisset.update(s)
print(thisset)

thisset.remove("banana")
# This will remove from the set

# This can also be used by discard() function
# The difference between remove and discard() is that for no item present it will give an error and for discard() no error

# Set also has functions of union, update, intersection

alpha = set('abracadabra')
abc = list(alpha.copy())
print(f"These are the contents of {abc}")