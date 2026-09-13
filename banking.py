class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def display_customer(self):
        print(f"Customer Name: {self.name}")
        self.account.display_balance()


class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

    def display_transaction(self):
        print(f"Transaction: {self.transaction_type}")
        print(f"Amount: ${self.amount:.2f}")


# Create an account object
account1 = Account("ACC1001", 1000)

# Create a customer object
customer1 = Customer("John Smith", account1)

# Display customer and account details
customer1.display_customer()

print("\n--- Deposit ---")
account1.deposit(500)
account1.display_balance()

print("\n--- Withdrawal ---")
account1.withdraw(200)
account1.display_balance()

# Create transaction objects
transaction1 = Transaction(500, "Deposit")
transaction2 = Transaction(200, "Withdrawal")

print("\n--- Transactions ---")
transaction1.display_transaction()
transaction2.display_transaction()