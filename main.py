from Factories.shape_factory import ShapeFactory

class Main:

    @staticmethod
    def create_circles_instance(count_instance):
        circles_list = list()
        for i in range(count_instance):
            circles_list.append(ShapeFactory.create_shape("circle")) #Create circle calculate and push to list.
        return circles_list

    @staticmethod
    def print_area_circles(circle_list):
        i = 1
        for circle in circle_list:
            print(f"Circle_{i}: {circle.area()}")
            i += 1

    @staticmethod
    def print_perimeter_circles(circle_list):
        i = 1
        for circle in circle_list:
            print(f"Circle_{i}: {circle.perimeter()}")
            i += 1

    @staticmethod
    def main():
        list_circle = Main.create_circles_instance(5)
        Main.print_area_circles(list_circle)
        Main.print_perimeter_circles(list_circle)

    # s1 = ShapeFactory.create_shape("square") #Create square calculate.
    # print(s1)
    # print(s1.area())
    # print(s1.perimeter())
    # r1 = ShapeFactory.create_shape("rectangle") #Create rectangle calculate.
    # print(r1)
    # print(r1.area())
    # print(r1.perimeter())
    # t1 = ShapeFactory.create_shape("triangle") #Create triangle calculate.
    # print(t1)
    # print(t1.area())
    # print(t1.perimeter())
    # h1 = ShapeFactory.create_shape("hexagon") #Create hexagon calculate.
    # print(h1)
    # print(h1.area())
    # print(h1.perimeter())


Main.main()

