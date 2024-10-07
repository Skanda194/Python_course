# Iterative style --  loops are there to do any repeating task
# Recursive Style ---- Where we use function to perform s repeating task

# Recursrion - A function calling itslef.
# def Hello():
#     print("I am in Hello function")

# def Greet():
#     print("Hello")
#     Greet()

# Greet()

# Base condition --- It is a condition to stop the code execution.


# def Increasing_Order(start, end):
#     if start > end:   
#         return
#     else:
#         print(start, end=" ")
#         Increasing_Order(start+1,end)
        

# Increasing_Order(1,10)

def Decreasing_Order(start, end):
    if start > end:   
        return
    else:
        Decreasing_Order(start+1,end)
        print(start, end=" ")
Decreasing_Order(1,10)
# Call Stack --

# 10 9 8 7 6 5 4 3 2 1 
