print("-------- Even Number Sum Calculator -----------")
number = int(input("Enter an even number :"))

sum = 0
for i in range(2, number+1,2):
    # print(i)
    sum = sum +i
print("Sum of Even numbers is : ",sum)


