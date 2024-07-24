#Revision

# Initialisation - Starting point
# Condition check - Tells how many times a loop will run
# increement - increasing the counter in each iteration
# for i in [4,8,12,16,20,24,28]:
#     print(i)
 
# for i in range(11):
#     print(i)

# Starting point - We can start from any value 
# for i in range(3,10):
#     print(i)

# for i in range(5,10):
#     print(i)

# We can have increement more than 1 also 
# for i in range(3,20,4):
#     print(i)


# Tell me the output 
# for i in range(3,20):
#     if i==8:
#         continue
#     else:
#         print(i*2)

# for i in range(2,40):
#     if i%3==0:
#         print("Divisible by 3")
#     elif i==23:
#         print("23 it is")
#     else:
#         print(i)

for i in range(1,40,3):
    if i<=10:
        print(i*i)
    elif i%11==0:
        print("11's multiple")
    else:
        print(i+4)