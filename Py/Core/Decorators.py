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
mul(3,5)