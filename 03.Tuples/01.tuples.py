
# =============================
# Python Tuples: Theory & Examples
# =============================
#
# A tuple in Python is an ordered, immutable (unchangeable) collection of items. Tuples can hold items of any data type and allow duplicates.
#
# Why use tuples?
# - To store multiple values in a single variable
# - To ensure data cannot be changed (immutability)
# - Tuples can be used as dictionary keys and set elements (if all items are hashable)
#
# Tuple Syntax:
# my_tuple = (item1, item2, ...)

# --- Tuple Creation ---
my_tuple = ("Apple", "Banana", "Coconut")
print("Tuple:", my_tuple)

# Single-item tuple (note the comma)
single_tuple = ("Orange",)
print("Single-item tuple:", single_tuple)

# Tuple with mixed data types
mixed_tuple = ("Hello", 23, 100.5, True)
print("Mixed tuple:", mixed_tuple)

# --- Indexing and Slicing ---
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice (first two):", my_tuple[:2])

# --- Immutability ---
# my_tuple[1] = "Kiwi"  # This will raise a TypeError

# --- Length of a tuple ---
print("Length:", len(my_tuple))

# --- Iterating over a tuple ---
for item in my_tuple:
	print("Item:", item)

# --- Tuple Packing and Unpacking ---
person = ("Alice", 30, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("First:", first, "Middle:", middle, "Last:", last)

# --- Concatenation and Repetition ---
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined = tuple1 + tuple2
print("Concatenated tuple:", combined)
repeated = tuple1 * 3
print("Repeated tuple:", repeated)

# --- Tuple Methods ---
sample = (1, 2, 2, 3, 4, 2)
print("Count of 2:", sample.count(2))
print("Index of 3:", sample.index(3))

# --- Membership Test ---
print("Is 'Banana' in my_tuple?", "Banana" in my_tuple)
print("Is 'Kiwi' not in my_tuple?", "Kiwi" not in my_tuple)

# --- Nested Tuples ---
matrix = (
	(1, 2, 3),
	(4, 5, 6),
	(7, 8, 9)
)
print("Element at row 2, col 3:", matrix[1][2])

# --- Converting between tuples and lists ---
temp_list = list(my_tuple)
temp_list[1] = "Kiwi"
new_tuple = tuple(temp_list)
print("Modified tuple:", new_tuple)

# --- Deleting a tuple ---
temp = (10, 20, 30)
# del temp  # Uncomment to delete the tuple variable

# --- Useful Built-in Functions ---
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

# --- Tuple as Dictionary Key ---
locations = {}
point = (10, 20)
locations[point] = "Home"
print("Dictionary with tuple key:", locations)








