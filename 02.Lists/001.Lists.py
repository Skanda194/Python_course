
# =============================
# Python Lists: Theory & Examples
# =============================
#
# A list in Python is an ordered, mutable (changeable) collection of items. Lists can hold items of any data type, and items can be repeated.
# Lists are one of the most commonly used data structures in Python.
#
# Why use lists?
# - To store multiple values in a single variable
# - To perform operations on sequences of items (iteration, search, sort, etc.)
# - To group related data
#
# List Syntax:
# my_list = [item1, item2, item3, ...]

# --- List Creation ---
numbers = [10, 20, 30, 40, 50]
strings = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty = []

# --- Accessing Elements (Indexing) ---
print("First element:", numbers[0])  # 10
print("Last element:", numbers[-1])  # 50

# --- Slicing ---
print("First three elements:", numbers[:3])  # [10, 20, 30]
print("Elements from index 2 to end:", numbers[2:])  # [30, 40, 50]
print("Every other element:", numbers[::2])  # [10, 30, 50]

# --- Updating Elements ---
numbers[1] = 99
print("After updating index 1:", numbers)  # [10, 99, 30, 40, 50]

# --- Adding Elements ---
numbers.append(60)  # Add to end
print("After append:", numbers)
numbers.insert(2, 25)  # Insert at index 2
print("After insert:", numbers)

# --- Removing Elements ---
numbers.remove(99)  # Remove first occurrence of value
print("After remove:", numbers)
removed = numbers.pop()  # Remove last item
print("After pop:", numbers, "; Popped value:", removed)
del numbers[0]  # Delete by index
print("After del:", numbers)

# --- List Methods ---
sample = [3, 1, 4, 1, 5, 9, 2]
print("Original sample:", sample)
sample.sort()
print("Sorted:", sample)
sample.reverse()
print("Reversed:", sample)
print("Index of 5:", sample.index(5))
print("Count of 1:", sample.count(1))

# --- Membership Test ---
print("Is 4 in sample?", 4 in sample)
print("Is 7 not in sample?", 7 not in sample)

# --- Iterating Over a List ---
for fruit in strings:
	print("Fruit:", fruit)

# --- List Comprehensions (Best Practice) ---
squares = [x**2 for x in range(6)]
print("Squares:", squares)
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# --- Copying Lists ---
copy1 = numbers[:]
copy2 = list(numbers)
copy3 = numbers.copy()
print("Copies:", copy1, copy2, copy3)

# --- Nested Lists ---
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print("Element at row 2, col 3:", matrix[1][2])  # 6

# --- Unpacking Lists ---
a, b, c = strings[:3]
print("Unpacked:", a, b, c)

# --- Useful Built-in Functions ---
print("Length:", len(strings))
print("Max:", max(sample))
print("Min:", min(sample))
print("Sum:", sum(sample))

# --- Clearing and Deleting Lists ---
temp = [1, 2, 3]
temp.clear()
print("Cleared list:", temp)
# del temp  # Uncomment to delete the variable entirely
