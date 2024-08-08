# Functions will be excecuted in the order of calling.

# def f1():
#     print("f1")

# def f2():
#     print("f2")

# def f3():
#     print("f3")

# f2()
# f1()
# f3()

# One function can call the another function.

# def f1():
#     print("f1")

# def f2():
#     print("f2")
#     f1()

# def f3():
#     print("f3")

# f2()
# f3()


# def f1():
#     print("f1")

# def f2():
#     f1()
#     print("f2")

# def f3():
#     print("f3")

# FUnction calls get stored in stack
# f2()
# f3()

# Call Stack  
#       f1
# f2    f2  


# return - functions can return a value 
# When we call a function it will return some value to its caller function

# Block /Functional - Local  - Bike , Family Car 
# GLocal Scope               - Public Transport

# Sum = 20
# def Add():
#     Sum = 20+30
#     print(Sum)

# Add()
# print(Sum)

# Sum = 20
def Add():
    Sum = 20+30
    return Sum
    # print(Sum)

x = Add()
print(x)

def PrintDetails(fname , lname):
    fullName = fname + " " + lname
    # print(fullName)
    return fullName
    # print("Hello")

# Whatever is return after return statement will not get executed
name = PrintDetails("Arvinder","XYZ")
print(name)


def MaxTwoNumbers(a,b):
    if a>b:
        return a 
    else:
        return b
    
max = MaxTwoNumbers(45,130)
print(max)
