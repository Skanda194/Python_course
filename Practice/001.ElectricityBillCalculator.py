
'''
Write a program in python to calculate and print the electricity bill of a given customer. 
The customer ID, name, and unit consumed by the user should be captured from the keyboard to
display the total amount to be paid to the customer.

The charge are as follow :
Unit	                                Charge/unit
upto 199	                               @1.20
200 and above but less than 400	           @1.50
400 and above but less than 600	           @1.80
600 and above	                           @2.00

If bill exceeds Rs. 400 then a surcharge of 15% will be charged and the minimum bill should 
be of Rs. 100/-

Test Data :
1001
James
800
Expected Output :
Customer IDNO :1001
Customer Name :James
unit Consumed :800
Amount Charges @Rs. 2.00 per unit : 1600.00
Surchage Amount : 240.00
Net Amount Paid By the Customer : 1840.00
'''

def consume(name,num):
    con=int(input("Enter how much money you've consumed: "))
    print("Customer name",name)
    print("Customer ID",num)
    if con<200:
        print("Amount Charges @$. 1.20 per unit:",float(con*1.20))
        print("Net Amount paid by customer:",con+con*1.20)
    elif con>=200 and con<=400:
        print("Amount Charges @$. 1.50 per unit:",float(con*1.5))
        print("Net Amount paid by customer:",con+con*1.5)
    elif con>400 and con<600:
        print("Amount Charges @$. 1.80 per unit:",float(con*1.8))
        print("Surcharge amount",con*0.15)
        print("Net Amount paid by customer:",con+con*1.8+con*0.15)
    else:
        print("Amount Charges @$. 2.00 per unit:",float(con*2))
        print("Surcharge amount",con*0.15)
        print("Net Amount paid by customer:",con+con*0.15+con*2)



def id():
    name=input("Enter your name: ")
    num=int(input("Enter your ID number: "))
    consume(name,num)
id()



'''
def calculate_bill(units):
    if units <= 199:
        amount = units * 1.20
    elif units >= 200 and units < 400:
        amount = units * 1.50
    elif units >= 400 and units < 600:
        amount = units * 1.80
    else:
        amount = units * 2.00
    
    surcharge = 0
    if amount > 400:
        surcharge = amount * 0.15
    
    total_amount = amount + surcharge
    
    if total_amount < 100:
        total_amount = 100
    
    return amount, surcharge, total_amount

# Input from the user
customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units_consumed = int(input("Enter Units Consumed: "))

# Calculate bill
amount, surcharge, total_amount = calculate_bill(units_consumed)

# Display the bill details
print("\nElectricity Bill")
print(f"Customer IDNO : {customer_id}")
print(f"Customer Name : {customer_name}")
print(f"Unit Consumed : {units_consumed}")
print(f"Amount Charges @Rs. {amount/units_consumed:.2f} per unit : {amount:.2f}")
print(f"Surcharge Amount : {surcharge:.2f}")
print(f"Net Amount Paid By the Customer : {total_amount:.2f}")

'''