# • Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class.
class University:
    Name="Shri Varalakshmi University"
    @classmethod
    def Admission(cls):
        print("You got admission")
class College(University):
    pass
C1=College()
C1.Admission()
print(C1.Name)