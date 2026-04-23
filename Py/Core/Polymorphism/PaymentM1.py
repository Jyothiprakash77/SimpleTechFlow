# Q6. Design:
# • Base class Payment with process(amount)
# • Subclass CreditCardPayment adds process(amount, card_type)
# Demonstrate what happens when overriding with different signatures and how Python
# handles it.
class Payment:
    def process(self,amount):
        print(f"Payment of Rs.{amount} is successfully done")
class CreditCardPayment(Payment):
    def process(self,amount,card_type):
        if card_type=="Gold":
            print(f"Payment of Rs.{amount} is successfully done")
            print("Enjoy the services of gold card")
        elif card_type=="Preminum":
            print(f"Payment of Rs.{amount} is successfully done")
            print("Enjoy the services of Premium services")
        else:
            print(f"Payment of Rs.{amount} is successfully done")
C1=CreditCardPayment()
P1=Payment()
C1.process(90000,"Gold")
P1.process(8707)