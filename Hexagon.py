import math
from Shape import Shape

class Hexagon(Shape):
    def __init__(self, side):
        self.side = side
        if not Shape.checking(self.side):
            raise TypeError("Error! Invalid value or type")

    def __str__(self):
        return f"The length of the side is {self.side} meters."

    def area(self):
        return 6 * ((self.side ** 2) * (math.sqrt(3) / 4))

    def perimeter(self):
        return 6 * self.side
