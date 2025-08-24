# =============================
# Python List Coding Examples
# =============================

# 1. Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)


# 2. Sum of all numbers (using loop)
total_sum = 0
for x in numbers:
	total_sum += x
print("Sum of all numbers:", total_sum)

# 3. Sum of even numbers (using loop)
even_sum = 0
for x in numbers:
	if x % 2 == 0:
		even_sum += x
print("Sum of even numbers:", even_sum)

# 4. Sum of odd numbers (using loop)
odd_sum = 0
for x in numbers:
	if x % 2 != 0:
		odd_sum += x
print("Sum of odd numbers:", odd_sum)

# 5. Product of all numbers (using loop)
product = 1
for x in numbers:
	product *= x
print("Product of all numbers:", product)

# 6. Maximum and minimum number (using loop)
max_num = numbers[0]
min_num = numbers[0]
for x in numbers:
	if x > max_num:
		max_num = x
	if x < min_num:
		min_num = x
print("Maximum number:", max_num)
print("Minimum number:", min_num)

# 7. List of squares
squares = [x**2 for x in numbers]
print("Squares:", squares)

# 8. List of cubes
cubes = [x**3 for x in numbers]
print("Cubes:", cubes)

# 9. Filter even and odd numbers
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
print("Even numbers:", evens)
print("Odd numbers:", odds)

# 10. Find index of a value (e.g., 7)
if 7 in numbers:
	idx = numbers.index(7)
	print("Index of 7:", idx)
else:
	print("7 not found in list")

# 11. Reverse the list
reversed_numbers = numbers[::-1]
print("Reversed list:", reversed_numbers)

# 12. Remove duplicates from a list
dupe_list = [1, 2, 2, 3, 4, 4, 5]
no_dupes = list(set(dupe_list))
print("List without duplicates:", no_dupes)

# 13. Sort a list in descending order
desc_sorted = sorted(numbers, reverse=True)
print("Descending order:", desc_sorted)

# 14. Find all numbers greater than 5
greater_than_5 = [x for x in numbers if x > 5]
print("Numbers > 5:", greater_than_5)


# 15. Count occurrences of a value (e.g., 2) using loop
count_2 = 0
for x in numbers:
	if x == 2:
		count_2 += 1
print("Count of 2:", count_2)

# ...existing code...
# =============================
# Python List Coding Examples
# =============================

# 1. Create a list of numbers
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

# 2. Add elements to a list
numbers.append(6)
numbers.insert(0, 0)
print("After append and insert:", numbers)

# 3. Remove elements from a list
numbers.remove(3)  # Remove value 3
last = numbers.pop()  # Remove last element
print("After remove and pop:", numbers, "; Popped:", last)

# 4. List slicing
print("First three elements:", numbers[:3])
print("Every other element:", numbers[::2])

# 5. Iterating over a list
for n in numbers:
	print("Element:", n)

# 6. List comprehension: squares of numbers
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# 7. Filtering with list comprehension: even numbers
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)

# 8. Find the sum, max, and min
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# 9. Nested lists (2D list)
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print("Element at row 2, col 3:", matrix[1][2])

# 10. List methods: count, index, reverse, sort
fruits = ["apple", "banana", "apple", "cherry"]
print("Count of 'apple':", fruits.count("apple"))
print("Index of 'banana':", fruits.index("banana"))
fruits.reverse()
print("Reversed:", fruits)
fruits.sort()
print("Sorted:", fruits)

# 11. Copying a list
copy1 = numbers[:]
copy2 = list(numbers)
print("Copies:", copy1, copy2)

# 12. Remove all elements
copy1.clear()
print("Cleared list:", copy1)

# 13. Unpacking a list
a, b, c, d, e = numbers[:5]
print("Unpacked:", a, b, c, d, e)

# 14. Using enumerate to get index and value
for idx, val in enumerate(numbers):
	print(f"Index {idx}: Value {val}")

# 15. Zipping two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
	print(f"{name} scored {score}")
