# Fibonacci Series : 0 1 1 2 3 5 8 13 ......
#                    0 1 2 3 4 5 6 7  8 

def fibon(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    else:
        return fibon(n-1)+fibon(n-2)

number = 7
print(fibon(number))
#       n-2  n-1   n
# 1,2 , 3 ,  4 ,   5 ,6 7,8

# Create a tree diagram for 7
