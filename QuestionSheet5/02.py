def List():
    i=0
    myList=[1,2,3,4,5,6,7]
    for i in myList:
        if i in myList%2==0:
            print("True")
        else:
            print("False")
List()