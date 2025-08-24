# Pass Statement in Conditionals
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

x = 10
if x > 5:
    pass  # nothing happens, but the code is syntactically correct

print('Code after pass statement')

# Example 2: Using pass in a loop
for i in range(5):
    if i == 2:
        pass  # placeholder for future code
    else:
        print(i)

# Example 3: Using pass in function definition
def my_function():
    pass  # function to be implemented later
