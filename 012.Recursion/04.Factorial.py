# 5! = 5*4*3*2*1 = 120
# 0! = 1 , 1! =1
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
        # 5*fact(4) = 5*4*fact(3) = 5*4*3*fact(2) = 5*4*3*2*fact(1)
        # 5*fact(4) = 5*4*fact(3) = 5*4*3*fact(2) =5*4*3*2*fact(1) =  5*4*3*2*1 = 120

n =5
print(fact(5))

