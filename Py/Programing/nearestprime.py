n=int(input())
def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
Ap=0
Bp=0
next=n+1
while True:
    if is_prime(next):
        Ap=next
        break
    next+=1
prev=n-1
while prev>0:
    if is_prime(prev):
        Bp=prev
        break
    prev-=1
Apd=Ap-n
Bpd=n-Bp
if Apd<Bpd:
    print(Ap)
elif Bpd<Apd:
    print(Bp)
else:
    print(Ap,Bp)

