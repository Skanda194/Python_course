def Donate10dollars():
     global donated_amount , totalDonors
     donated_amount+=10
     totalDonors+=1
     print("Thank you for donating 10.00.")
     print(f'total amount donated {donated_amount} and total donors ={totalDonors}')