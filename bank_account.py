class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if amount > 0:
            self.balance -= amount

    def get_balance(self) -> float:
        return self.balance

