# 10. Implement a generator that yields running maximum from a list Example:
# [3,1,4,2] → 3, 3, 4, 4
def runningMaxium(*n):
    max=0
    list1=list(n)
    for i in list1:
        max= max if max>i else i
        yield max
for i in runningMaxium(1,7,9,4,3):
    print(i,end=" ")