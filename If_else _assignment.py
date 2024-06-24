y=input("Enter your employment status:")
z=int(input("Enter your income:"))
a=int(input("Enter your age:"))
b=int(input("Enter your credit score:"))
if y=="Employed":
    if z>=50000:
        if a>=25:
            if b>=650:
                print("You're eligible for a premium card. Want this card?")
    else:
        print("You're only eligible for a basic card.")