# 6.Create a generator that yields cumulative sum of numbers in a list. Example:
# [1,2,3] → 1, 3, 6
def cumSum(*num,p=0):
    sum=0
    n=p
    if p>len(num):
        raise StopIteration
    while True:
        if n<0:
            break
        sum+=list(num)[n]
        n-=1
    yield sum
    p+=1
it=cumSum(1,2,3,4,5)
print(next(it))
print(next(it))
