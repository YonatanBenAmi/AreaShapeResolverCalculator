from Rectangle import Rectangle
from Shape import Shape

class Triangle(Rectangle):
    def __init__(self, base, height, side1, side2):
        super().__init__(base, height)
        self.base = base
        self.height =height
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return f"The length of the base is {self.base} meters and the height is {self.height} meters."

    def area(self):
        return 0.5 * (super().area())

    def perimeter(self):
        return self.side1 + self.side2 + self.base
