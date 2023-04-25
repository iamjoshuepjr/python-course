class AccountBank:
    
    # Instance Attributes
    def __init__(self, account_id, account_holder, account_balance):
        self.account_id = account_id
        self.account_holder = account_holder 
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if(self.account_balance < amount):
            print("Insufficient balance")
        else:
            self.account_balance -= amount
    
    def check_balance(self):
        return f'Balance USD$ {self.account_balance}'

account = AccountBank(990124, "Joshuép Jr.", 8900)

print(account.check_balance())
account.deposit(5000)
print(account.check_balance())
account.withdraw(3000)
print(account.check_balance())