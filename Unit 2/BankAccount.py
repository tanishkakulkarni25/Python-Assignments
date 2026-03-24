#Create a class to represent a bank account. Include attributes like account number,balance,and 
#methods like deposit,withdraw and check balance.
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited", amount, ". New balance:", self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrew", amount, ". New balance:", self.balance)
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print("Account", self.account_number, "balance:", self.balance)
        return self.balance
    
account = BankAccount(12345, 100)
account.check_balance()
account.deposit(50)
account.withdraw(5)