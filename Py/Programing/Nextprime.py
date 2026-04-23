n=int(input())
def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
next=n
while True:
    next+=1
    if is_prime(next):
        print(next)
        break