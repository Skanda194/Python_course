
# =============================
# Python Sets: Theory & Examples
# =============================
#
# A set in Python is an unordered, mutable collection of unique elements. Sets do not allow duplicates and are useful for membership tests, removing duplicates, and set operations (union, intersection, etc).
#
# Why use sets?
# - To store unique items
# - To perform mathematical set operations
# - Fast membership testing
#
# Set Syntax:
# my_set = {item1, item2, ...}

# --- Set Creation ---
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Duplicates are removed automatically
dupe_set = {1, 2, 2, 3, 4, 4, 5}
print("No duplicates:", dupe_set)

# Sets can contain mixed data types
mixed_set = {"Hello", 100, 245.67, True, 'A'}
print("Mixed set:", mixed_set)

# True == 1, False == 0 in sets
bool_set = {True, 1, 0, False}
print("Boolean set:", bool_set)

# --- Adding and Removing Elements ---
my_set.add(6)
my_set.add(3)  # No effect, already present
print("After add:", my_set)
my_set.remove(2)  # Raises KeyError if not present
print("After remove:", my_set)
my_set.discard(10)  # No error if not present
print("After discard:", my_set)

# --- Pop and Clear ---
popped = my_set.pop()
print("Popped element:", popped)
print("After pop:", my_set)
my_set.clear()
print("After clear:", my_set)

# --- Set Operations ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)

# --- Membership Test ---
print("Is 3 in a?", 3 in a)
print("Is 7 not in a?", 7 not in a)

# --- Iterating Over a Set ---
for item in b:
	print("Set item:", item)

# --- Set Comprehension ---
squares = {x**2 for x in range(6)}
print("Set of squares:", squares)

# --- Convert List to Set (remove duplicates) ---
my_list = [10, 20, 20, 30, 40, 10]
unique = set(my_list)
print("Unique from list:", unique)

# --- Set Length ---
print("Length of set a:", len(a))

# --- Set Copy ---
copy_a = a.copy()
print("Copy of a:", copy_a)



