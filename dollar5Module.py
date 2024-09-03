def Donate5dollars():
     global donated_amount , totalDonors
     donated_amount+=5 
     totalDonors+=1
     print("Thank you for donating $5.00.")
     print(f'total amount donated {donated_amount} and total donors ={totalDonors}')