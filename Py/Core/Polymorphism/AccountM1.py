# Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.
class Account:
    def withdraw(self,amt):
        print(f"Amount of Rs.{amt} has been withdrawn")
class SavingsAccount(Account):
    def withdraw(self,amt):
        print(f"Amount of Rs.{amt} has been withdrawn from savings account")
class PremiumSavingAccount(SavingsAccount):
    def withdraw(self,amt):
        print(f"This is Premium Saving Account:")
        super().withdraw(amt)
A1=Account()
SA1=SavingsAccount()
PSA1=PremiumSavingAccount()
A1.withdraw(20000)
SA1.withdraw(20000)
PSA1.withdraw(20000)