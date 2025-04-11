import json
def Calculator(a,b):
    y=int(input("press 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: "))
    result=json.dumps(y)
    if y==1:
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("Your answer will be:",a+b)
    elif y==2:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Your answer will be:",a-b)
    elif y==3:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Your answer will be:",a*b)
    elif y==4:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Your answer will be:",a/b)
    else:
        ValueError("Your response is invalid")




