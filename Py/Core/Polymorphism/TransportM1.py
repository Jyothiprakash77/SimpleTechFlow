# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.
class Transport:
    def move(self):
        print("Takes you to one place to another")
class Bus(Transport):
    def move(self):
        super().move()
        print("Moves on four wheels")
class Bike(Transport):
    def move(self):
        super().move()
        print("Moves on two wheels")
B1=Bus()
B1.move()
print("")
Bik1=Bike()
Bik1.move()