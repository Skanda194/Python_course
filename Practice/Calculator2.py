file=open('test.txt','r')
print(file.readline())
print(file.readline())
print(file.readline())
y=(file.readline())
def calculator(a,b):
    if "+" in file:
        print(a+b)
    elif "-" in file:
        print(a-b)
    elif "*" in file:
        print(a*b)
    elif "/" in file:
        print(a/b)
    else:
        ValueError("This is an invalid input")