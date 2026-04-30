class Account:
    def __init__(self,  name , bal , acc):
        self.name = name
        self.balance = bal
        self.acc =  acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "debited")
        print("total balance = ", self.get_balance)

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount ,"credited ")
        print("total balance = ", self.get_balance)

    def get_balance(self):
        return self.balance
    
acc1 = Account("Kavya Kushwaha", 10000, 4500)
print(acc1.name , acc1.balance , acc1.acc)

acc1.debit(1000)
acc1.credit(90000)


