from Shape import Shape

class Hexagon(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return 6 * (((self.side ** 2) * (3 ** 0.5)) / 4)
