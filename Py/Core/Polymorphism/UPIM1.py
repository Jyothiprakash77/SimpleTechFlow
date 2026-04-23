# Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
# pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling
# pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.
#we use duck typing for achieve polymorphism in different classes
class UPI:
    def pay(self,amount):
        print(f"Rs.{amount} has debitted from UPI")
class Card:
    def __init__(self,PIN):
        self.__pin=PIN
    def Setter(self,PIN):
        self.__pin=PIN
    def pay(self,pin,amount):
        if pin==self.__pin:
            print(f"Rs.{amount} has been debitted from card")
        else:
            print("Invalid Pin")
class Cash:
    def pay(self,amount,N500=0,N200=0,N100=0,N50=0,N20=0,N10=0):
        if amount==(N500*500)+(N200*200)+(N100*100)+(N50*50)+(N20*20)+(N10*10):
            print(f"Rs.{amount} is payed successfully")
        else:
            print("Invalid notes")
def payment(k,amount,pin=0,Nt500=0,Nt200=0,Nt100=0,Nt50=0,Nt20=0,Nt10=0):
    if isinstance(k,UPI):
        k.pay(amount)
    elif isinstance(k,Card):
        k.pay(pin,amount)
    elif isinstance(k,Cash):
        k.pay(amount,N500=Nt500,N200=Nt200,N100=Nt100,N50=Nt50,N20=Nt20,N10=Nt10)
    else:
        print("invalid way")
# payment(UPI(),8000)
# payment(Card(2367),6700,2367)
C1=Card(9089)