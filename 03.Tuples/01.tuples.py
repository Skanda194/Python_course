#Unchangable , ordered , allow duplicates
myTuple = ("Apple","Banana","Coconut")
print(myTuple)

print("Length: ",len(myTuple))

myTuple2 =("Hello",23,100.50,"World",True)
print(myTuple2)


print(myTuple[1])
# myTuple[2]= "Random"
# print(myTuple)
print(myTuple[-1])

#Changing the items of myTuple2

myTupleList = list(myTuple2)
print(myTupleList)
myTupleList[2]= "Random"
myTuple2 =  tuple(myTupleList)
print(myTuple2)

myNewTuple = myTuple + myTuple2
print(myNewTuple)

singleTuple = ("Orange",)
myLatestTuple = myTuple + singleTuple

myLatestTuple = singleTuple + myTuple
print(myLatestTuple)

#Multiply tuple 

multiplyTuple = myTuple*3
print("Multiplied Tuple :",multiplyTuple)

#Removing Elements from Tuple
thisTuple = (12,13,45,67,84,20,28,20)
thisList = list(thisTuple)
thisList.remove(13)
thisTuple = tuple(thisList)
print(thisTuple)


#Unpacking of tuple 
#myTuple = ("Apple","Banana","Coconut")
# (first,second,third)=myTuple
# print(second)

# myTuple2 =("Hello",23,100.50,"World",True)
(first,second,*third)=myTuple2
print(second)
print(third)








