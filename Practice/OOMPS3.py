
class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def PassOrFail(self):
        self.y="fail"
        self.z="pass"
        if self.marks<50:
            return self.y,self.name,self.roll
        else:
            return self.z,self.name,self.roll

student=Student("Skanda",23414,45)
print(student.PassOrFail())



