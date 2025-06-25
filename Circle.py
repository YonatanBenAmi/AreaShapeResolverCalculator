import math
from Shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        if not Shape.checking(self.radius):
            raise TypeError("Error! Invalid value or type")

    def __str__(self):
        return f"The radius is {self.radius} meters."

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
