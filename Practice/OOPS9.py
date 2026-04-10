class Hero:
    def __init__(self,name,health,experience):
        self.name=name
        self.health=health
        self.experience=experience
    def damage(self,take_amount):
        self.take_amount=take_amount
        self.y="Your health is at zero, the hero has fainted!"
        self.d="Your new health after damage is:"
        self.z=self.health-self.take_amount
        if self.health<self.take_amount:
            return self.y
        else:
            return self.d,self.z
    def rest(self):
        self.boost=20
        self.b=self.z+self.boost
        self.a=self.z+100-self.z
        self.h="Your new health after resting is:"
        if self.z+self.boost>100:
            return self.h,self.a
        else:
            return self.h,self.b
    def gain_xp(self,amount):
        self.amount=amount
        self.level="Level up"
        self.gain=self.experience+self.amount
        self.resetexp="Your experience resetted"
        self.reset=self.gain*0
        self.newexp="Your new experience score is:"
        if self.gain>100:
            return self.level,self.resetexp,self.reset
        else:
            return self.newexp,self.gain
    def overview(self):
        return self.name, self.b,
hero=Hero("skanda",100,1)
print(hero.damage(20))
print(hero.rest())
print(hero.gain_xp(100))






