#CONDITIONALS AND LOOPS
#1
# y=int(input("Enter a Number: "))
# if y<0:
#     print("the number is negative")
# elif y>0:
#     print("Positive")
# else:
#   print("neither")
#2
# y=int(input("enter a year"))
# if y%4==0:
#     print("leap year")
# else:
#     print("not a leap year")
#3
# y=int(input("Enter your score: "))
# if y<100 and y>89:
#     print("A")
# elif y<90 and y>79:
#     print("B")
# elif y<80 and y>69:
#     print("C")
# elif y<70 and y>59:
#     print("D")
# elif y>100:
#     print(ValueError("Answer is invalid"))
# else:
#     print("F")
#4
# y=input("Enter a word: ")
# y2=y[::-1]
# if y == y2:
#     print("palindrome")
# else:
#     print("Not a palindrome")
#5
# for i in range (1,11):
#     print(i)
# i=i+1
#6
# def factorial_while_loop(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n == 0:
#         return 1
#     else:
#         result = 1
#         while n > 0:
#             result *= n
#             n -= 1
#         return result
# number = 5
# factorial_of_number = factorial_while_loop(number)
# print(f"The factorial of {number} is {factorial_of_number}") # Output: The factorial of 5 is 120
#
# number = 0
# factorial_of_number = factorial_while_loop(number)
# print(f"The factorial of {number} is {factorial_of_number}") # Output: The factorial of 0 is 1
#
# number = -1
# factorial_of_number = factorial_while_loop(number)
# print(f"The factorial of {number} is {factorial_of_number}") # Output: The factorial of -1 is Factorial is not defined for negative numbers
#7
# y=float(input("enter a number: "))
# for i in range (1,11):
#     print(y*i)
#     i=i+1
#8
# y=101
# for i in range(1,y):
#    print(i)
#    i=i+1
#10
# y=input("enter a word: ")
# for i in y:
#     i=y[::-1]
#     print(i)