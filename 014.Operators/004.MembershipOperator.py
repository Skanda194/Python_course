# Memmbership Operator : these are used to check whether a value or element exists within a sequence like a list , tuple , string or dictionary.


# in , not in 

# 1,2,3,4,5,6,7,8,9 -- List of numbers 
# 9 in list -- yes (True)

# 10 in list --- False

# 9 not in list -- False 
# 10 not in list --- True

cars=['BMW','AUDI','Skoda','Toyota']
print('Ford' in cars)  # False

print('AUDI' in cars)   #True

print('Ford' not in cars) #True

print('AUDI' not in cars)  #False



print("--------------------------------------------")

# Grade 8
students= ['Rahul','John','Smith','Cathy','Ramesh','Ching','Bill']

#print('Girish' in students)  # False
newName = 'Girish'
if newName in students:
    print(newName ," studies in grdae 8.")
else:
    print(newName ," does not study in grade 8.")

