#Bank
class BankAccount:
    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"The amount of {amt} is credited to your account.")
        print(f"Updated balance is {self.balance}")

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amt
            print(f"Withdrew {amt}. Current balance is: {self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.acc_holder}, Balance: {self.balance}")


# Derived class for Savings Account
class SavingAccount(BankAccount):
    def __init__(self, acc_holder, balance=0, interest_rate=0.05):
        super().__init__(acc_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of {interest}. New balance is: {self.balance}")


# Derived class for Current Account
class CurrentAccount(BankAccount):
    def __init__(self, acc_holder, balance=0, overdraft_limit=500):
        super().__init__(acc_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amt):
        if amt > self.balance + self.overdraft_limit:
            print("Withdrawal denied! Overdraft limit exceeded.")
        else:
            self.balance -= amt
            print(f"Withdrew {amt}. New balance is: {self.balance}")

def operation():
    print("Welcome to the Bank System!")

    acc_holder = input("Enter the Account holder's Name: ")
    account_type = input("Choose account type (1.Savings 2.Current): ")

    if account_type == "1":
        print(f"\nCreating a Savings Account for {acc_holder}.")
        account = SavingAccount(acc_holder)
        account.display_balance()

        while True:
            ch = input("\nChoose an Operation: 1. Deposit 2. Withdraw 3. Apply Interest 4. Exit\n ")
            if ch == "1":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif ch == "2":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif ch == "3":
                account.apply_interest()
            elif ch == "4":
                print("Thank you for using the Bank System!")
                break
            else:
                print("Invalid option. Try again.")

    elif account_type == "2":
        print(f"\nCreating a current account for {acc_holder}.")
        account = CurrentAccount(acc_holder)
        account.display_balance()

        while True:
            ch = input("\nChoose an Operation: 1. Deposit 2. Withdraw 3. Exit\n ")
            if ch == "1":
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            elif ch == "2":
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif ch == "3":
                print("Thank you for using the Bank System!")
                break
            else:
                print("Invalid option. Try again.")
    else:
        print("Invalid account type chosen. Please start again.")

operation()
