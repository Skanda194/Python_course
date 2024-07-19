print("---- Product calculator -----")

number = int(input("Enter a number : "))

product = 1
for i in range(1,number+1):
    product = product*i

# i=1 - product =1    -> product = 1*1 = 1
# i=2 - product =1    -> product = 1*2 = 2
# i=3 - product =2    -> product = 2*3 = 6
# i=4 - product =6    -> product = 6*4 = 24
print(product)
