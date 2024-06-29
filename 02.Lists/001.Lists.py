# What is list and Why do we need it ?
x =30
myList = [10,20,30,40,50]
stringList = ["arvin","Hello","World","Programming","Python"]
# boolList = [True, False, True , False, True]
#mixList = [10 , True , "Hello", 10.30]

#Printing the list
print(myList)

#Lists are index based - 0 1 2 3 4 5

#printing the first element
print(myList[0])


# 40 will be printed
print(myList[3])

# length of a list
print("Length of the list : ",len(myList))

#last item of the list 
print("Last Item : ",myList[len(myList)-1])
print("Last Item : ",stringList[len(stringList)-1])

#Slicing 
# : operator  -> Left = Starting Point : Ending Point : Steps 

print("Slicing the stringlist : ",stringList[0:4])
print("Slicing the stringlist : ",stringList[:4])
print("Slicing the stringlist : ",stringList[0:])
print("Slicing the stringlist : ",stringList[3:])

print("Slicing the stringlist with step 1 : ",stringList[0:4:1])
print("Slicing the stringlist with step 2 : ",stringList[0::2])


#Negative Indexing 
print("Negative Index: ",myList[-2])

print("Slicing the stringlist with Negative Indexing : ",stringList[-4:-1])

#Updating the value in the list 
myList[2]=60

print("Updated myList :",myList)

#Append - to add items at the end of the list

myList.append(70)
print("Updated myList :",myList)

#We can append multiple items 
# myList.append(stringList)
# print("Updated myList :",myList)

#insert - to add items at particular index number 
# myList.insert(indexNumber , item)

myList.insert(1,"Programmer")
print(myList)

# remove - to remove a particular element from the list
myList.remove("Programmer")
print(myList)

# To remove last element from the list
myList.pop()
print(myList)

myList.pop()
print("50 will be removed",myList)

# to delete the complete list
# del myList
