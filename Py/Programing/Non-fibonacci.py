def Non_Fibonacci(i):
    a = 0
    b = 1
    while True:
        c=a+b
        if a>=i:
            if a==i:
                return False
            else:
                return True
        a=b
        b=c
for i in range(1,190):
    if Non_Fibonacci(i):
        print(i)
print("-------------------------------------------")
for i in range(1,10):
    if Non_Fibonacci(i):
        print(i)
