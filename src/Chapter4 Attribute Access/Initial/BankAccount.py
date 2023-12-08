class BankAccount:
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance

    
    def set_deposit(self, amount):
        if amount < 200:
            raise ValueError('Minimum deposit has to be > 200')
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
        
    @property
    def annual_salary(self):
        return self.balance * 12
            