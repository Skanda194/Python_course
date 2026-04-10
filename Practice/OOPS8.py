class Coffee_Machine:
    def __init__(self,water,coffee_beans,milk):
        self.water=water
        self.coffee_beans=coffee_beans
        self.milk=milk
    def latte(self):
        self.y="Here's your latte!"
        self.x="Your current levels are"
        self.a="Sorry, refill required"
        self.z=self.water-200,self.milk-100,self.coffee_beans-20
        if self.water>=200 and self.milk>100 and self.coffee_beans>20:
            return self.y,self.x,self.z
        else:
            return self.a
    def report(self):
        return self.x,self.z
coffee=Coffee_Machine(12093,123,1093)
print(coffee.latte())



