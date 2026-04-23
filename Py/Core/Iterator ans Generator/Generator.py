def num(n):
    for i in range(1,n):
        yield i
it=num(9)
print(next(it))
print(next(it))
print(next(it))