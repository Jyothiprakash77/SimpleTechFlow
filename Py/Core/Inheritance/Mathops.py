#*  Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.
class MathOps:
    @staticmethod
    def add(a,b):
        return a+b
class AdvancedOps(MathOps):
    def A(self):
        super().add(1,2)
Diff=AdvancedOps()
print(Diff.add(9,10))
print(Diff.A())
