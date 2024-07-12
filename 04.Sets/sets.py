#Sets - Unordered , Unmutable , unidexed , duplicates are not not allowed

# my_list = [29,30,45,879]
# print(my_list[3])
my_sets ={1,45,67,37,20}
print(my_sets)

#Duplicates are not allowed
my_sets2= {20,20,30,34,50,50,49,60}
print(my_sets2)

mySets3= {"Hello", 100, 245.67, True, 'A'}

#True ==1 , False ==0
my_sets4={True , 1 , 0 , False}
print(my_sets4)

# We can add/remove elements from sets but we can not chage the exxisting elements 
#mySets3= {"Hello", 100, 245.67, True, 'A'}
mySets3.add(300)
mySets3.add("Hello World")

print(mySets3)

#Removing a particular item from the sets
# mySets3.remove("Hello3")
# print(mySets3)

mySets3.discard("Hello3")
mySets3.discard("Hello")
print(mySets3)


#Pop to remove an item from sets
# mySets3.pop()

#Clear a set - make it empty
# mySets3.clear()
# print(mySets3)

#JOin sets
#mySets3= {"Hello", 100, 245.67, True, 'A'}
#my_sets4={True , 1 , 0 , False}

new_set = mySets3.union(my_sets4)
print(new_set)

#Take the common items only
new_set = mySets3.intersection(my_sets4)
print(new_set)

my_list = [10,20,30,40]
my_sets5 = mySets3.update(my_list)
print(my_sets5)
# del mySets3
# print(mySets3)



