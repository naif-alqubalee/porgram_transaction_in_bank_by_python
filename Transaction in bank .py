
class Transaction: # transaction name for class
    def __init__(self, seq, date, amount, operation): 
        self.date = date
        self.amount = amount
        self.operation = operation
        self.seq = seq

class bankAccount: 
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.trans = []

    def add_tran(self, seq,  date, amount, operation):
        transaction = Transaction(seq, date, amount, operation)
        self.trans.append(transaction)

    def get_balance(self):
        balance = 0
        for transaction in self.trans[-5:]:
            if transaction.operation == 'deposit':
                balance += transaction.amount
            elif transaction.operation == 'withdrawal':
                balance -= transaction.amount
        return balance

    def print_reoprt(self):
        print(f"Account Number:  {self.account_number} ")
        print(f"Account Holder: {self.account_holder} ")
        for transaction in self.trans[-5:]:
            print(f"seq: {transaction.seq} | Date: {transaction.date} | Amount: {transaction.amount} | Operation: {transaction.operation} ")
        balance = self.get_balance()
        print(f"Balance: {balance} ")
r = input("report press r:")
if r == "r":
    account = bankAccount('25555668', 'Naif alqubali')
    account.add_tran( '1','2021/3/12', 20000, 'deposit')
    account.add_tran( '2', '2021/4/15', 40000, 'withdrawal')
    account.add_tran( '3', '2021/5/16', 65000, 'withdrawal')
    account.add_tran( '4', '2021/6/2', 30000, 'deposit')
    account.add_tran( '5', '2021/11/29', 15000, 'withdrawal')

    account.print_reoprt()
    print(f"Finshed")
else:
    print(f"Finshed")