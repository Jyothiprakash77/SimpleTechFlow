s = abs(int(input()))
e = abs(int(input()))
if s > e:
    s, e = e, s


def is_Armstrong(n):
    temp = n
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    temp = n
    arm = 0
    while temp > 0:
        r = temp % 10
        arm += (r ** count)
        temp //= 10
    return arm == n


if s != 0 and e != 0:
    sum = 0
    Scount = 0
    count = 0
    Avg = 0
    U = False
    for i in range(s, e + 1):
        if is_Armstrong(i):
            Scount += 1
            if Scount % 2 == 1:
                count += 1
                U = True
                if count == 1:
                    print("Average of Alternative Armstrong Numbers in the Given Range is ( ", end="")
                if count != 1:
                    print(" + ", end="")
                print(i, end="")
                sum += i
    if U:
        Avg = sum / count
        print(f" ) / {count} = {Avg:.2f}")
    else:
        print("No Armstrong Numbers in a Given Range")
else:
    print("Invalid Inputs.")
