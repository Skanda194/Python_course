
def main():
    y=int(input("Welcome to password manager!"
            "press one of the following: "
            "1.Add new "
            "2.View all  "
            "3.manage passwords: "))
    print(y)
    if y==1:
        z=[" "]
        email=input("enter your email (i.e gmail): ")
        print(email)
        password=input("enter your password for your email: ")
        print(password)
        save=input("Would you like to save?: ")
        if save=="yes":
            z.append(email)
            z.append(password)
            print("You have saved",z)
            x=input("Do you need anything else? ")
            print(x)
            if x=="yes":
                print(y)
            elif x=="no":
                print("Have a great rest of your day! \U0001F603")
            else:
                print(ValueError("Invalid option. Say either yes or no"))
                print(x)
        elif save=="no":
            a=input("Do you need anything else? ")
            print(a)
            if a=="yes":
                print(y)
            elif a=="no":
                print("Have a great rest of your day! \U0001F603 ")
            else:
                print(ValueError("Invalid option. Say either yes or no"))
                print(a)
        else:
            print(ValueError("That is an invalid option. say either yes or no"))
            print(save)
    elif y==2:
        print("These are the ones you have so far saved",z)
main()



