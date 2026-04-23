#9. Write an iterator that returns characters at even indices of a string.
class Even_string:
    def __init__(self):
        self.count=0
    def __call__(self,string):
        self.string=string
        return self
    def __iter__(self):
        return self
    def __next__(self):
        if self.count>=len(self.string):
            raise StopIteration
        if self.count%2==0:
            c=self.count
            self.count+=1
            return self.string[c]
        self.count+=1
S1=Even_string()
for i in S1("iterator"):
    print(i,end=" ")

