food={1:["pizza margherita","35.99"],2:["soda","2.99"],3:["pepperoni pizza","37.99"],4:["veggie pizza","40.99"],5:["meat lover's pizza","42.99"]}
def menu():
    print(food)
def order():
    amount=int(input("How many people are there? "))
    common=int(input("Are you guys having a common item or are you all ordering different items? Order 1 for common and 2 for different option "))
    orders=[]
    if common==1:
        menu()
        have=int(input("What would you like to have? Enter the item number: "))
        item=int(input("How many items are there? "))
        if have in food.keys():
            for i in range(1,item+1):
                orders.append(food[have])
    elif common==2:
        for i in range(1,amount+1):
            separate=int(input("Enter the item number: "))
            if separate in food:
                orders.append(food[separate])
    else:
        print(ValueError("This is an invalid input"))
    return orders
def price(orders):
        total = 0
        for item in orders:
            total += float(item[1])
        return total
def tax():
    y=order()
    x=price(y)
    print("Without taxes:",x)
    taxes=x*0.06
    with_taxes=x*0.06+x
    print("With taxes:",with_taxes)
    return with_taxes
def tip():
    a=tax()
    tips=int(input("How much do you want to tip, press 1 for 15%, 2 for 20%, and 3 for no tip "))
    if tips==1:
        print("With tip:",a*0.15+a)
        return a*0.15+a
    elif tips==2:
        print("With tip:",a*0.2+a)
        return a*0.2+a
    elif tips==3:
        print("Total price:",a)
        return a
    else:
        return "Invalid input"
my_tip=tip()
print(my_tip)












#def payment():
   # y=order()









