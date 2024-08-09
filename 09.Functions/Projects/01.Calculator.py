num1 = int(input("Enetr a number: "))
num2 = int(input("Enetr the second number :"))

print(""" Welcome to Calculator Program :Enter
      1.Addition of two numbers
      2. Subtraction
      3. Multiplication
      4. Division
       """)
choice = input("Enter your choice :")

if choice=="1":
    print("The addition of two numbers is =", num1+num2)
elif choice=="2":
    print("The Subtract of two numbers is =", num1 - num2)
elif choice=="3":
    print("The Multiplication of two numbers is =", num1*num2)
elif choice=="4":
    print("The Division of two numbers is =", num1/num2)
else:
    print("INvalid Choice")

