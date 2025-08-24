# Python Conditionals - Theory and Overview
'''
Conditionals are used to perform different actions based on different conditions.
Python supports the following conditional statements:
- if statement
- if...else statement
- if...elif...else ladder
- Nested if statements
- Short hand if and if...else (ternary operator)
- Logical operators (and, or, not)
- Comparison operators (==, !=, >, <, >=, <=)
- pass statement (to do nothing)
'''

# Example 1: Simple if statement
x = 7
if x > 5:
	print('x is greater than 5')

# Example 2: if...else statement
age = 18
if age >= 18:
	print('You are an adult')
else:
	print('You are not an adult')

# Example 3: if...elif...else ladder
score = 85
if score >= 90:
	print('Grade: A')
elif score >= 80:
	print('Grade: B')
elif score >= 70:
	print('Grade: C')
else:
	print('Grade: D or below')

# Example 4: Nested if
num = -3
if num >= 0:
	if num == 0:
		print('Zero')
	else:
		print('Positive number')
else:
	print('Negative number')

# Example 5: Using logical operators
temperature = 25
humidity = 60
if temperature > 20 and humidity < 70:
	print('Nice weather!')
