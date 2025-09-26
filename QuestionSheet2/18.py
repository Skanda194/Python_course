#How can you check if a number is divisible by both 2 and 3 (user input)?
y=int(input("Enter a number: "))
if y%2==0 and y%3==0:
    print("divisible")
else:
    print("not divisible")