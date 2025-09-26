#What program determines if a person can vote (age >= 18, user input)?
y=int(input("Enter your age: "))
if y>=18:
    print("You can vote")
else:
    print("Minor: Cannot vote")