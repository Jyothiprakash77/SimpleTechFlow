L=list(map(int,input().split()))
n=len(L)
for i in range(n-1):
    for j in range(0,n-i-1):
        if L[j]>L[j+1]:
            L[j+1],L[j]=L[j],L[j+1]
print(L)