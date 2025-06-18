class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display(self):
        print(f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}")

acc = BankAccount(12345, "Priya", 10000)
acc.deposit(2000)
acc.withdraw(1500)
acc.display()
