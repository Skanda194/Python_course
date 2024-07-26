"""
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
"""
# for i in range(1,7):  
#     for j in range(i):  
#         print(str(i)+" ", end='')
#     print()

# for i in range(1,10):
#     print(i)
# for i in "ABCDEFGHIJ":
#     print(i)

rows, cols = (5, 5)
print([[i+j for i in range(1,cols)] for j in range(1,rows)])
# i =1 - j= 1, 1 ,2,3,4,5
# 
# 11    12   13  14 
# 21    22   23  24
# 31    32   33  34
