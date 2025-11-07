"""
Python None & NoneType
"""

# ========================================
# 1. What is NoneType?
# ========================================

print("1. NONE & NONETYPE BASICS")
print("=" * 50)

none_value = None
print(f"Value          : {none_value}")
print(f"Type           : {type(none_value)}")   # <class 'NoneType'>
print(f"Is singleton   : {None is None}")        # True
print()

# ========================================
# 2. None vs Other Falsy Values
# ========================================

print("2. NONE vs OTHER FALSY VALUES")
print("=" * 50)

values = [
    ("None", None),
    ("False", False),
    ("0", 0),
    ("0.0", 0.0),
    ("''", ""),
    ("[]", []),
    ("{}", {}),
    ("set()", set()),
]

for name, val in values:
    print(f"{name:8} == None → {val == None}")
    print(f"{name:8} is None → {val is None}")
    print(f"{name:8} bool()  → {bool(val)}")
print()

# ========================================
# 3. Proper Way to Check for None
# ========================================

print("3. CORRECT CHECKS")
print("=" * 50)

def check(value):
    # Recommended
    if value is None:
        return "value is None (identity check)"
    if value == None:  # Works but not idiomatic
        return "value == None (equality check)"
    return f"value is {value!r}"

print(check(None))
print(check(""))
print(check(0))
print(check(False))
print()

# ========================================
# 4. Functions and None
# ========================================

print("4. FUNCTIONS RETURNING NONE")
print("=" * 50)

def no_return():
    print("This function returns nothing → None")

def find_user(user_id):
    if user_id == 42:
        return {"id": 42, "name": "Alice"}
    return None  # Explicitly no user

result = no_return()
print(f"no_return() returns → {result} ({type(result)})")

user = find_user(99)
if user is None:
    print("User not found")
else:
    print(f"Found: {user['name']}")
print()

# ========================================
# 5. Default Parameters
# ========================================

print("5. NONE AS SAFE DEFAULT")
print("=" * 50)

def append_item(item, container=None):
    if container is None:
        container = []    # Create new list only when needed
    container.append(item)
    return container

list1 = append_item(10)
list2 = append_item(20)
list1 = append_item(30, list1)

print(f"New list each call : {append_item(5)}")   # [5]
print(f"Same list reused  : {list1}")             # [10, 30]
print()

# ========================================
# 6. Common Errors with None
# ========================================

print("6. COMMON ERRORS")
print("=" * 50)

def risky_function(flag):
    if flag:
        return "Success"
    # Implicit return None if no return statement

data = risky_function(False)
try:
    print(data.upper())
except AttributeError as e:
    print(f"Error: {e}")  # 'NoneType' object has no attribute 'upper'

# Safe pattern
data = risky_function(False) or "default"
print(f"Safe fallback → {data}")
print()

# ========================================
# 7. None in Data Structures
# ========================================

print("7. NONE IN JSON / DICTS / APIs")
print("=" * 50)

import json

payload = {
    "name": "Rahul",
    "age": 28,
    "email": None,
    "tags": None
}

json_str = json.dumps(payload, indent=2)
print("JSON with None → becomes null:")
print(json_str)
print()

# ========================================
# 8. Quick Reference Table
# ========================================

print("8. SUMMARY TABLE")
print("=" * 50)
print(f"{'Expression':<15} {'Result':<10} {'Recommended'}")
print("-" * 50)
checks = [
    ("value is None",       "Detect None",      "YES"),
    ("value == None",       "Works",            "Avoid"),
    ("if not value:",       "Catches falsy",    "Only if intended"),
    ("value is not None",   "Has value",        "YES"),
]

for expr, desc, rec in checks:
    print(f"{expr:<15} {desc:<10} {rec}")
print()

print("All done! You now master NoneType in Python.")
print("Use 'None' to represent absence of value – never 0 or '' for that purpose.")
"""

Ready for your next question! 🐍
