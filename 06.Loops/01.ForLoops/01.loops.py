#Repetetion 

#How to print a statement 10 times
#First method
#print("Hello\n"*10)
# print("Hello\n"*100)
#Second method 
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# for i in range(10):
#     print("Hello")

# for i in range(2,10):
#     print(i)

# for i in range(2,10,2):
#     print(i)
#i = 0
# Condition Check - i>10 - No 
# Print
# i++ == i +1 

# fruits = ["Apple","Banana", "Cherry", "Dates"] 
# for f in fruits:
#     print(f)

# touple = ("Apple","Banana", "Cherry", "Dates")
# for f in touple:
#     print(f)

# set = {"Apple","Banana", "Cherry", "Dates"}
# for f in set:
#     print(f)

#fruitsDictionary = {"A":"Apple","B":"Banana","C":"Cherry","D":"Dates"}
# for f in fruitsDictionary:
#     print(f)

# for f in fruitsDictionary:
#     print(fruitsDictionary[f])

# for key, value in fruitsDictionary.items():
#     print(key , value)


# for f in fruitsDictionary.keys():
#     print(f)

#Strings 
# for x in "Hello World":
#     print("-", x ," -\n")

# for x in [1,2,3,4,4,5]:
#     print(x)

#Continue -- to skip a particular iteration
# for x in [1,2,3,4,4,5]:
#     if x ==4:
#         continue
#     else:
#         print(x)

#Break 
for x in [1,2,3,4,4,5]:
    if x ==4:
        break
    else:
        print(x)