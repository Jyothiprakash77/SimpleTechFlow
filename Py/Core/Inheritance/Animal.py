# • Create a base class Animal with a method sound(). Create a derived class Dog
# that overrides the sound() method. Demonstrate method overriding.
class Animal:
    def sound(self):
        print("zZzZzZzZzZzZzZzZ")
class Dog(Animal):
    def sound(self):
        print("Dowwwwwwwwwwww")
        super().sound()
Spike=Dog()
Spike.sound()
