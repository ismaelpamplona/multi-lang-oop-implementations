from datetime import datetime


class BankAccount:
    def __init__(self, account_number: str, account_type: str, balance: float = 0.0):

        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Account number must be a non-empty string.")

        if account_type not in {"checking", "savings"}:
            raise ValueError("Account type must be either 'checking' or 'savings'.")

        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a non-negative number.")

        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number.")

        self.balance += amount
        timestamp = datetime.now().isoformat()
        self.transactions.append(f"[{timestamp}] Deposited: {amount}")

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be a non-negative number.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        timestamp = datetime.now().isoformat()
        self.transactions.append(f"[{timestamp}] Withdraw: {amount}")

    def apply_interest(self, interest_rate: float):
        if self.account_type != "savings":
            raise ValueError("Interest can only be applied to savings accounts.")

        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Interest rate must be a non-negative number.")

        interest = self.balance * (interest_rate / 100)
        self.balance += interest

        timestamp = datetime.now().isoformat()
        self.transactions.append(
            f"[{timestamp}] Interest Applied: {interest} ({interest_rate}%)"
        )
