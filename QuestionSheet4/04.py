import datetime
def date():
    date=datetime.datetime.now()
    print(date)
    currentdate=date.strftime("%Y-%m-%d")
date()
