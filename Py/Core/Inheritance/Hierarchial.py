# • Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.
class Mahabharat:
    @classmethod
    def display(cls):
        print("Mahabharata")
class BhagavathGita(Mahabharat):
    @classmethod
    def display(cls):
        print("BhagavathGita")
        super().display()
class IntroductionToGita(BhagavathGita):
    @classmethod
    def display(cls):
        print("Summary to BhagawatGita")
        super().display()
G1=IntroductionToGita()
G1.display()
