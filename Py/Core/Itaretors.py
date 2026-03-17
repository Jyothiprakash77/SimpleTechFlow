class Prime:
    def __init__(self,n):
        self.num=n
        self.count=0
        self.prime=0
    @staticmethod
    def is_prime(n):
        fc=0
        for i in range(1,n+1):
            if n%i==0:
                fc+=1
        return fc==2
    def __iter__(self):
        return self
    def __next__(self):
        self.count+=1
        if self.count>self.num:
            raise StopIteration
        else:
            while True:
                self.prime+=1
                if self.is_prime(self.prime):
                    return self.prime
def p(n):
    prime1 = Prime(n)
    for i in prime1:
        yield i
prime2=Prime(10)
print(next(prime2))
print(next(prime2))