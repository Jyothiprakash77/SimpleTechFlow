# 3.Implement an iterator that iterates over a string character by character in
# reverse order.
class reverseString:
    def __init__(self,string):
        self.string=string
        self.count=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count>len(self.string):
            raise StopIteration
        point=self.count
        self.count+=1
        return self.string[len(self.string)-point]
stringObj=reverseString("Svrange")
for i in stringObj:
    print(i,end=" ")