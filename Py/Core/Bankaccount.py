# Q9. Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.
class BankAccount:
    bank_name="Uththuththi bank"
    def __init__(self,holder,balance):
        self.Holder=holder
        self.balance=balance
    def deposit(self,amount):
        if self.validate_amount(amount):
            self.balance+=amount
            print(f"{self.Holder}'s Total balance:{self.balance}")
        else:
            print("Invalid Amount")
            print(f"{self.Holder}'s Total balance:{self.balance}")
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amt):
        return amt>0
Afhridi=BankAccount("Afhidi",120000)
SuryaKumar=BankAccount("SuryaKumar",90000)
SuryaKumar.deposit(5000000)
Afhridi.deposit(0)