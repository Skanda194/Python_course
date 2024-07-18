#Python program to print a multiplication table of a given number

print(" ---- Number Table printer ---- ")

number = int(input("Enter a number : "))

for i in range(1,11):
    print(number,"*",i,"=",number*i)