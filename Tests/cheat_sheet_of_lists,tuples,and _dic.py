#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
#List
myLst=["hi","my","name","is","Skanda"]
print(myLst)
#List has [] brackets unless you are converting using list()
myLst2=list(("hi",21,25,24,25.09))
print(myLst2)
#you can find what type of data type the list is using type()
myLst3=[2,3,4,5,6,7,8,9,10]
print(type(myLst3))
# add to the end of the list using append()
myLst4=["hi","my","name","is"]
myLst4.append("skanda")
print(myLst4)
#if you want to add something at a specific place, use insert()
myLst4.insert(0,"hello")
print(myLst4)
#if you want to add something from one list to another use extend()
myLst4.extend(myLst3)
print(myLst4)
#Lastly, if you want to delete something use remove()
myLst4.remove("my")
print(myLst4)
#to remove a certain thing, use pop()
myLst2.pop(0)
print(myLst2)
