class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0.0

    def Accept(self):
        self.Name = input("Enter Account Holder Name: ")
        self.Amount = float(input("Enter Initial Amount: "))

    def Deposit(self):
        deposit_amt = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amt

    def Withdraw(self):
        withdraw_amt = float(input("Enter amount to withdraw: "))
        if withdraw_amt <= self.Amount:
            self.Amount -= withdraw_amt
        else:
            print("Insufficient Balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on current balance: {interest}")

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")


# Using the class
acc1 = BankAccount()
acc1.Accept()
acc1.Deposit()
acc1.Withdraw()
acc1.CalculateInterest()
acc1.Display()
