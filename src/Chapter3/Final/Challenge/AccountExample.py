import BankAccount as account

#Adding an initial account balance
account1 = account.BankAccount(123,40000)

#Getting initial account balance
print('The balance of account1 is: ' + str(account1.get_balance()))

#Adding balance to the account
account1.deposit(500)

#Getting initial account balance
print('The balance of account1 is: ' + str(account1.get_balance()))

#Getting account info with display method
print(account1.display_account_info())

#Attempt to withdraw more than balance
print(account1.withdraw(500000))

#Attempt do withdraw a small amount
print(account1.withdraw(50))

#Proof the amount was discounted from the original amount
#Getting account info with display method
print(account1.display_account_info())



