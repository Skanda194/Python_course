# Nested loops - Loop inside a loop

# for i in range(5):
#     for j in range(5):
#         print('*', end='')

# for i in range(3):
#     print('*')
# for i in range(3):
#     print('*', end=' ')
# *
# *
# *

# * * * * * * 

"""
row 1    *
row 2    *   *
row 3    *   *   *
row 4    *   *   *   *
row 5    *   *   *   *   *
"""
# print('''
# *                 
# *   *
# *   *   *
# *   *   *   *
# *   *   *   *   *
# *   *   *   *   *   *
# ''')

# number of rows- 0 , 1 ,2 3,4 
# i=0 , j = 0, 1,2,3,4 => i=1 , j= 0,1,2,3,4


# rows = 7 
print()
"""
* 
* *
* * *
* * * *       
* * * * *     
* * * * * *   
"""
for i in range(1,7):  
    for j in range(i):  
        print('* ', end='')
    print()

print("------------------------")
"""
* * * * * * * 
* * * * * *   
* * * * *     
* * * *       
* * *
* *
* 
"""
for i in range(7,0,-1):  
    for j in range(i):  
        print('* ', end='')
    print()
print("----------------------------")
for i in range(1,7):  
    for j in range(i):  
        print(str(i)+" ", end='')
    print()

print("----------------------------")
for i in range(1,7):  
    for j in range(i):  
        print("1 ", end='')
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
"""
print("----------------------------")
for i in range(1,7):  
    for j in range(1,i):  
        print(str(j)+" ", end='')
    print()