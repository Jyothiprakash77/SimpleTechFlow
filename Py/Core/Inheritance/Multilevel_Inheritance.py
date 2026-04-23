# Brahma – The creator of the universe.
# Marichi – One of Brahma’s mind-born sons.
# Kashyapa – A great sage and one of Marichi’s descendants.
# Vivasvan (Surya) – The Sun God, son of Kashyapa.
# Vaivasvata Manu – The progenitor of mankind, son of Surya.
# Ikshvaku – Founder of the Ikshvaku dynasty and the first king of Ayodhya.
class Ikshvaku:
    def about(self):
        print("The founder of the Ikshvaku dynasty and the first king of Ayodhya.")
class Dasaratha(Ikshvaku):
    def Ancistor(self):
        print("Ikshvaku- ",end="")
        super().about()
    def about(self):
        print("The mighty ruler of Ayodhya, known for his valor and wisdom. ")
class ShriRama(Dasaratha):
    def Ancistors(self):
        super().Ancistor()
        print("                             |")
        print("Dasaratha- ",end="")
        super().about()
    def about(self):
        print("Mighty greatest king the ever lived One women man,Father word follower,love everybody equally"
              "\nTreat everybody equally,the mightest warrior ever lived,the humble human ever lived")
lord_Rama=ShriRama()
lord_Rama.about()
lord_Rama.Ancistors()
print(ShriRama.mro())