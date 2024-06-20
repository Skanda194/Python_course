first = int(input("Enter the first number : "))
second = int(input("Enter the second number :" ))
choice = input(("Select any one option : \n\n 1. Addition \n 2. Subtract  \n 3. Multiply \n 4. Divide \n"))

# if choice == "1":
#     print("Sum of ",first ," and ", second ," is :",first+second)
# if choice =="2":
#     print("Difference of ", first ," and ",second , " is : ",first-second)

# if choice =="3":
#     print("Multiplication of ", first , " and ", second , " is : ",first*second)

# if choice =="4":
#     if second ==0:
#         print("Division with Zero is not possible.")
#     else: 
#         print("Division of ", first ," and ",second , " is :", first/second)


if choice == "1":
    print("Sum of ",first ," and ", second ," is :",first+second)
elif choice =="2":
    print("Difference of ", first ," and ",second , " is : ",first-second)
elif choice =="3":
    print("Multiplication of ", first , " and ", second , " is : ",first*second)
elif choice =="4":
    if second ==0:
        print("Division with Zero is not possible.")
    else: 
        print("Division of ", first ," and ",second , " is :", first/second)

else:
    print("Please Enter a valid option.")