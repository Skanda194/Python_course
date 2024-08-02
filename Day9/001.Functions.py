# Fuctions - block of code that can be executed together

# Task - 1 : Greet every coming member with "Good Morning"

# print("Good Morning") 
# print("Good Morning")
# print("Good Morning")
# print("Good Morning")
# print("Good Morning")
# print("Good Morning")

# Using loops 
# for i in range(10):
#     print("Good Morning")

# Defining  a function
def myGreet():
    print("Good Morning")

# Calling a fnction
# myGreet()
# myGreet()

# Paasing values to functions - Parameters
def GreetUser(name):
    print("Good Morning ",name)

# GreetUser("Arvinder")
# GreetUser("Skanda")

# Adding two numbers

def AddNumbers(first, second):
    print("The sum of two numebrs is :", first + second)
# AddNumbers(10,20)
# AddNumbers(100,210)

# User information display
def UserDetails(name, age , college , education,rollNum,city, country):
    print("------- User Card ----------")
    print("Name: ", name)
    print("Age: ", age)
    print("College: ", college)
    print("Education: ", education)
    print("Roll Number: ", rollNum)
    print("City: ", city)
    print("Name: ", country)

UserDetails("Skanda",12,"ABC","XYZ",1234,"DEF","TEG")


# DRY Principle - Do not repeat Yourself