# Calculator

def calculator():
    first = int(input("Enter first Number :"))
    second = int(input("Enter second Number : "))
    print('''
    What do you want to do with these numbers:
        Enter 1. To add  2. To Subtract 3. To Multiply  4. To Divide
''')
    choice = int(input())

    if choice==1:
        add(first, second)
    elif choice ==2:
        sub(first, second)

def add(first,second):
    print("The sum of ",first , " and ", second, " is ", first+second)

def sub(first,second):
    print("The subtraction of ",first , " and ", second, " is ", first - second)



calculator()