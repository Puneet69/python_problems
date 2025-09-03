class Bank:
    def __init__(self, acc_num, bal):
        self.balance=bal
        self.account_number=acc_num
    def debit(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Debited:",amount)
    def credit(self,amount):
        self.balance += amount
        print("Amount Credited:",amount)
    def check_balance(self):
        print("Current Balance:",self.balance)
obj1 = Bank(792791479729, 10000)
obj1.check_balance()
obj1.debit(5000)
obj1.credit(2000)
obj1.check_balance()
obj1.debit(8000)
obj1.check_balance()
obj2 = Bank(792791479730, 20000)
obj2.check_balance()
obj2.debit(15000)
obj2.credit(5000)
obj2.check_balance()
obj2.debit(30000)
obj2.check_balance()