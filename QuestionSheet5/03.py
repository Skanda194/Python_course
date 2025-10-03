def number():
    myList=[1,2,3,4,5,6,7,8,9,10]
    y=int(input("Enter a number: "))
    if y>=0:
        myList.append(y)
        print("The new list is ",myList)
    else:
        print("put a number greater than -1")
number()