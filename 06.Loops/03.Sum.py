# Python program to calculate the sum of all numbers from 1 to a given number.

print("------ Find the sum of N Numbers ----------")
number = int(input("Enter a number: "))

sum = 0
for i in range(1, number+1):
    # print(i)
    print("The sum in ",i ,"iteration is ",sum)
    sum = sum + i
    
# i=1 - sum =0   -> sum = 0+1 = 1
# i=2 - sum =1    -> sum = 1+2 = 3
# i=3 - sum =3   -> sum = 3 + 3 = 6
# i=4  - sum =6   -> sum =  6 + 4 = 10 
print(sum)

 