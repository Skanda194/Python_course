import os
from datetime import datetime

# Constants
CATEGORY_FILE = 'category_donations.txt'
DONOR_FILE = 'donors.txt'
DONATION_GOAL = 1000  # Set a donation goal for the project
BADGE_THRESHOLD = 500  # Threshold for badges

# Donation categories
donation_categories = {
    "1": "Health Care",
    "2": "Education",
    "3": "Environmental",
    "4": "Animal Welfare",
    "5": "Others"
}

# Load existing category data
def load_category_data():
    category_totals = {key: 0 for key in donation_categories.keys()}
    if os.path.exists(CATEGORY_FILE):
        with open(CATEGORY_FILE, 'r') as file:
            for line in file:
                category, amount = line.strip().split(',')
                category_totals[category] += float(amount)
    return category_totals

# Save updated category totals to file
def save_category_totals(category_totals):
    with open(CATEGORY_FILE, 'w') as file:
        for category, total in category_totals.items():
            file.write(f"{category},{total}\n")

# Function to save category donation
def save_category_donation(category, amount, category_totals):
    category_totals[category] += amount
    save_category_totals(category_totals)

# Function to save donor information
def save_donor(name, amount, category):
    with open(DONOR_FILE, 'a') as file:
        file.write(f"{name},{amount},{category},{datetime.now()}\n")

# Function to send a thank you message
def send_thank_you(name, amount):
    print(f"Thank you, {name}, for your donation of ${amount:.2f}!")

# Function to check for milestones
def check_milestone(name, total, personal_milestones):
    if total >= DONATION_GOAL:
        print(f"Congratulations, {name}! You've reached the donation goal of ${DONATION_GOAL}!")
    for milestone in personal_milestones:
        if total >= milestone:
            print(f"Great job, {name}! You've reached your personal milestone of ${milestone}!")

# Function to display donation history
def display_donation_history():
    if os.path.exists(DONOR_FILE):
        print("\nDonation History:")
        with open(DONOR_FILE, 'r') as file:
            for line in file:
                donor_name, amount, category, date = line.strip().split(',')
                print(f"Name: {donor_name}, Amount: ${amount}, Category: {donation_categories.get(category, 'Unknown')}, Date: {date}")
    else:
        print("No donation history found.")

# Function to display personal donation history
def display_personal_history(name):
    if os.path.exists(DONOR_FILE):
        print(f"\n{name}'s Donation History:")
        with open(DONOR_FILE, 'r') as file:
            found = False
            for line in file:
                donor_name, amount, category, date = line.strip().split(',')
                if donor_name == name:
                    found = True
                    print(f"Amount: ${amount}, Category: {donation_categories.get(category, 'Unknown')}, Date: {date}")
            if not found:
                print(f"No donations found for {name}.")
    else:
        print("No donation history found.")

# Function to show leaderboard
def show_leaderboard():
    donors = {}
    if os.path.exists(DONOR_FILE):
        with open(DONOR_FILE, 'r') as file:
            for line in file:
                donor_name, amount, _, _ = line.strip().split(',')
                donors[donor_name] = donors.get(donor_name, 0) + float(amount)
        sorted_donors = sorted(donors.items(), key=lambda x: x[1], reverse=True)[:5]
        print("\nLeaderboard (Top 5 Donors):")
        for name, total in sorted_donors:
            print(f"Name: {name}, Total Donated: ${total:.2f}")
            if total >= BADGE_THRESHOLD:
                print(f"Congratulations {name}, you've earned a badge for donating over ${BADGE_THRESHOLD}!")

# Function to display total donations by category
def show_category_totals(category_totals):
    print("\nTotal Donations by Category:")
    for key, value in category_totals.items():
        print(f"{donation_categories[key]}: ${value:.2f}")

# Updated progress function
def show_progress(total_donations, goal):
    """Show progress towards the donation goal using stars"""
    if goal:
        progress = (total_donations / goal) * 100
        star_count = int((total_donations / goal) * 10)  # 10 stars for 100% progress
        stars = " ★ " * star_count + " ☆ " * (10 - star_count)  # Fill the rest with empty stars
        print(f"\nDonation Progress: {stars} ({progress:.2f}%)")
        
        if total_donations >= goal:
            print("Congratulations! We have reached the donation goal!")
    else:
        print("No donation goal set.\n")
def show_categories():
    print("\nDonation Categories:")
    for key, value in donation_categories.items():
        print(f"{key}. {value}")

# Main menu function
def menu():
    total_donated = 0
    category_totals = load_category_data()
    personal_milestones = []
    name = ""  # Initialize name

    while True:
        print("\n--- Charity Fund Manager ---")
        print("1. Set Personal Milestone")
        print("2. Donate $1")
        print("3. Donate $2")
        print("4. Donate $5")
        print("5. Donate $10")
        print("6. Donate Any Amount")
        print("7. View Donation History")
        print("8. View Personal Donation History")
        print("9. View Leaderboard")
        print("10. View Total Donations by Category")
        print("11. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            milestone = float(input("Enter your personal milestone amount: "))
            personal_milestones.append(milestone)
            print(f"Milestone of ${milestone} set!")
        elif choice=='2':
            amount = 1
            name = input("Enter your name: ")
            show_categories()
            category = input("Select a category (1-5): ")
            total_donated += amount
            save_donor(name, amount, category)
            save_category_donation(category, amount, category_totals)
            send_thank_you(name, amount)
        elif choice=='3':
            amount = 2
            name = input("Enter your name: ")
            show_categories()
            category = input("Select a category (1-5): ")
            total_donated += amount
            save_donor(name, amount, category)
            save_category_donation(category, amount, category_totals)
            send_thank_you(name, amount)
        elif choice=='4':
            amount = 5
            name = input("Enter your name: ")
            show_categories()
            category = input("Select a category (1-5): ")
            total_donated += amount
            save_donor(name, amount, category)
            save_category_donation(category, amount, category_totals)
            send_thank_you(name, amount)
        elif choice=='5':
            amount = 10
            name = input("Enter your name: ")
            show_categories()
            category = input("Select a category (1-5): ")
            total_donated += amount
            save_donor(name, amount, category)
            save_category_donation(category, amount, category_totals)
            send_thank_you(name, amount)
        elif choice == '6':
            name = input("Enter your name: ")
            amount = float(input("Enter the amount to donate: "))
            show_categories()
            category = input("Select a category (1-5): ")
            total_donated += amount
            save_donor(name, amount, category)
            save_category_donation(category, amount, category_totals)
            send_thank_you(name, amount)
        elif choice == '7':
            display_donation_history()
        elif choice == '8':
            name = input("Enter your name: ")
            display_personal_history(name)
        elif choice == '9':
            show_leaderboard()
        elif choice == '10':
            show_category_totals(category_totals)
        elif choice == '11':
            print("Thank you for using Charity Fund Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Show progress and milestones
        show_progress(total_donated, DONATION_GOAL)  # Pass both arguments
        if name:  # Check if name is initialized
            check_milestone(name, total_donated, personal_milestones)

if __name__ == "__main__":
    menu()
