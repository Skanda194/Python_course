#What program assigns a grade (A, B, C, etc.) based on a score (user input)?
y=int(input("enter a percent: "))
if y>=90:
    print("A")
elif y>=80 and y<=89:
    print("B")
elif y>=70 and y<=79:
    print("C")
else:
    print("C or lower")
