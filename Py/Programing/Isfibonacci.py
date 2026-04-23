def isFibonacii(n):
    a=0
    b=1
    while a<=n:
        if n==a:
            return True
        c=a+b
        a=b
        b=c
    return False
print(isFibonacii(5))