import dollar1Module,dollar5Module,dollar10Module,dollar15Module,dollarAnyModule
donated_amount=200000
totalDonors=201
def DisplayMenu():
    print("Press 1 to donate 1 dollar: ")
    print("Press 2 to donate 5 dollars: ")
    print("Press 3 to donate 10 dollars: ")
    print("Press 4 to donate 15 dollars: ")
    print("Press 5 to donate any other amount: ")
print("Welcome to the Charity Fund Calculator!")
DisplayMenu()
choice=input("Choose one option from 1 to 5: ")
if choice=="1":
    dollar1Module.Donate1dollars()
elif choice=="2":
    dollar5Module.Donate5dollars()
elif choice=="3":
    dollar10Module.Donate10dollars()
elif choice=="4":
    dollar15Module.Donate15dollars()
elif choice=="5":
    dollarAnyModule.DonateAnyDollar()
else:
    print("Invalid option")

    