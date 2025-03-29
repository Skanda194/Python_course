from datetime import datetime


if __name__ == "__main__":
    birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
    age = calculate_age(birth_date_input)
    print(f"You are {age} years old.")