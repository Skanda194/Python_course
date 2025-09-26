#How can you check if a year is a leap year (divisible by 4, user input)?
y=int(input("Enter a year: "))
if y%4==0:
    print("leap year")
else:
    print("not leap year")
