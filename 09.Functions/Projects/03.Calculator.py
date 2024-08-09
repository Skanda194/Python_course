def PrintingOptions():
    print(""" Welcome to Calculator Program :Enter
      1.Addition of two numbers
      2. Subtraction
      3. Multiplication
      4. Division
       """)

def Add(num1, num2):
    result = num1 + num2
    return result

def Sub(num1, num2):
    result = num1 - num2
    return result 

def Multi(num1, num2):
    result = num1 * num2
    return result

def Div(num1, num2):
    result = num1/num2
    return result
    

num1 = int(input("Enetr First number: "))
num2 = int(input("Enetr the second number :"))
PrintingOptions()
choice = input("Enter your choice :")
    
if choice=="1":
    result = Add(num1, num2)
    print("The addition of two numbers is =", result)
elif choice=="2":
    result = Sub(num1,num2) 
    print("The Subtract of two numbers is =", result) 
elif choice=="3":
    result = Multi(num1,num2) 
    print("The Multiplication of two numbers is =", result)   
elif choice=="4":
    result = Div(num1, num2)
    print("The Division of two numbers is =", result)   
else:
    print("Invalid Choice")