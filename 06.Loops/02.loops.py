print("---------- Example - 1 ------------ ")
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Basic for loop
for number in numbers:
    print(number)

print("---------- Example - 2 ------------ ")
# Using range to iterate from 0 to 4
for i in range(5):
    print(i)

print("---------- Example - 3 ------------ ")
# Using range with custom start and step
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

print("---------- Example - 4 ------------ ")
# String iteration
for char in "Python by Arvinder Pal":
    print("-",char,"-")

print("---------- Example - 5 ------------ ")
# Tuple of fruits
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

print("---------- Example - 6 ------------ ")
# Dictionary of fruit prices
fruit_prices = {"apple": 5, "banana": 10, "cherry": 25}
# Iterating over keys
for fruit in fruit_prices:
    print(fruit)

# Iterating over values
for price in fruit_prices.values():
    print(price)

# Iterating over key-value pairs
for fruit, price in fruit_prices.items():
    print(fruit, price)

print("---------- Example - 7 ------------ ")
# List of fruits
fruits = ["apple", "banana", "cherry"]
# Using enumerate to get index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("---------- Example - 8 ------------ ")
# Two lists of names and ages
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
# Using zip to iterate over both lists simultaneously
for name, age in zip(names, ages):
    print(name, age)

print("---------- Example - 9 ------------ ")
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Using else with for loop
for number in numbers:
    print(number)
else:
    print("Something wrong happend")

print("---------- Example - 10 ------------ ")
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Using break to exit the loop
for number in numbers:
    if number == 3:
        break
    print(number)
print("Loop terminated")

print("---------- Example - 11 ------------ ")
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Using continue to skip an iteration
for number in numbers:
    if number % 2 == 0:  # Skip even numbers
        continue
    print(number)


