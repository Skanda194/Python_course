#Order of execution of functions 

# def Noon():
#     print("Good Afternoon !!!!")

# def Greet():
#     print("Good Morning !!!!!!")

# Greet()
# Noon()


# The order odf execution depends upon the order of calling the function
def func1():
    print("I am in func1.....")

def func2():
    print("I am in func2....")
    func3()                        #function inside another function  --  Nested function
    print("func2 is completed")

def func3():
    print("func3 is called....")

# func1()
# func2()

# Another example 

def first():
    print("I am in first function. Going to second ....")
    second()          
    print("Completed - first")

def second():
    print("I am in second function. Going to fourth .....")
    fourth()            
    print("Completed - second")

def fourth():
    print("I am tired now. Not going anywhere.")

def third():
    print("I am third function.")

third()
first()

