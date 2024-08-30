#Multiple returns in a function

def MaxNum(a,b):
    if a>b:
        return a
    else:
        return b

for i in range(5):
    if i==3:
        continue      # continue skips the current iteration and will resume from the next
    else:
        print(i)
print("----------------------------------------")
for i in range(5):
    if i==3:
        break   
    # break is used to exit loops - when you encounter break you will exit the loop next statements will not run
    else:
        print(i)

# x= MaxNum(10,20)
# print(x)

def MyNum(x):
    print(x)
    return x+3

m=MyNum(10)
print(m)

