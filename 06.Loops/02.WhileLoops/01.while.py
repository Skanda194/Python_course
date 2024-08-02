# i = 1
# while i<6:
#     print(i)
#     i += 1 

# i = 0
# while i<6:
#     i += 1 
 
# for i in range(11):
#     print(i)
    
#     if i==3:
#         continue
#     print(i)

# i = 0
# while i<6:
#     i += 1 
    
#     if i==3:
#         break
#     print(i)

#Infinite Loop
# i = 0
# while i<6:
#     # i += 1 # i =i+1
#     if i==3:
#         continue
#     print(i)

# i = 10
# while i> 0:
#     print(i)
#     i -=1     # i = i-1

# choice = input("Enter Y to play tha game or N to exit")
# while True:
#     if choice=="Y":
#         print("Let's start the game")
#     else:
#         print("Exiting")

# print("------ Find the sum of N Numbers ----------")
number = int(input("Enter a number: "))

# sum =0
# while True:
#     sum +=number
#     number -=1
#     if number ==0:
#         break
# print(sum)

# while True:
#     sum +=number
#     number -=2
#     if number ==0:
#         break
# print(sum)

product =1
while True:
    product *=number
    number -=1
    if number ==0:
        break
print(product)