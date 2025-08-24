# Elif Statement
# The elif keyword is used to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions is true.

x = 5
if x > 5:
    print('x is greater than 5')
elif x == 5:
    print('x is equal to 5')
else:
    print('x is less than 5')

# Example 2: Categorize age
age = 12
if age < 13:
    print('Child')
elif age < 20:
    print('Teenager')
else:
    print('Adult')

# Example 3: Weather conditions
weather = "rainy"
if weather == "sunny":
    print('Wear sunglasses')
elif weather == "rainy":
    print('Take an umbrella')
else:
    print('Check the weather forecast')
