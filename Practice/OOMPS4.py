class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def AnnualSalary(self):
        self.y=("Yearly Salary:",self.salary*12)
        return self.name, self.department, self.y
employee=Employee("Skanda",10000,"computer science")
print(employee.AnnualSalary())
