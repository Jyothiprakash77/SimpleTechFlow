class A:
    def display(self):
        print("class A")
class B(A):
    def display(self):
        print("class B")
        super().display()
class C(B):
    def display(self):
        print("class C")
        super().display()
c1=C()
c1.display()