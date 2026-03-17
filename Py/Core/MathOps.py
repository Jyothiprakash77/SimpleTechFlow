class MathOps:
    @staticmethod
    def is_even(num):
        return bool(num%2)
math=MathOps()
print(math.is_even(79))