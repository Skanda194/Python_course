"""
1. What is the output of `print(type([]))`?
   a) `<class 'list'>`
   b) `<class 'tuple'>`
   c) `<class 'dict'>`
   d) `<class 'array'>`

2. Which of the following is a valid variable name in Python?
   a) 2variable
   b) _variable
   c) variable-name
   d) variable name

3. What is the output of `print(2  3  2)`?
   a) 64
   b) 512
   c) 256
   d) 128

4. Which method is used to add an element to a list at a specific position?
   a) append()
   b) insert()
   c) add()
   d) push()

5. What is the output of `print(3 * 'abc')`?
   a) abcabcabc
   b) abc*3
   c) Error
   d) ['abc','abc','abc']

6. Which of the following is not a keyword in Python?
   a) eval
   b) assert
   c) nonlocal
   d) pass

7. What is the output of `len(['hello', 2, 3.5, [1,2]])`?
   a) 4
   b) 5
   c) 6
   d) 3

8. Which function is used to get the memory address of a variable?
   a) memory()
   b) addr()
   c) id()
   d) ref()

9. What is the output of `print(bool(0), bool(3.14), bool(''))`?
   a) True True False
   b) False True False
   c) False True True
   d) True False True

10. Which operator is used for floor division?
    a) /
    b) //
    c) %
    d) 

11. What is the output of `{1,2,3} - {2,3}`?
    a) {1}
    b) {1,2,3}
    c) {2,3}
    d) Error

12. Which of the following creates a tuple?
    a) [1,2,3]
    b) {1,2,3}
    c) (1,2,3)
    d) <1,2,3>

13. What is the output of `'Hello World'[2:7]`?
    a) 'llo W'
    b) 'llo Wo'
    c) 'ello '
    d) 'ello W'

14. How do you access the last element of a list named 'my_list'?
    a) my_list[last]
    b) my_list[-1]
    c) my_list[end]
    d) my_list[0]

15. What is the output of `len({'a':1, 'b':2, 'c':3})`?
    a) 3
    b) 6
    c) 2
    d) Error

16. Which method returns the number of occurrences of an element in a list?
    a) count()
    b) length()
    c) size()
    d) total()

17. What is the output of `[x2 for x in range(3)]`?
    a) [0,1,4]
    b) [0,1,4,9]
    c) [1,4,9]
    d) [0,1,2]

18. Which of the following is immutable?
    a) List
    b) Dictionary
    c) Set
    d) Tuple

19. What is the output of `'abcdef'.find('cd')`?
    a) 2
    b) 3
    c) 4
    d) 1

20. How do you merge two dictionaries d1 and d2 in Python 3.9+?
    a) d1 + d2
    b) merge(d1,d2)
    c) d1 | d2
    d) d1 & d2

21. What is the output of:
```python
for i in range(1,4):
    if i == 2:
        break
    print(i)
```
a) 1
b) 1 2
c) 1 2 3
d) 1 3

22. Which statement is used to skip the rest of the code inside a loop for the current iteration?
    a) break
    b) continue
    c) pass
    d) skip

23. What is the output of:
```python
x = 5
print(3 < x < 10)
```
a) True
b) False
c) Error
d) None

24. How many times will the following loop execute?
```python
i = 5
while i > 0:
    i -= 1
```
a) 5
b) 4
c) 6
d) Infinite

25. What is the output of:
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```
a) 3 pairs
b) 6 pairs
c) 5 pairs
d) 2 pairs

26. Which conditional statement is used for multiple conditions?
    a) if
    b) if-else
    c) if-elif-else
    d) switch

27. What is the output of:
```python
x = 10
y = 20
print(x if x > y else y)
```
a) 10
b) 20
c) None
d) Error

28. Which loop is guaranteed to execute at least once?
    a) for loop
    b) while loop
    c) do-while loop
    d) None in Python

29. What is the output of:
```python
for i in range(5,0,-2):
    print(i, end=' ')
```
a) 5 3 1
b) 5 4 3 2 1
c) 5 3 1 -1
d) 5 4 3 2

30. Which statement can be used as a placeholder?
    a) continue
    b) break
    c) pass
    d) None

31. What is a lambda function?
    a) A named function
    b) An anonymous function
    c) A recursive function
    d) A built-in function

32. What is the output of:
```python
def func(x, y=5):
    return x * y
print(func(3))
```
a) 15
b) 8
c) 35
d) Error

33. Which keyword is used to return a value from a function?
    a) return
    b) yield
    c) give
    d) output

34. What is a decorator in Python?
    a) A function that modifies another function
    b) A class that inherits from another class
    c) A type of loop
    d) A data structure

35. What is the output of:
```python
def outer():
    x = 1
    def inner():
        return x + 1
    return inner()
print(outer())
```
a) 2
b) 1
c) Error
d) None

36. Which statement about *args is correct?
    a) Accepts variable number of keyword arguments
    b) Accepts variable number of positional arguments
    c) Creates a list
    d) Creates a tuple

37. What is the output of:
```python
def func(a, b, c=10):
    return a + b + c
print(func(1,2,3))
```
a) 6
b) 13
c) 16
d) Error

38. Which function returns the length of an object?
    a) length()
    b) len()
    c) size()
    d) count()

39. What is recursion?
    a) Function calling itself
    b) Function calling another function
    c) Loop inside a function
    d) Multiple return statements

40. What is the output of:
```python
def func():
    pass
print(func())
```
a) None
b) pass
c) Error
d) ""
---
"""


## 10 True/False Questions

# 41. Python is a compiled language. 

# 42. Lists in Python are immutable. 

# 43. The 'is' operator compares the memory addresses of two objects. 

# 44. A function can return multiple values in Python. 

# 45. Python supports multiple inheritance. 

# 46. The 'finally' block always executes regardless of exceptions. 

# 47. Sets in Python maintain insertion order. 

# 48. Global variables can be modified inside a function without any keyword. 

# 49. Python uses indentation to define code blocks. 

# 50. The 'with' statement is used for exception handling. 

