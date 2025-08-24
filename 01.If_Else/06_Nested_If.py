x = 15
# Nested If Statements
# You can have if statements inside if statements, this is called nested if statements.

x = 15
if x > 10:
    print('x is above 10')
    if x > 20:
        print('x is also above 20')
    else:
        print('x is not above 20')

# Example 2: Nested if for grading
score = 92
if score >= 60:
    print('Passed')
    if score >= 90:
        print('Excellent!')
    else:
        print('Good job!')
else:
    print('Failed')

# Example 3: Nested if for login
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print('Login successful')
    else:
        print('Incorrect password')
else:
    print('Unknown user')
