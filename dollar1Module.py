def Donate1dollars():
    global donated_amount , totalDonors
    donated_amount+=1
    totalDonors+=1
    print("Thank you for donating $1.00.")
    print(f'total amount donated {donated_amount} and total donors ={totalDonors}')