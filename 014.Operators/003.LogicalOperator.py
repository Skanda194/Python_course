#Logical operators - used to combine conditional statements.


# Driving License : Age > 18 , Pass the driving test 

# div by 5 and 3 
# div 3 
# div 5
# none 
# number = 30
# if number %3==0 and number %5==0:
#     print(number ,"is divisible by 3 and 5")
# elif number %3==0:
#     print("divisible with 3")
# elif number %5==0:
#     print("Divisible with 5")
# else:
#     print("Not divisible with 5 and 3")

# Truth Table for AND
# Condtion 1 and Condition 2 : Result
# True and True              : True       Case 1
# False and True             : False      Case 2    
# True   and False           : False      Case 3
# False and False            : False      Case 4

x =30
print("---------------------- AND OPERATOR ---------------------------")
#Case 1
if x>20 and x<40:
    print("Case 1: True")

#Case 2
if x<20 and x<40:
    print(x)
else:
    print("Case 2: False")

#Case 3
if x>20 and x>40:
    print(x)
else:
    print("Case 3: False")

#Case 4
if x<20 and x>40:
    print(x)
else:
    print("Case 4: False")



#OR operator - atleast one true condition is required

# Truth Table for OR
# Condtion 1 and Condition 2 : Result
# True or True               : True       Case 1
# False or True              : True       Case 2    
# True   or False            : True       Case 3
# False or False             : False      Case 4

print("---------------------- OR OPERATOR ---------------------------")
x =35
#Case 1
if x>20 or x<40:
    print("Case 1: True")

#Case 2
if x<20 or x<40:
    print("Case 2: True")  
else:
    print(x)
    

#Case 3
if x>20 or x>40:
    print("Case 3: True")
else:
    print(x)
    

#Case 4
if x<20 or x>40:
    print(x)
else:
    print("Case 4: False")



# Not Operator - 

# Truth Table for OR
# Condtion 1  : Result
# True              : False       Case 1
# False             : True        Case 2
# 
#  
print("---------------------- NOT OPERATOR ---------------------------")   
number = 40
if not (number ==40):
    print("it is not equal to 40")
else:
    print("equal to 40")


if not (number !=40):
    print("it is not equal to 40")
else:
    print("equal to 40")