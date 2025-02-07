class BankAccount:
    def __init__(self, o, b=0):
        self.o = o
        self.b = b

    def deposit(self, am):
        self.b += am
        print(f"{am} added , balance: {self.b}.")

    def withdraw(self, am):
        if am > self.b:
            print("Withdrawal amount is too big")
        else:
            self.b -= am
            print(f"{am} withdrawn, balance: {self.balance}.")
    def owner_name(self, n):
        self.n = n
account = BankAccount("Elza")

account.deposit(int(input()))
account.deposit(int(input()))

account.withdraw(int(input()))
account.withdraw(int(input()))
account.owner_name(print(input("Owners name:")))