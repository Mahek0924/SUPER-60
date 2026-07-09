class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder,
                 balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._BankAccount__balance * self.interest_rate
        self.deposit(interest)
        print("Interest added:", interest)


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder,
                 balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and (
            self._BankAccount__balance - amount
        ) >= -self.overdraft_limit:
            self._BankAccount__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Overdraft limit exceeded")


# User Input

account_number = input("Enter Account Number: ")
account_holder = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

print("\n1. Savings Account")
print("2. Current Account")

account_type = int(input("Enter Account Type: "))

if account_type == 1:
    account = SavingsAccount(
        account_number,
        account_holder,
        balance
    )

elif account_type == 2:
    account = CurrentAccount(
        account_number,
        account_holder,
        balance
    )

else:
    print("Invalid Account Type")
    exit()


# Menu

while True:

    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Add Interest")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        if isinstance(account, SavingsAccount):
            account.add_interest()
        else:
            print("Interest is only for Savings Account")

    elif choice == 5:
        print("Thank you for using Bank System")
        break

    else:
        print("Invalid choice")