from Rectangle import Rectangle
from Shape import Shape

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"The length of the side is {self.side1} meters."


