class Shape:
    def area(self):
        pass

    @staticmethod
    def print_area(shape):
        print(shape.area())

    @staticmethod
    def checking(num):
        return (type(num) == int or type(num) == float) and num > 0
