n=int(input())
def isprime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc==2
num=2
j=0
while j<n:
    if isprime(num):
        print(num,end=" ")
        j+=1
    num+=1

