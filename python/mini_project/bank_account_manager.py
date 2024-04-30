
#Bank Account Manager - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}$ into Account {self.account_number}.")
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}$")


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}$ from Checking Account {self.account_number}.")
        else:
            print(f"Insufficient funds in Checking Account {self.account_number}.")
    
    def __str__(self):
        return f"Checking Account {self.account_number}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}$ from Savings Account {self.account_number}.")
        else:
            print(f"Insufficient funds in Savings Account {self.account_number}.")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied {interest}$ interest to Savings Account {self.account_number}.")
    
    def __str__(self):
        return f"Savings Account {self.account_number}"


class BusinessAccount(Account):
    def __init__(self, account_number, balance=0, transaction_fee=1):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        if amount + self.transaction_fee <= self.balance:
            self.balance -= amount + self.transaction_fee
            print(f"Withdrew {amount}$ (+{self.transaction_fee}$ transaction fee) from Business Account {self.account_number}.")
        else:
            print(f"Insufficient funds in Business Account {self.account_number}.")
    
    def __str__(self):
        return f"Business Account {self.account_number}"


checking = CheckingAccount("1234", 1000, 500)
savings = SavingsAccount("5678", 2000, 0.02)
business = BusinessAccount("9012", 5000, 2)

checking.deposit(500)
checking.withdraw(2000)
checking.withdraw(3000)

savings.deposit(1000)
savings.withdraw(500)
savings.apply_interest()

business.deposit(2000)
business.withdraw(1500)

checking.get_balance()
savings.get_balance()
business.get_balance()
