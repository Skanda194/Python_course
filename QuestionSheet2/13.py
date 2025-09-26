#What program finds the larger of two numbers (user input)?
y=int(input("Enter a number: "))
x=int(input("Enter a number: "))
if y>x:
    print(y,"is larger")
elif x>y:
    print(x,"is larger")
else:
    print("equal")
