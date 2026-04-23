class potential_Energy:
    def __init__(self,m,g,h):
        self.M=m
        self.G=g
        self.H=h
    def __call__(self):
        return self.M*self.G*self.H
    def __contains__(self,G):
        return self.G==G
    
P1=potential_Energy(90,89,9)
P1E=P1()
print(P1E)
print(90 in P1)