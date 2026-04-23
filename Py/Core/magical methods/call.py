class RVR:
    def __init__(self,x,y):
        self.c=x
        self.s=y
    def __call__(self):
        return self.c+self.s
vkr=RVR(4,9)
print(vkr())