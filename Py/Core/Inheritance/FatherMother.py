# • Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO.
class Mother:
    def skill(self):
        print("Cooking")
        super().skill()
class Father:
    def skill(self):
        print("Farming and Doctor")
class child(Mother,Father):
    pass
Buu=child()
Buu.skill()
print(child.mro())