def Donate15dollars():
    global donated_amount , totalDonors
    donated_amount+=15
    totalDonors+=1
    print("Thank you for donating $15.00.")
    print(f'total amount donated {donated_amount} and total donors {totalDonors}')
    