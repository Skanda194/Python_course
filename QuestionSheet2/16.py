#How do you check if a number is between 1 and 100 (user input)?
y=int(input("Enter a number: "))
if y<=100 and y>=1:
    print("in range between 1 and 100")
else:
    print("Not in range")