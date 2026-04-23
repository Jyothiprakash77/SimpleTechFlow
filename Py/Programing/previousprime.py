n=int(input())
def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
prev=n-1
while prev>0:
    if is_prime(prev):
        print(prev)
        break
    prev-=1