import os 

# f = open('profile.txt','w')    # Write mode --- removes the previous comtent and start writing from start
f = open('profile.txt','a')       # append mode --- It will keep the previous data as it is and append the new data

f.write("I teach online.")

f.close()

"""
File :
My name is Arvinder Pal. 
I am a Python Tutor.

line = "I teach online."
write mode - 'w'

File: 
I teach online.

--------------------------------------------------------
append mode - 'a'
File:
My name is Arvinder Pal. 
I am a Python Tutor.
I teach online.

"""