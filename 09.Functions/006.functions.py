def noPassingNoReturn():
    a=20
    b =30
    print("Sum :",a+b)

def PassingNoReturn(a,b):
    print("Sum:", a+b)

def noPassingButReturn():
    a=20
    b =40
    return f"Sum:{a+b}"

def PassingAndReturn(a,b):
    return f"Sum: {a+b}"


def Numbers():
    print("Hello I am in numbers.")
    return 10
    print("This is me after return")

#calling functions 

print(Numbers())


noPassingNoReturn()
a =30
b =40
# PassingNoReturn(10,30)
PassingNoReturn(a,b)

print(noPassingButReturn())
# x = noPassingButReturn()
# print(x)

print(PassingAndReturn(10,20))
# y = PassingAndReturn(30,40)
# print(y)

