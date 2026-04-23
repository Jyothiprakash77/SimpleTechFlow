# • Create class A with method show(). Create class B(A) that overrides show() and
# also calls the parent method using super().
class Mahabharat:
    def show(self):
        print("The Mahabharata is a vast epic that narrates the struggle for sovereignty between the Kauravas \n"
                "and the Pandavas, two cousins who are descendants of the Kuru dynasty. The epic is divided into \n"
                "18 parvan s, or sections, and is known for its complex structure and rich narrative. It is not only \n"
                "a historical account but also a philosophical treatise that explores themes of duty, morality, and destiny. \n"
                "The Mahabharata is considered one of the most important texts of ancient Indian literature and continues to \n"
                "influence Hinduism and world literature. \n")
class BhagavathGita(Mahabharat):
    def show(self):
        super().show()
        print("The Bhagavad Gita is a 700-verse dialogue between Lord Krishna and Arjuna, set in the Mahabharata. It serves \n"
                "as a philosophical guide, addressing themes such as dharma (duty), karma (action), and devotion (bhakti). \n"
                "The dialogue unfolds during a critical moment in the Kurukshetra War, where Arjuna hesitates to fight against \n"
                "his own kin. Krishna, as his charioteer, teaches him the importance of duty, self-knowledge, and the path to \n"
                "spiritual liberation. The Gita is revered for its profound insights into life, duty, and the nature of existence, \n"
                "making it a timeless classic in Hindu philosophy and spirituality.\n")

B1=BhagavathGita()
B1.show()
