"""" 
# There are 3 parameters here first the name of the file and then what is to be performed and then the encoding nature
f = open('test.txt', 'r')
# These letters like r, a or any other letter denote that what operations are to be performed on these files
print(f.name)
print(f.mode)
# Now we have to close the file explicitly to avoid memory leak
f.close()
"""

# Now if we use this appproach, this doesn't need file to be closed
with open('test.txt', 'r') as f:
    # The file will do all operations under this intendation only
    fContents = f.readline()
    fContents1 = f.readlines()
    print(fContents)
    print(f.read(10)) # This tells to read only 10 characters

    f.seek(0,0)
    # seek command is used to reset the pointer of file reader

# Now writing
with open('test2.txt', 'w') as f2:
    f2.write('This is a new test file')
    
# Similarly we can do this for images
# images are read and written in the form of bytes