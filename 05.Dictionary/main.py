#Dictionary:
# Key value pair 
#{ "name": "arvinder",
# "age" : 20 }
# Dictionary_name ={
#     'key1':'Value1',
#     'Key2':Value2 
# }
#Dictionaries are ordered
my_dict ={
    'name':'Arvinder',
    'roll nu':122676,
    'age':24   
}
#Printing the whole dictionary
print(my_dict)

#Getting the length 
print(len(my_dict))

#Type of a dictionary

print(type(my_dict))

#Accessing a particular item in the dictionary

print(my_dict['name']) 
print(my_dict['age']) 

print(my_dict.get('roll nu'))

#Accessing all the keys 

student ={
    'name':'Arvinder',
    'roll nu':122676,
    'age':24,
    'College':'NIT',
    'Country':'India' 
}
print(my_dict.keys())
print(student.keys())
print(student.values())

#Adding a new item 
student['Graduated']=True
print(student)
student.update({'subject':'Computer Scinece'})
print(student)
#update an item of a dictionary 

student['roll nu']=11610184
print(student)

student.update({'roll nu':1234})
print(student)

#Removing an item from dictionary
student.pop('roll nu')
print(student)

#Deletes the last item 
student.popitem()
print(student)

#Empty a dictionary
# student.clear()
# print(student)
#Deleting the dictionary
# del student
# print(student)

#Creating a copy of a dictionary
new_dict = my_dict.copy()
print(" - "*30)
print(new_dict)
