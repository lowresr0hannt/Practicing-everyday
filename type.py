class BankAccount:
    MIN_BALANCE = 100
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance =balance
        
    def deposit (self,amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: {self._balance}")
        else:
            print("deposit amount must be positive")
            
    @staticmethod
    def is_valid_int_rate(rate):
        return 0 <= rate <= 5


account = BankAccount("kat",500)
account.deposit(2000000000)

print(BankAccount.is_valid_int_rate(3))
print(BankAccount.is_valid_int_rate(10))

<<<<<<< HEAD
print(user1.get_email())
=======
>>>>>>> c15947e (bank)
