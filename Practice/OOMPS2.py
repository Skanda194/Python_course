class BankAccount:
    def __init__(self,balance,amount):
        self.balance=balance
        self.amount=amount
    def deposit(self,):
        return self.balance+self.amount
    def withdraw(self):
        return self.balance-self.amount
Account=BankAccount(1000,5)
print(Account.deposit())
print(Account.withdraw())
