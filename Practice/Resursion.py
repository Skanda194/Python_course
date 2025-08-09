
# def Hello():
#     print("Hello")

# Hello()


# def First():
#     print("First")
#     Second()

# def Second():
#     print("Second")

# First()

# Recursive Approach
# def PrintNumber(n):
# # Base Condition
#     if n >=5:
#         return 
#     print(n, end=" ")

# # Recursive Function Call
#     PrintNumber(n+1)

# PrintNumber(0)


# Iterative Approach
# for i in range(5):
#     print(i)


# 
print("-------------")
# def PrintNumber(n):
#     if n>=5:
#         return 
#     PrintNumber(n+1)
#     print(n, end=" ")

# PrintNumber(0)    


# Sum of all the elements of a list

# def SumOfElements(myList):
#     total = 0
#     for i in myList:
#         total+= i
#     return total 
# myList = [12,23,45,43,21,76]
# print(SumOfElements(myList))


# def SumOfElem(myList):
     
#     if not myList:
#         return 0

#     return myList[0]+SumOfElem(myList[1:])

# myList = [12,23,45,43,21,76]
# print(SumOfElem(myList))