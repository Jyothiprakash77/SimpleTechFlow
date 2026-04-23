# Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
# override it.
# Demonstrate polymorphism by iterating over a list of different animal objects and calling
# make_sound().
class Animal:
    def make_sound(self):
        print("Animal sounds")
class Dog:
    def make_sound(self):
        print("DOWwwwwwwwwww")
class Cat:
    def make_sound(self):
        print("MEOWwwwwwwwww")
class Cow:
    def make_sound(self):
        print("AMBAaaaaaaaaaa")
D1=Dog()
D2=Dog()
C1=Cat()
Cow1=Cow()
Obj=[D1,D2,C1,Cow1]
for i in Obj:
    i.make_sound()