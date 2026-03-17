#M2
# Q4. Build a Loan class that:
# •	Has a common interest rate for all loans.
# •	Each object stores borrower name and principal.
# •	Calculates total payable amount.
# •	Provides a function to update the interest rate.
# •	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.	Creating multiple loan accounts.
# 2.	Updating interest rates.
# 3.	Checking eligibility and total repayment for borrowers.
class Loan:
    interest_rate=10
    def __init__(self,name,principle):
        self.name=name
        self.principle=principle
    def total_payable(self):
        Total=self.principle+self.principle*(self.interest_rate/100)
        return Total
    @classmethod
    def Update_interest(cls,new_rate):
        cls.interest_rate=new_rate
    @staticmethod
    def is_Eligible(salary):
        if salary>500000:
            return "is eligible"
        else:
            return "not eligible"
L1=Loan("Alex perera",20000)
L2=Loan("Panthoja",40000)
L3=Loan("Ellia Tuporia",20000)
Loan.Update_interest(20)
print(L1.is_Eligible(2300000))
print(L1.total_payable())
#my instance has total_payable button which gives my total payable,is_Eligible() button which gives
#is i'm eligible or not,update to update all interest,attributes name and loan amount


