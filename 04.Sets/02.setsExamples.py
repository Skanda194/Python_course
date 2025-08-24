# =============================
# Unique Python Set Coding Examples (No Repeats)
# =============================

# 1. Manual union of two sets (using loops)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_manual = set1.copy()
for x in set2:
	if x not in union_manual:
		union_manual.add(x)
print("Manual union:", union_manual)

# 2. Manual intersection of two sets (using loops)
intersection_manual = set()
for x in set1:
	if x in set2:
		intersection_manual.add(x)
print("Manual intersection:", intersection_manual)

# 3. Manual difference (set1 - set2)
difference_manual = set()
for x in set1:
	if x not in set2:
		difference_manual.add(x)
print("Manual difference (set1 - set2):", difference_manual)

# 4. Manual symmetric difference
sym_diff_manual = set()
for x in set1:
	if x not in set2:
		sym_diff_manual.add(x)
for x in set2:
	if x not in set1:
		sym_diff_manual.add(x)
print("Manual symmetric difference:", sym_diff_manual)

# 5. Find common elements between two lists using sets
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
common = set()
for x in list1:
	if x in list2:
		common.add(x)
print("Common elements in lists:", common)

# 6. Remove duplicates from a list using a set (with loop)
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = []
seen = set()
for n in nums:
	if n not in seen:
		unique_nums.append(n)
		seen.add(n)
print("List with duplicates removed:", unique_nums)

# 7. Check if two sets are disjoint (no common elements) using a loop
setA = {1, 2, 3}
setB = {4, 5, 6}
disjoint = True
for x in setA:
	if x in setB:
		disjoint = False
		break
print("Are setA and setB disjoint?", disjoint)

# 8. Manual subset and superset checks
subset = True
for x in setA:
	if x not in setB:
		subset = False
		break
print("Is setA a subset of setB?", subset)

superset = True
for x in setB:
	if x not in setA:
		superset = False
		break
print("Is setA a superset of setB?", superset)

# 9. Count unique elements in a list
data = [1, 2, 2, 3, 4, 4, 5, 1]
unique_count = 0
seen = set()
for n in data:
	if n not in seen:
		unique_count += 1
		seen.add(n)
print("Number of unique elements:", unique_count)

# 10. Manual set equality check
setX = {1, 2, 3}
setY = {3, 2, 1}
equal = True
if len(setX) != len(setY):
	equal = False
else:
	for x in setX:
		if x not in setY:
			equal = False
			break
print("Are setX and setY equal?", equal)

# 11. Find all pairs in a set that sum to a target value
nums_set = {1, 2, 3, 4, 5, 6}
target = 7
pairs = set()
for x in nums_set:
	for y in nums_set:
		if x < y and x + y == target:
			pairs.add((x, y))
print(f"Pairs in set that sum to {target}:", pairs)
