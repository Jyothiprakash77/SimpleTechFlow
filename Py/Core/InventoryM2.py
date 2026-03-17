#M2
# Q7. Build an Inventory class that:
# •	Tracks the total number of items across all inventories.
# •	Each instance maintains its own stock dictionary ({"item": quantity}).
# •	Provides a method to add or remove stock.
# •	Allows updating a minimum stock threshold globally.
# •	Offers a static checker to verify if a stock level is below threshold.
# Demonstrate:
# 1.	Managing multiple inventories.
# 2.	Adjusting stock threshold.
# 3.	Using static validation inside the instance logic.
class Inventory:
    min_threshold=3
    total_items=0
    def __init__(self):
        self.stock={}
    def add(self,item,quantity):
        if self.checker(len(self.stock)):
            self.stock.update({item:quantity})
            Inventory.total_items+=1
    def remove(self,item):
        Quantity=self.stock.pop(item,None)
        print("Item got removed")
        Inventory.total_items-=1
        return Quantity
    @classmethod
    def update_threshold(cls,new_value):
        cls.min_threshold=new_value
    @staticmethod
    def checker(level):
        if level>=Inventory.min_threshold:
            print("Invalid can't add")
            return False
        else:
            return True
R3=Inventory()
I2=Inventory()
R3.add("sugar",98)
R3.add("Rice",700)
R3.add("Ginger",4)
Inventory.update_threshold(5)
R3.add("Jeera",90)
print(R3.stock)




