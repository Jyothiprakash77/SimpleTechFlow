# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.
class Car:
    def start(self):
        print("Car is Starting")
class Computer:
    def start(self):
        print("Computer is Starting")
class WashingMachine:
    def start(self):
        print("WashingMachine is Starting")
def operate(device):
    device.start()
C1=Car()
Com1=Computer()
WM1=WashingMachine()
operate(C1)
operate(Com1)
operate(WM1)
#Polymorphism work by behaviour not by type