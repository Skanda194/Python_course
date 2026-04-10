class FitnessTracker:
    def __init__(self,username,steps_walked):
        self.username=username
        self.steps_walked=steps_walked
    def steps(self,count):
        self.count=count
        self.total=self.steps.walked+self.count
        self.y="Your step count is:"
        return self.y,self.total
    def calories_burned(self):
        self.calories=0.04*self.steps_walked
        self.z="You have burned"
        self.x="calories"
        return self.z,self.calories,self.x
    def check_goal(self,goal):
        self.goal=goal
        self.a="You've hit your daily limit!"
        self.steps_left=self.goal-self.steps_walked
        if self.goal<self.steps_walked:
            return self.a
        else:
            return self.steps_left




