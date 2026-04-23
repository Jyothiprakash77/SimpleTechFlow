class Monkey:
    legs=2
    hands=2
    def __init__(self,hairColour):
        self.hair_colour=hairColour
    def walk(self):
        print(f"Walks on {self.legs} legs")
    def eats(self):
        print(f"Eats with {self.hands} hands")
class Human(Monkey):
    def __init__(self,IQ):
        self.IQ=IQ

H1=Human(980)
H1.walk()