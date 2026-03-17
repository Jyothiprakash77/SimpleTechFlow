# Q4. Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.
class car:
    Wheels=4
    def __init__(self,mileage):
        self.Mileage=mileage
    def display_specs(self):
        print(f"Wheels->{self.Wheels}")
        print(f"Mileage->{self.Mileage} miles")
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.Wheels=new_wheels
Mahindra=car(9000)
Mahindra.change_wheels(9)
Mahindra.display_specs()
TATA=car(7900)
print(TATA.Mileage)
TATA.display_specs()