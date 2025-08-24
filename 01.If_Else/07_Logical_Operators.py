x = 5
# Logical Operators in Conditionals
# Logical operators (and, or, not) are used to combine conditional statements.


y = 10
if x > 0 and y > 0:
    print('Both x and y are positive')

if x > 0 or y < 0:
    print('At least one is positive')

if not(x < 0):
    print('x is not negative')

# Example 2: Check if a number is in a range
num = 8
if num > 0 and num < 10:
    print('num is between 1 and 9')

# Example 3: Using or for multiple options
color = "red"
if color == "red" or color == "blue":
    print('Color is red or blue')

# Example 4: Using not
logged_in = False
if not logged_in:
    print('Please log in')
