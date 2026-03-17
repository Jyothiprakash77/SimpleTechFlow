#M2
# Q2. Design a class Product that:
# •	Maintains a base tax rate applicable to all products.
# •	Each product has a name and base price.
# •	Has a method to compute final price including tax.
# •	Can change tax rate for all products using one method.
# •	Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.	Creating multiple products.
# 2.	Changing the tax rate.
# 3.	Showing updated prices and validity checks.
class Product:
    Base_tax=12
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        final_price=Product.Base_tax+self.base_price
        print(final_price)
    @classmethod
    def change_tax(cls,newrate):
        cls.Base_tax=newrate
    @staticmethod
    def valid_price(price):
        if price>0:
            if int(price)==price:
                print("valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
Shampoo=Product("Kerthika Shampoo",230)
Chocolate=Product("Dairy milk",78)
Oil=Product("Parachut oil",56)
Product.change_tax(89)
Shampoo.valid_price(Shampoo.base_price)
Chocolate.valid_price(Chocolate.base_price)
Oil.valid_price(Oil.base_price)
#my instance have product name and its rate,how much tax rate it has and what's the final value of rate ,have a feature to
#change it's tax rate ,feature to check it's own price valid or not
