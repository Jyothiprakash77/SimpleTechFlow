# • Implement hierarchical inheritance using a base class Vehicle and two child
# classes Car and Bike, each defining a method wheels().
class Vehicle:
    @classmethod
    def wheels(cls):
        print(2)
class car(Vehicle):
    @classmethod
    def wheels(cls):
        print(4)
class Bike(Vehicle):
    @classmethod
    def wheels(cls):
        print("2 Wheels")
C1=car()
B1=Bike()
C1.wheels()
B1.wheels()