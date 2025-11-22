from Practice.NestedAPIs import myData


def account():
    print("Welcome to Expense tracker! Please create an account to continue")
    account=[]
    my_budget=[]
    name=input("Enter your name: ")
    account.append(name)
    income=int(input("Enter your income: "))
    account.append(income)
    currency=input("Enter currency: ")
    account.append(currency)
    budget=int(input("Enter budget"))
    account.append(budget)
    my_budget.append(budget)
    return account,my_budget
def entry():
    my_account=account()
    print(my_account)
    monthly_report=int(input("How many things have you bought this month?"))
    my_account_entry=[]
    for i in range(0,monthly_report+1):
        account_entry=float(input("Enter any groceries or anything you've spent on: "))
        date=input("Enter date ")
        category={1:["business"],2:["education"],3:["grocery"],4:["extra"],}
        print(category)
        my_category=int(input("Enter number which corresponds to which category is your purchase: "))
        total=0
        for item in category:
            total+=str(item[1])
    my_account_entry.append(account_entry)
    my_account_entry.append(date)
    my_account_entry.append(total)












