# # Object Oriented Programming -- A different way of writting code

# x = 40
# print(type(40))
# # Person -- NAme --String , Height - int , Address -- City , Pincode , State  
# height = 156
# city = "Sirsa"

# # class Person{
# #     Name string 
# #     height int 
# #     city string 
# # }

# # Object -- Skanda ,156 , USA , 
# # p1 = Person("Skanda",165,"USA")
# # p2 = Person("Arvin",160,"India")

# # Class is just the blueprint. Object is the real world entity 
# # Class -- 

# # x = 30 
# # print(type(x))
import math
class Circle:
    def __init__(self,radius):
        self.radius= radius
    
    def calculate_area(self):
        return math.pi*self.radius**2
    
    def circumference(self):
        return math.pi*2*self.radius

# object1 = <ClassName>()
c1 = Circle(10)
# TO access any attributes (variables) and methods of a class using the . (dot operator)
# c1.radius 
# c1.calculate_area()
print(c1.circumference())
print(int(c1.calculate_area()))




    

    

    

        


