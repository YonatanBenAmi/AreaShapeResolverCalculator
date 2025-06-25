
import random

from Circle import Circle
from Hexagon import Hexagon
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle

rand_num = random.randint(1,10)

class ShapeFactory:


    @staticmethod
    def create_shape(shape):
        match shape:
            case "circle":
                return Circle(random.randint(1,10))
            case "square":
                return Square(random.randint(1,10))
            case "triangle":
                return Triangle(random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
            case "hexagon":
                return Hexagon(random.randint(1,10))
            case "rectangle":
                return Rectangle(random.randint(1,10), random.randint(1,10))
            case _:
                print("The shape name does not exist.")
