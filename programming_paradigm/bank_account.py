# bank_account.py

class BankAccount:
    """A simple BankAccount class that supports deposit, withdraw, and balance display."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False  # insufficient funds

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance}")

