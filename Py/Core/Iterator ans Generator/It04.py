# 4.Write an iterator that yields elements of a list with their index (don’t use
# enumerate).
def Lin(L):
    l=0
    for i in L:
        yield i,l
        l+=1
L=[90,2,3,9,67,9]
iter=Lin(L)
while True:
    print(next(iter))