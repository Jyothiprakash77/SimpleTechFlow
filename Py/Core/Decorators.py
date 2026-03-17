#Decoretors
def extra_feature(mul):
    def wrapper(*args,**kwargs):
        print("Multiplication is getting executed")
        print(mul(*args,**kwargs))
        print("Multiplication is done")
    return wrapper
@extra_feature
def mul(a,b):
    return a*b
#mul=extra_feature(mul)
def reverse(sqr):
    def wrapper(x):
        n = sqr(x)
        print(f"{n} and it's reversal is {str(n)[::-1]} ")
    return wrapper
@reverse
def square(x):
    return x**2
square(56)