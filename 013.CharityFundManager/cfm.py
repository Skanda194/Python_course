import os
from datetime import datetime 

CATEGORY_FILE = 'category_donations.txt'
DONOR_FILE = 'donors.txt'
DONATION_GOAL = 1000
BADGE_THRESHOLD = 500

donation_categories={
    "1":"Health Care",
    "2":"Education",
    "3":"Child Protection",
    "4":"Women Empowerment",
    "5":"Animal",
    "6":"Others"
}
def display_category_history():
    if os.path.exists(DONOR_FILE):
        print("\n Donation History: ")
        with open(DONOR_FILE,'r') as file:
            for line in file:
                donors_name , amount , category , date = line.strip().split(',')
                print(f"Name: {donors_name}, Amount: ${amount}, Category: {donation_categories.get(category,'Unknown')}, Date : {date} ")
    else:
        print("No danation history found.")


def send_thanks_message(name , amount):
    print(f"Thanks you {name} for donating ${amount}.")

#Displaying the categories 
def show_categories():
    print("\n Donation Categories : ")
    for key , value in donation_categories.items():
        print(f"{key}:{value}")
def main():
    total_donated = 0
    personal_milestones = []
    while True:
        print("\n ---- Charity Fund Manager ----")
        print("1. Set Personal Milestone")
        print("2. Donate $1")
        print("3. Donate $2")
        print("4. Donate $5")
        print("5. Donate $10")
        print("6. Donate any amount")
        print("7. View Donation history")
        print("8. View Personal DOnation history")
        print("9. View Leaderboard")
        print("10. View total donations by Category")
        print("11. Exit")

        choice = input("Select any option: ")
        if choice == '1':
            milestone = float(input("Enter your personal milestone amount"))
            personal_milestones.append(milestone)
            print(f"Your Personal Miestone is set for ${milestone}.")
        if choice =='2':
            amount =1 
            name = input("Enter your name :")
            show_categories()
            category = input("Select one category:")
            total_donated +=amount
            # save_donor(name,amount,category)
            #save_category_donation(category,amount , total)
            send_thanks_message(name, amount)
        if choice =='3':
            amount =2 
            name = input("Enter your name :")
            show_categories()
            category = input("Select one category:")
            total_donated +=amount
            # save_donor(name,amount,category)
            #save_category_donation(category,amount , total)
            send_thanks_message(name, amount)
        if choice =='4':
            amount =5 
            name = input("Enter your name :")
            show_categories()
            category = input("Select one category:")
            total_donated +=amount
            # save_donor(name,amount,category)
            #save_category_donation(category,amount , total)
            send_thanks_message(name, amount)
        if choice =='5':
            amount =10 
            name = input("Enter your name :")
            show_categories()
            category = input("Select one category:")
            total_donated +=amount
            # save_donor(name,amount,category)
            #save_category_donation(category,amount , total)
            send_thanks_message(name, amount)
        if choice=='6':
            name = input("Enter your name :")
            amount = float(input("Enter the amount you want to donate: "))
            show_categories()
            category = input("Select one category:")
            total_donated +=amount
            # save_donor(name,amount,category)
            #save_category_donation(category,amount , total)
            send_thanks_message(name, amount)
        if choice =='7':
            display_category_history()
if __name__ =="__main__":
    main()