class PaymentProcessor:
    def __init__(self):
        self.balance = 0

    def add_funds(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def pay(self, price):
        if price > self.balance:
            raise Exception("Insufficient funds")
        
        if price <= 0:
            raise ValueError("Amount must be positive")
        self.balance -= price
