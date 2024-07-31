"""
1 2 3 4 5
2 3 4 5 
3 4 5
4 5
5
"""
print("----------------------------")
rows =5
for i in range(0,rows+1,1):  
    for j in range(i+1,rows+1):  
        print(j, end=' ')
    print(" ")