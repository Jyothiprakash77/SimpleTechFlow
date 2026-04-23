class Math:
    def __init__(self,name):
        self.name=name
    def __add__(self,list):
        # l + differentiation
        # ~ ^ ~~~~~~~~~~~~~~~
        # TypeError: can only concatenate list(not "Math") to list
        list.append(self.name)
    # def __radd__(self,list):
    #     #it changes l+obj=>obj+l
    #     list.append(self.name)

differentiation=Math("differentiation")
Trignometry=Math("Trignometry")
Matrix=Math("Matrix")
l=[]
l+differentiation
l+Trignometry
l+Matrix
print(l)