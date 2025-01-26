'''
Q1. What is the data type of the variable “x” in the following code snippet?
'''
x = 5
'''
    a) Integer

    b) String

    c) Float

    d) Boolean
a.
Q2. Which data type in Python is used to store a sequence of characters?
    a) Integer

    b) Float

    c) String

    d) Boolean
d.
Q3. Which data type is used to store a collection of items, where each item is indexed by a key?
    a) List

    b) Tuple

    c) Set

    d) Dictionary
d.
Q4. What will be the output of the following code snippet? '''

x = 10
y = "20"
print(x + int(y))
'''
    a) 30

    b) 1020

    c) “1020”

    d) Error
 a.   
Q5. Which data type in Python is mutable?
    a) String

    b) Tuple

    c) Set

    d) List
d.
Q6. Which data type is used to store a collection of items, where each item is unique and unordered?
    a) List

    b) Tuple

    c) Set

    d) Dictionary
b.    
Q7. Which data type is used to store a collection of items, where each item is indexed by a numerical index?
    a) list

    b) Tuple

    c) Set

    d) Dictionary
c.
Q8. Which of the following statements about Python strings is true?
    a) Strings in Python are mutable.

    b) Strings can only contain numeric characters.

    c)catenated usin trings can Sbe cong the “+” operator.

    d) Strings can be accessed by numerical indices.
a.
Q9. What will be the output of the following code snippet? '''
x = 10
y = "20"
print(str(x) + y)
'''
    a) 30

    b) “1020”

    c) Error

    d) “10200”
b.    
 Q10. What is the output of the following code snippet?
'''
x =[1,2,3]
x.copy()
x.append(4)
print(y)
'''
    a) [1, 2, 3]

    b) [1, 2, 3, 4]

    c) [1, 2, 3, 4, 4]

    d) [1, 2, 3, 3]
b.
Q11. What will be the output of the following code snippet? '''
x = {"a", "b", "c"}
y = {"b", "c", "d"}
z = x & y
print(z)
'''
    a) {“a”, “b”, “c”, “d”}

    b) {“b”, “c”}

    c) {“a”, “d”}

    d) {“a”, “b”, “c”}
b.
Q12. What is the output of the following code snippet?
'''
x = 10
y = 20
x, y = y, x
print(x, y)
'''
    a) 10 20

    b) 20 10

    c) 20 20

    d) 10 10
b.
    Q13. What will be the output of the following code snippet?
    '''
x = {"name": "John", "age": 30}
print(x["address"])
'''
    a) “John”

    b) 30

    c) None

    d) Error
d.
    Q14. What is a variable in Python?
    a) A container to store data

    b) A function to perform mathematical operations

    c) A loop to iterate through data

    d) A conditional statement for decision-making

    Q15. In Python, variable names are case-sensitive. What does this mean?
    a) Variable names cannot contain uppercase letters.

    b) Variable names must always start with an uppercase letter.

    c) Variable names must always be written in uppercase letters.

    d) Variable names are distinguished by uppercase and lowercase letters.
d.
Q16. Which of the following is a valid variable name in Python?
    a) 3total

    b) my_variable

    c) global

    d) class
b,c,d    
Q17. What does the “global” keyword do in Python?
    a) Declares a variable that is accessible from anywhere in the program.

    b) Declares a variable that is local to a specific function.

    c) Declares a variable that is accessible only within a specific module.

    d) Declares a variable that cannot be modified.
a.
Q18. What is the purpose of the “del” keyword in Python?
    a) To delete a variable from memory.

    b) To define a new variable.

    c) To initialize a variable.

    d) To declare a variable as global.
a.    
Q19. What is the output of the following code snippet? 
'''
x = [1, 2, 3]
y = x[:]
x[0] = 4
print(y)
'''
    a) [1, 2, 3]

    b) [4, 2, 3]

    c) [1, 2, 3, 4]

    d) [4, 2, 3, 4]
b.
Q20. What is the purpose of the “id()” function in Python?
    a) To identify the data type of a variable.

    b) To generate random numbers.

    c) To return the memory address of an object.

    d) To convert a variable to an integer.
a.
Q21. What is the difference between local and global variables in Python?
    a) Local variables are declared outside of any function, while global variables are declared within functions.

    b) Local variables are accessible only within the function they are defined in, while global variables are accessible from any part of the program.

    c) Local variables are stored in the global namespace, while global variables are stored in local namespaces.

    d) Local variables are immutable, while global variables are mutable.
b.
Q22. What is the output of the following code? '''
def test():
    global x
    x = 10
test()
print(x)
'''
    a) 0

    b) 10

    c) Error

    d) None
b.
Q23. What is the output of the following code snippet?

    x = {“name”: “John”, “age”: 30}
    y = x.copy()
    x[“name”] = “Jane”
    print(y[“name”])

    a) “John”

    b) “Jane”

    c) 30

    d) Error
d.
Q24. What will be the output of the following code snippet? '''

x = [1, 2, 3]
y = x.pop(1)
print(y)
'''
    a) 1  

    b) 2  

    c) 3  

    d) Error
b.    
Q25. What will be the output of the following code snippet?
'''
x = [1, 2, 3]
x.insert(1, 4)
print(x)
'''
    a) [1, 4, 2, 3]  

    b) [4, 1, 2, 3]  

    c) [1, 2, 4, 3]  

    d) [1, 4, 2, 4, 3]
d.
Q26. What will be the output of the following code snippet?
'''
x = "Hello"
y = x[1:4]
print(y)
'''
    a) “H”  

    b) “Hell”  

    c) “ell”  

    d) “Hello”
c.
Q27. Which operator is used to calculate the remainder of a division?
    a) %

    b) //

    c) /

    d) **
a.
Q28. What is the result of the expression 4 < 5 and 5 < 6?
    a) True

    b) False

    c) Error

    d) None of the above
a.    
Q29. What will be the output of the following code?
'''
print(3 ** 3)
'''
    a) 9

    b) 27

    c) 81

    d) 6
b.
Q30. What does the expression not(10 == 10) evaluate to?
    a) True

    b) False

    c) Error

    d) None of the above
b.
Q31. Which operator is used to perform floor division?
    a) %

    b) //

    c) /

    d) **
b.
Q32. What will be the output of the following code?
'''
print(9 % 4)
'''
    a) 1

    b) 2

    c) 3

    d) 0
a.
Q33. What will be the output of the following code?
'''
print(7 // 2)
'''
    a) 3.5

    b) 4

    c) 3

    d) 2
a.    
Q34. What does the expression not(3 < 2) evaluate to?
    a) True

    b) False

    c) Error

    d) None of the above
a.
Q35. What will be the output of the following code?
'''
print(2 ** 0)
'''
    a) 1

    b) 0

    c) 2

    d) 3
a.
Q36. Which operator is used to perform logical OR operation?
    a) |

    b) ||

    c) or

    d) OR
c.
Q37. What is the result of the following expression in Python?
    10 > 5 < 2

    a) True
    
    b) False

    c) 7

    d) Error
b.

Q38. What is the result of the following expression in Python?
    3 * "Hello"

    a) “HelloHelloHelloHello”

    b) “Hello 3 times”

    c) “HelloHelloHello”

    d) Error
c.
Q39. What is the result of the following expression in Python?
'''
print(-5 // 2)
'''
    a) -2

    b) -3

    c) 2

    d) 3
a.
Q40. What does the expression bool(0) evaluate to?
    a) True

    b) False

    c) None
    
    d) Error
d.    
'''
