from Shape import Shape

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        if not (Shape.checking(self.side1) or Shape.checking(self.side2)):
            raise TypeError("Error! Invalid value or type")

    def __str__(self):
        return f"The length of the side_1 is {self.side1} meters and side_2 is is {self.side2} meters."

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return (2 * self.side1) + (2 * self.side2)