y=int(input("Enter coordinate digit x: "))
x=int(input("Enter coordinate digit y: "))
if x==0 and y==0:
    print("point is on origin")
elif x==0:
    print("Point is on y-axis")
elif y==0:
    print("Point is on x-axis")
elif x>0 and y>0:
    print("It is on neither x or y coordinate")