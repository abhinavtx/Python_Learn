# Collection of ordered items
# Use key value pair
# Key should be immutable
names = {1: 'Abhinav', 2:'Kiran', 3:'Harsh'}
print(names[3])
print(names)

print(names.get(1, 'Not Found'))
print(names.get(4, 'Not Found')) 
names.update({4:'Aggarwal'})
print(names.keys())
keys = ['Abhinav', 'Kiran', 'Harsh']
values = ['Java', 'Python', 'PHP']
names.pop({4:'Aggarwal'})
data = dict(zip(keys,values))
# Zip is first used to associate in the form of key and values
# Then dict make dictionary
print(data)


## For copying a dictionary
# This will make a copy of names dictionary and assign it to mydict
mydict = names.copy()
print(mydict)
mydict2 = dict(names)
print(mydict)

# For all other data types also use this approach