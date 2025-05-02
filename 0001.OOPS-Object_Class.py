# Object Oriented Programming -- 

# We have built in data strcuture -- int float string

# A person -- Name , City , Phone , EployeeId , age ,email etc.

# name= "Skanda"
# age = 23
# city="USA"

# Objects for real world entities 
# User Defined data structure -- 

# '''
# Person{
#   name:"Arvinder"
#   age:23
#   city:"India"
#   EmpId:123456
#   email:"cool@gmail.com"
# }

# car {
#   color
#   Model 
#   year 
  
#   SpeedUp()
#   StartingEngine()
#   HonkingHorn()
#   ApplyBrake()
  
# }
# '''

# Class -- A blueprint -- 
# class Car:
#   def __init__(self):
#     self.color="Red"
#     self.model ="BMW"
#     self.year = 2020
  
#   def StartEngine(self):
#     print("Starting Engine")
    
#   def HonkingHorn(self):
#     print("Honking Horn")

# # Objects using the Class -- Real world entity
# Car1 = Car()
# Car1.StartEngine()
# print(Car1.color)

# Car2 = Car()
# Car2.StartEngine()
# print(Car2.model)

#  Lists , Sets , Dictionary , Tuple 

class Student:
  def __init__(self,name , age):
    self.name = name 
    self.age = age 
  
  def StudyCoding(self):
    print(self.name ,"is studying coding.")
  
  def AgeCalculator(self):
    print(self.name , "is",self.age ,"years old.")
    
Arvinder = Student("Arvinder",23)
Arvinder.StudyCoding()
Arvinder.AgeCalculator()

Skanda = Student("Skanda",17)
Skanda.StudyCoding()
Skanda.AgeCalculator()


# Create a class for an Employee with fields Name , EmpId , Department , city

# Methods -- 1. he works in department 
# 2. He lives in Some city
# 3. His Empd Id is this.  --- PrintDetails -- Name and ID , Department , City
