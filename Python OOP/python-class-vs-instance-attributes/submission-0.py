class BankAccount: 
    total_accounts = 0
    total_balance = 0
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
x1 = BankAccount("Alice",1000)
x2 = BankAccount("Bob",2000)

print(f"Alice's balance: ${x1.balance}")
print(f"Bob's balance: ${x2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")