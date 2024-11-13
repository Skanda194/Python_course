# 2^3 = 2*2*2

def power(base, expo):      # Call1- base 2 expo=3  call2- base=2 expo=2 call3- base=2 expo=1   call4- base=2 expo=0
    if expo==0:
        return 1
    else:
        return base*power(base,expo-1)     # 2*power(2,2)    # 2*2*power(2,1)  2*2*2*power(2,0)  2*2*2*1 = 8

print(power(2,3))

# 6 - 1+2+3+4+5+6
 
# 5 - 1+2+3+4+5+  6

# 4 - 1+2+3+4  + 5

#3 -1+2+3  + 4 

# 2 - 1+2  + 3

# 1 1+ 2

# 1


# power(3,5)
# 3,5 ----- 3*3*3*3*3 
# 3,4 ----- 3*3*3*3
# 3,3 ----- 3*3*3
# 3,2 ----- 3*3
# 3,1 ----- 3 