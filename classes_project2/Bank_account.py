import random, string

# Class for exception handling for the simulation
class BankException(Exception):
    pass

# Main class for the bank app simulation
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        
    # Method to create an account number for a user
    def createAcctNumber(self):
        numList = []
        number = string.digits
        count = 0
        while count < 10:
            num = random.choice(number)
            count += 1 
            numList.append(num) 
        acctNumber = "".join(numList)
        print(f"\nAccount number created: {acctNumber}")
    
    # Method to get the account balance
    def getBalance(self):
        print(f"\nAccount name: {self.name}\nBalance: ${self.balance:.2f}")

    # Method to deposit into the account
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposit complete!")
        self.getBalance()
        
    # Method to check viable transaction
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BankException(f"Sorry, account '{self.name}' has a balance of ${self.balance:.2f}")
        
    # Method to withdraw from user account
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - (amount * 0.05)
            print(f"Withdrawal complete!")
            self.getBalance()
        except BankException as error:
            print(f"Withdrawal interrrupted! {error}")
                    
    # Method to transfer to another account
    def transfer(self, amount, account):
        try:
            print("\n⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕\n\nBeginning transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!✅\n\n⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕⁕")
        except BankException as error:
            print(f"Transfer interrupted!❌ {error}")
            
            
        
        
       
        

        

