from datetime import datetime

def calculate_age(day, month, year):
    try:
        # Validate inputs
        dob = datetime(year, month, day)
        today = datetime.today()
        
        # Check if DOB is in the future
        if dob > today:
            return "Error: Date of birth cannot be in the future."
        
        # Calculate the difference
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day
        
        # Adjust if days are negative
        if days < 0:
            months -= 1
            previous_month = today.month - 1 if today.month > 1 else 12
            previous_year = today.year if today.month > 1 else today.year - 1
            days_in_prev_month = (datetime(previous_year, previous_month + 1, 1) - datetime(previous_year, previous_month, 1)).days
            days += days_in_prev_month
        
        # Adjust if months are negative
        if months < 0:
            years -= 1
            months += 12
        
        return f"You are {years} years, {months} months, and {days} days old."
    except ValueError:
        return "Error: Invalid date. Please enter a valid day, month, and year."

# User input
try:
    day = int(input("Enter your birth day (DD): "))
    month = int(input("Enter your birth month (MM): "))
    year = int(input("Enter your birth year (YYYY): "))
    print(calculate_age(day, month, year))
except ValueError:
    print("Error: Please enter valid numerical values for day, month, and year.")
