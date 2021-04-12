class BankAccount:
    def __init__(self, int_rate, balanc): # don't forget to add some default values for these parameters!
        self.int_rate = 0.01
        self.balance = 0
        print("this works")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self

    def display_account_info(self):
    # your code here
        print("int_rate: {self.int_rate}, Balance: {self.balance}")

    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate # self.balance += self.balance * self.int_rate the same thing
        print(self.balance)

an = BankAccount(100)
ok = BankAccount(150)