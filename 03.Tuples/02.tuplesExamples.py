# =============================
# Unique Python Tuple Coding Examples
# =============================

# 1. Sorting a tuple (by converting to list and back)
unsorted_tuple = (5, 2, 8, 1, 3)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("Sorted tuple:", sorted_tuple)

# 2. Enumerating a tuple
colors = ("red", "green", "blue")
for idx, color in enumerate(colors):
	print(f"Index {idx}: {color}")

# 3. Comparing tuples
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print("t1 < t2:", t1 < t2)
print("t1 == t2:", t1 == t2)

# 4. Tuples in sets (hashable)
set_of_tuples = set()
set_of_tuples.add((1, 2))
set_of_tuples.add((3, 4))
print("Set of tuples:", set_of_tuples)

# 5. Function returning multiple values as a tuple
def min_max(nums):
	min_val = nums[0]
	max_val = nums[0]
	for n in nums:
		if n < min_val:
			min_val = n
		if n > max_val:
			max_val = n
	return min_val, max_val

result = min_max([7, 2, 9, 4])
print("Min and Max:", result)

# 6. Generator expression to create a tuple (tuple comprehension-like)
gen = (x**2 for x in range(5))
tuple_of_squares = tuple(gen)
print("Tuple of squares:", tuple_of_squares)

# 7. Immutability demonstration with try/except
immutable = (10, 20, 30)
try:
	immutable[0] = 99
except TypeError as e:
	print("Immutability error:", e)

# 8. Length of nested tuples
nested = ((1, 2), (3, 4, 5), (6,))
print("Length of outer tuple:", len(nested))
for i, inner in enumerate(nested):
	print(f"Length of inner tuple {i}:", len(inner))

# 9. Swapping variables using tuple unpacking
a, b = 5, 10
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)
# =============================
# Python Tuple Coding Examples
# =============================

# 1. Create a tuple
fruits = ("apple", "banana", "cherry")
print("Tuple:", fruits)

# 2. Access elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Slicing a tuple
print("First two fruits:", fruits[:2])

# 4. Tuple with mixed data types
person = ("Alice", 28, 5.7, True)
print("Person tuple:", person)

# 5. Iterating over a tuple
for fruit in fruits:
	print("Fruit:", fruit)

# 6. Tuple unpacking
name, age, height, is_student = person
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# 7. Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("First:", first, "Middle:", middle, "Last:", last)

# 8. Concatenation and repetition
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print("Concatenated tuple:", combined)
repeated = tuple1 * 3
print("Repeated tuple:", repeated)

# 9. Tuple methods: count and index
sample = (1, 2, 2, 3, 4, 2)
print("Count of 2:", sample.count(2))
print("Index of 3:", sample.index(3))

# 10. Membership test
print("Is 'banana' in fruits?", 'banana' in fruits)
print("Is 'kiwi' not in fruits?", 'kiwi' not in fruits)

# 11. Nested tuples
matrix = (
	(1, 2, 3),
	(4, 5, 6),
	(7, 8, 9)
)
print("Element at row 2, col 3:", matrix[1][2])

# 12. Convert tuple to list and back
temp_list = list(fruits)
temp_list[1] = "kiwi"
new_tuple = tuple(temp_list)
print("Modified tuple:", new_tuple)

# 13. Tuple as dictionary key
locations = {}
point = (10, 20)
locations[point] = "Home"
print("Dictionary with tuple key:", locations)

# 14. Find max, min, and sum (with numbers)
nums = (5, 2, 9, 1)
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

# 15. Immutability demonstration
# The following line would raise an error:
# fruits[0] = "orange"  # TypeError: 'tuple' object does not support item assignment
