# Short Hand If and If...Else (Ternary Operator)

# Short hand if
x = 10
y = 5
if x > y: print('x is greater than y')

# Short hand if...else (ternary)
print('x is greater') if x > y else print('y is greater or equal')

# Example 2: Assign value using ternary
max_value = x if x > y else y
print('Max value:', max_value)

# Example 3: Multiple statements in one line
a = 3
b = 7
print('a is less than b') if a < b else print('a is not less than b')
