# Q3. Create a Vector class that supports:
# • + operator → add coordinates
# • == operator → compare equality
# Show how operator overloading gives natural polymorphism to user-defined classes.
class Vector:
    def __init__(self,x1,y1):
        self.x=x1
        self.y=y1
    def __add__(self,obj):#see posibility of three parameters
        return Vector(self.x+obj.x,self.y+obj.y)
#print(V1+V2+V3)#One "+" operator with different functionality when use with different objects
#      ~~~~~^~~
#TypeError: can only concatenate tuple (not "Vector") to tuple
    def __eq__(self,obj):
        return (self.x==obj.x) and (self.y==obj.y)
    def __str__(self):
        return f"({self.x} {self.y})"
V1=Vector(2,9)
V2=Vector(4,9)
V3=Vector(2,9)
print(V1+V2+V3)#One "+" operator with different functionality when use with different objects
print(V1==V3)
print(V1==V2)#"==" same equals to but with different behaviour when use on different items
print(V1)