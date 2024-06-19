x=input("Enter W for withdrawal, D for deposit, and B for Balance check")
Balance=10000000
MinimumBalance=1000
if x=="W":
    if MinimumBalance>=Balance:
        print("Insufficient funds, you need more money!")
    if Balance>1000:
        y=int(input("Enter how much dollars you want to withdraw"))
        if y>=1000:
            print("you can't print this much money")
        else:
            print("Your balance is",int(Balance)-y,"dollars")
    else:
        print("Balance is less than a thousand dollars")

elif x=="B":
    print(Balance)
elif x=="D":
    z=int(input("Enter how much dollars you want to deposit"))
    print("Your balance is",int(Balance)+z,"After depositing",z)

