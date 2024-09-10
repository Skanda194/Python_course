import os  #Operating System 

f = open('test.txt','r')
# filename , mode 

# TO read the whole content
# print(f.read())

# to read first character lines of the file
# print(f.read(5))

# print(f.readline())
# print(f.readline())

for x in f:
    print(x)

f.close()