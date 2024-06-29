z=int(input(" Enter a a percentage: "))
if z>=0:
    if z>=90:
        print("The letter grade is a A")
    elif z>=80:
        print("The letter grade is a B")
    elif z>=65:
        print("The letter grade is a C")
    elif z>55:
        print("The letter grade is a D")
    else:
        print("The letter grade is a F")
else:
    print("Error you can't enter this low of a letter grade")
    
    
    