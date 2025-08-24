# Advanced Conditionals and Best Practices

# Example: Multiple conditions and input
num = int(input('Enter a number: '))
if num > 0:
    print('Positive number')
elif num == 0:
    print('Zero')
else:
    print('Negative number')

# Example: Chained comparisons
x = 15
if 10 < x < 20:
    print('x is between 10 and 20')

# Example: Using conditionals in list comprehensions
nums = [1, 2, 3, 4, 5]
even_nums = [n for n in nums if n % 2 == 0]
print('Even numbers:', even_nums)

# Example 4: Using any() and all() with conditionals
values = [True, True, False]
if any(values):
    print('At least one value is True')
if all(values):
    print('All values are True')
else:
    print('Not all values are True')

# Example 5: Conditional expressions in function arguments
def greet(name=None):
    print('Hello, ' + (name if name else 'Guest'))

greet('Sam')
greet()
