class Smartphone:
    def __init__(self,brand,model,battery_level):
        self.brand=brand
        self.model=model
        self.battery_level=battery_level
    def call(self,minutes):
        self.minutes=minutes
        self.y="You've been calling for",self.minutes,"minutes, your new battery percentage is"
        self.z=self.battery_level-self.minutes
        self.x="Your battery level",self.battery_level,"is less than the time you have your call for, which is",self.minutes,"try calling later"
        if self.minutes>1:
           return self.y,self.z
        elif self.battery_level<self.minutes:
            return self.x
    def charge(self,amount):
        self.amount=amount
        self.a="You cannot charge this high, try a different amount"
        self.b="Your new charge is:"
        self.c=self.z+self.amount
        if self.z+self.amount>100:
            return self.a
        else:
            return self.b,self.c
    def status(self):
        self.d="is at"
        self.e="Your"
        return self.e,self.brand,self.model,self.d,self.c
phone=Smartphone("Iphone","17 pro max",24)
print(phone.call(10))
print(phone.charge(87))
print(phone.status())











