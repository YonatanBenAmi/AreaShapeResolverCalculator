from Shape import Shape

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    def area(self):
        return self.side1 * self.side2
