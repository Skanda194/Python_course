import datetime
import json
def first_requirement():
    obj=int(input("Welcome to Calendar"
          "This is a calendar in which you can put certain events"
           "Select 1 for knowing the date: "
              "Select 2 for the time: "))
    result=json.dumps(obj)
    if obj=="1":
        time=datetime.datetime(2025,4,3)
        print("it is",time)
    elif obj=="2":
        times=datetime.datetime(2025,4,3)
        print(times.striftime("%I"),("%M"),("%p"))
first_requirement()





