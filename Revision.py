# Recursion 
# Type Casting 
# Return Keyword


# From Starting , DS (List , Tuples , Dictionaries , Sets) , Functions , Loops , Conditionals

# Recursion - 

# def Hello():
#   print("Hello Called")

# def Second():
#   Hello()     # called 
#   print("Second called")
  
  
# Second()  # Caller Function

#Hello()

#  Recursion - A function calling itself is called recursion.

#  The problem should get smaller with the consecutive calls 
#  AT one o=point it should get resolved (There should be a base case)

# def Number(n):
#   if n == 0:
#     return 
#   print(n)
#   return Number(n-1)

# Number(5)
  
# Return -- It represents the ending of the code. It shows this is the last line of the code and anything written after will not be executed.

#  It returns a copy of the local variables outside the function.

# def Sum(a,b):
#   result = a+b
#   print(result)
#   return result

# final = Sum(10,20)

# print(final+100)

# def increement(number):
#   number+= number
#   print(number)
#   # return number

# print(number)
# increement(10)
# print(number + 100)

# Type casting /conversion :
# x = 100.22
# print(int(x))

# Unpacking -- 
tuple1 = ("Apple","Ball","Cat","Dog")
print(tuple1)
# print(tuple1[0])
# a , b,  c, d = tuple1
# a , *b, d = tuple1
a , *b = tuple1
print(a)
print(b)
# print(c)
# print(d)
