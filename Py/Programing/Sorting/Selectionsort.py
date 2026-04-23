L=list(map(int,input().split()))
n=len(L)
for i in range(n-1):
    SE=i
    for j in range(i+1,n):
        if L[j]<L[SE]:
            SE=j
    L[i],L[SE]=L[SE],L[i]
for i in L:
    print(i,end=" ")