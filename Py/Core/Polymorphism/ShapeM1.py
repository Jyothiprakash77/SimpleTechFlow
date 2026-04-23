# Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
# Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?
class Circle:
    def draw(self):
        radius = 5  # Fixed radius (no user input)
        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):
                # Equation of a circle: x² + y² ≈ r²
                if abs(x ** 2 + y ** 2 - radius ** 2) < radius:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
class Square:
    def draw(self):
        for i in range(5):
            for j in range(5):
                print("* ",end="")
            print()
class Rectangle:
    def draw(self):
        for i in range(5):
            for j in range(7):
                print("* ", end="")
            print()
class Car:
    def draw(self):
        print("Car Car Car Car Car")
l=[Circle(),Square(),Rectangle(),Car()]
for i in l:
    i.draw()
    print()