def DonateAnyDollar():
    global donated_amount , totalDonors
    y=int(input("How much do you want to enter: "))
    donated_amount=donated_amount+y 
    totalDonors+=1
    print("Thank you for donating this amount.")
    print(f'total amount donated{donated_amount} and total donors{totalDonors}')