# Functional Components of this code -
# Printing the message for the user : PrintingOptions
def PrintingOptions():
    print(""" Welcome to Calculator Program :Enter
      1.Addition of two numbers
      2. Subtraction
      3. Multiplication
      4. Division
       """)

def Add(num1, num2):
    print("The addition of two numbers is =", num1+num2)

def Sub(num1, num2):
    print("The Subtract of two numbers is =", num1 - num2)

def Multi(num1, num2):
    print("The Multiplication of two numbers is =", num1*num2)

def Div(num1, num2):
    print("The Division of two numbers is =", num1/num2)

num1 = int(input("Enetr First number: "))
num2 = int(input("Enetr the second number :"))
PrintingOptions()
choice = input("Enter your choice :")
    
if choice=="1":
    Add(num1, num2)
elif choice=="2":
    Sub(num1,num2)  
elif choice=="3":
    Multi(num1,num2)    
elif choice=="4":
    Div(num1, num2)   
else:
    print("Invalid Choice")

# It is not scalable - For different input we have to run the code again and again 

