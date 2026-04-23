# 1.  Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.
class BankAccount:
    def __init__(self,min_deposit=6700):
        self.Account_Number="PYU9893467981"
        self.__balance=min_deposit
    @property
    def Balance(self):
        return f"Rs.{self.__balance} /-"
    #data masking
    def deposit(self,amount):
        if amount<=25000:
            self.__balance+=amount
            print(f"Total balance is Rs.{self.__balance}")
        else:
            print("Try another day")
    def withdraw(self,amount):
        if amount>0:
            self.__balance-=amount
            print(f"Rs.{amount} is withdrawed")
        else:
            print("Invalid Amount")
B1=BankAccount()
B1.withdraw(5000)
print(B1.Balance)

