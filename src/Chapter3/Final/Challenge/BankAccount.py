class BankAccount:
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account {self.account_number} has a balance of {self.balance}"


    def withdraw(self, amount):
        if self.balance <= amount:
            return f"Not enough funding to withdraw: {amount}"
        else:
            self.balance = self.balance - amount
            return f"Success - enough funding to withdraw: {amount}"
            