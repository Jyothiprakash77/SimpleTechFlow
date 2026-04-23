class kshatriya:
    @classmethod
    def about(cls):
        print("-Warriors, rulers, and administrators tasked with protection, governance, and maintaining law and order.")
class Rama(kshatriya):
    @classmethod
    def about(cls):
        print("-Greatest of all wariors")
        super().about()
class Sita(kshatriya):
    @classmethod
    def about(cls):
        print("-prettest woman in all woman")
        super().about()
class LavaKusa(Sita,Rama):
    @classmethod
    def about(cls):
        print("-Spreaders of rama katha")
        super().about()
LK1=LavaKusa()
LK1.about()