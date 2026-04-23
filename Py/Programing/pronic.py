# A Pronic number (also known as a Heteromecic number, oblong number, or rectangular number) is a number
# that is the product of two consecutive integers.
#
# In simple terms, if you can take a number and write it as n×(n+1), it is a Pronic number. These are called "rectangular"
# because they can be arranged in a grid that is exactly one unit longer than it is wide.
n=int(input())
a=1
while True:
    c=a*(a+1)
    if c>=n:
        if c>n:
            print(f"{n} is Not a pronic number")
            break
        else:
            print(f"{n} is a Pronic number")
            break
    a+=1