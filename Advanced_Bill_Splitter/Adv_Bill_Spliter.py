def prices():
    Pizza_Margherita=35.99
    Wine_Bottle=45.00
    Desert_Platter=22.50
    y=input("Welcome to this restaurant! Enter food: ")
    x=input("is there more food? ")
    if y=="pizza margherita":
        print("price: ",Pizza_Margherita)
        multiple=input("do you want multiple of the same item? ")
        if multiple=="yes":
            multiple2=int(input("how many? "))
            print("price",Pizza_Margherita*multiple2)
        else:
            print("Alright then price is:",Pizza_Margherita)
            Split=input("Do you want to split the item? ")
            if Split=="yes":
                percent=int(input("Enter the amount of people splitting the bill: "))
                if percent == 1:
                    print(ValueError("Sorry, an Error happened"))
                elif percent == 2:
                    print("for first and second person amount due:",Pizza_Margherita*0.5,)
                elif percent == 3:
                    print("first, second , and third person amount due:",Pizza_Margherita/3)
                elif percent == 4:
                    print("All 4 people amount due:",Pizza_Margherita/4)
                elif percent == 5:
                    print("All 5 people amount due:",Pizza_Margherita/5)
                elif percent == 6:
                    print("All 6 people amount due:",Pizza_Margherita/6)
                elif percent == 7:
                    print("All 7 people amount due:",Pizza_Margherita/7)
                elif percent == 8:
                    print("All 8 people amount due:",Pizza_Margherita/8)
                elif percent == 9:
                    print("All 9 people amount due:",Pizza_Margherita/9)
                elif percent == 10:
                    print("All 10 people amount due:",Pizza_Margherita/10)
                else:
                    print(ValueError("Sorry an Error Occured"))
    elif y=="Wine Bottle":
        print("price:",Wine_Bottle)
        multiple = input("do you want multiple of the same item?")
        if multiple == "yes":
            multiple2 = int(input("how many?"))
            print("price",Wine_Bottle * multiple2)
        else:
            print("Alright then, price:",Wine_Bottle)
        Split = input("Do you want to split the item? ")
        if Split == "yes":
            percent = int(input("Enter the amount of people splitting the bill: "))
            if percent <= 1:
                print(ValueError("Sorry, an Error happened"))
            elif percent == 2:
                print("for first and second person amount due:", Wine_Bottle * 0.5, )
            elif percent == 3:
                print("first, second , and third person amount due:", Wine_Bottle/ 3)
            elif percent == 4:
                print("All 4 people amount due:", Wine_Bottle / 4)
            elif percent == 5:
                print("All 5 people amount due:", Wine_Bottle / 5)
            elif percent == 6:
                print("All 6 people amount due:", Wine_Bottle / 6)
            elif percent == 7:
                print("All 7 people amount due:", Wine_Bottle / 7)
            elif percent == 8:
                print("All 8 people amount due:", Wine_Bottle/ 8)
            elif percent == 9:
                print("All 9 people amount due:", Wine_Bottle/ 9)
            elif percent == 10:
                print("All 10 people amount due:", Wine_Bottle / 10)
            else:
                print(ValueError("Sorry an Error Occured"))
    elif y=="Dessert Platter":
        print("price:",Desert_Platter)
        multiple = input("do you want multiple of the same item? ")
        if multiple == "yes":
            multiple2 = int(input("how many?"))
            print("price",Desert_Platter * multiple2)
        Split = input("Do you want to split the item? ")
        if Split == "yes":
            percent = int(input("Enter the amount of people splitting the bill: "))
            if percent == 1:
                print(ValueError("Sorry, an Error happened"))
            elif percent == 2:
                print("for first and second person amount due:", Desert_Platter * 0.5, )
            elif percent == 3:
                print("first, second , and third person amount due:", Desert_Platter / 3)
            elif percent == 4:
                print("All 4 people amount due:", Desert_Platter/ 4)
            elif percent == 5:
                print("All 5 people amount due:", Desert_Platter / 5)
            elif percent == 6:
                print("All 6 people amount due:", Desert_Platter / 6)
            elif percent == 7:
                print("All 7 people amount due:", Desert_Platter/ 7)
            elif percent == 8:
                print("All 8 people amount due:", Desert_Platter / 8)
            elif percent == 9:
                print("All 9 people amount due:", Desert_Platter/ 9)
            elif percent == 10:
                print("All 10 people amount due:", Desert_Platter / 10)
            else:
                print(ValueError("Sorry an Error Occured"))

    if x=="yes":
        z=input("enter the next food: ")
        if z=="pizza margherita" and y=="pizza margherita":
            print("combined price:",z+y)
        elif z=="pizza margherita" and y=="Wine Bottle":
            print("combined price:",z+y)
        elif z=="pizza margherita" and y=="Desert Platter":
            print("combined price:",z+y)
        elif z=="Wine bottle" and y=="Pizza margherita":
            print("combined price:",z+y)
        elif z=="Wine bottle" and y=="Desert platter":
            print("combined price:",z+y)
        elif z=="Desert Platter" and y=="Pizza margherita":
            print("combined price:",z+y)
        elif z=="Desert Platter" and y=="Wine Bottle":
            print(z+y)
    #elif x=="no":
     #   print("your current price is:",Desert_Platter)
      #  a=input("is there more food?")
       # if a=="yes":
        #    b=input("Enter the next food")
prices()






