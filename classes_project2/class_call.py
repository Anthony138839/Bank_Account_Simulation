from Bank_account import *

''' User 1 account '''
name1 = input("Enter your name: ").capitalize()
age1 = int(input("Enter your age: "))
if age1 < 18:
    raise BankException("Sorry, you must be 18 and above to open an account!")
else:
    money1 = int(input("How much do you want to use to open the account? $"))
account1 = BankAccount(money1, name1)
account1.createAcctNumber()
account1.getBalance()

amount1 = int(input("\nEnter amount to be deposited: $"))
account1.deposit(amount1)

amount2 = int(input("\nEnter amount to be withdrawn: $"))
account1.withdraw(amount2)
        
''' User 2 account '''
name2 = input("\nEnter name of second account: ").capitalize()
age2 = int(input("Enter age of second account: "))
if age2 < 18:
    raise BankException("Sorry, you must be 18 and above to open an account!")
else:
    money2 = int(input("How much do you want to use to open the account? $"))

account2 = BankAccount(money2, name2)
account2.createAcctNumber()
account2.getBalance()

amount1 = int(input("\nEnter amount to be deposited: $"))
account2.deposit(amount1)

amount2 = int(input("\nEnter amount to be withdrawn: $"))
account2.withdraw(amount2)

transfer_amount = int(input("How much do you want to transfer? $"))
account2.transfer(transfer_amount, account1)