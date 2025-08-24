# Comparison Operators in Conditionals
# Comparison operators are used to compare values.

x = 7
y = 10
if x == y:
    print('x is equal to y')
if x != y:
    print('x is not equal to y')
if x < y:
    print('x is less than y')
if x > y:
    print('x is greater than y')
if x <= y:
    print('x is less than or equal to y')
if x >= y:
    print('x is greater than or equal to y')

# Example 2: Compare strings
str1 = "apple"
str2 = "banana"
if str1 < str2:
    print('apple comes before banana')

# Example 3: Compare list lengths
list1 = [1, 2, 3]
list2 = [4, 5]
if len(list1) > len(list2):
    print('list1 is longer')
