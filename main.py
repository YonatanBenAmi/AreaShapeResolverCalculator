from Factories.shape_factory import ShapeFactory

class Main:
    #Circle>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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
            print(f"\033[33mCircle_{i}:\033[0m The area of the circle is \033[32m{circle.area()}\033[0m meters.")
            i += 1

    @staticmethod
    def print_perimeter_circles(circle_list):
        i = 1
        for circle in circle_list:
            print(f"Circle_{i}: {circle.perimeter()}")
            i += 1

    #Square>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @staticmethod
    def create_square_instance(count_instance):
        square_list = list()
        for i in range(count_instance):
            square_list.append(ShapeFactory.create_shape("square"))  # Create square calculate and push to list.
        return square_list

    @staticmethod
    def print_area_squares(square_list):
        i = 1
        for square in square_list:
            print(f"Circle_{i}: {square.area()}")
            i += 1

    @staticmethod
    def print_perimeter_squares(square_list):
        i = 1
        for square in square_list:
            print(f"Circle_{i}: {square.perimeter()}")
            i += 1

    #Rectangle>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @staticmethod
    def create_rectangle_instance(count_instance):
        rectangle_list = list()
        for i in range(count_instance):
            rectangle_list.append(ShapeFactory.create_shape("rectangle"))  # Create rectangle calculate and push to list.
        return rectangle_list

    @staticmethod
    def print_area_rectangles(rectangle_list):
        i = 1
        for rectangle in rectangle_list:
            print(f"Circle_{i}: {rectangle.area()}")
            i += 1

    @staticmethod
    def print_perimeter_rectangles(rectangle_list):
        i = 1
        for rectangle in rectangle_list:
            print(f"Rectangle_{i}: {rectangle.perimeter()}")
            i += 1

    #Triangle>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @staticmethod
    def create_triangle_instance(count_instance):
        triangle_list = list()
        for i in range(count_instance):
            triangle_list.append(
                ShapeFactory.create_shape("triangle"))  # Create triangle calculate and push to list.
        return triangle_list

    @staticmethod
    def print_area_triangle(triangle_list):
        i = 1
        for triangle in triangle_list:
            print(f"Triangle_{i}: {triangle.area()}")
            i += 1

    @staticmethod
    def print_perimeter_triangles(triangle_list):
        i = 1
        for triangle in triangle_list:
            print(f"triangle_{i}: {triangle.perimeter()}")
            i += 1

    #Hexagon>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @staticmethod
    def create_hexagon_instance(count_instance):
        hexagon_list = list()
        for i in range(count_instance):
            hexagon_list.append(ShapeFactory.create_shape("hexagon"))  # Create hexagon calculate and push to list.
        return hexagon_list

    @staticmethod
    def print_area_hexagon(hexagon_list):
        i = 1
        for hexagon in hexagon_list:
            print(f"Hexagon_{i}: {hexagon.area()}")
            i += 1

    @staticmethod
    def print_perimeter_hexagon(triangle_list):
        i = 1
        for triangle in triangle_list:
            print(f"triangle_{i}: {triangle.perimeter()}")
            i += 1

    #<<<<<<<<<<<<<<<<<<<<<<<<<<Details>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @staticmethod
    def circle_details():
        list_circle = Main.create_circles_instance(5)
        print("\033[32m--Area--\033[0m")
        Main.print_area_circles(list_circle)
        print("\033[32m--Perimeter--\033[0m")
        Main.print_perimeter_circles(list_circle)

    @staticmethod
    def square_details():
        list_square = Main.create_square_instance(5)
        print("\033[32m--Area--\033[0m")
        Main.print_area_squares(list_square)
        print("\033[32m--Perimeter--\033[0m")
        Main.print_perimeter_squares(list_square)

    @staticmethod
    def rectangle_details():
        list_rectangle = Main.create_square_instance(5)
        print("\033[32m--Area--\033[0m")
        Main.print_area_squares(list_rectangle)
        print("\033[32m--Perimeter--\033[0m")
        Main.print_perimeter_squares(list_rectangle)

    @staticmethod
    def triangle_details():
        list_triangle = Main.create_square_instance(5)
        print("\033[32m--Area--\033[0m")
        Main.print_area_squares(list_triangle)
        print("\033[32m--Perimeter--\033[0m")
        Main.print_perimeter_squares(list_triangle)

    @staticmethod
    def hexagon_details():
        list_hexagon = Main.create_square_instance(5)
        print("\033[32m--Area--\033[0m")
        Main.print_area_squares(list_hexagon)
        print("\033[32m--Perimeter--\033[0m")
        Main.print_perimeter_squares(list_hexagon)


    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Play >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    @staticmethod
    def play():
        #Circle
        print("\033[34m<<<Circle>>>\033[0m")
        Main.circle_details()

        #Square
        print("\033[34m<<<Square>>>\033[0m")
        Main.square_details()

        #Rectangle
        print("\033[34m<<<Rectangle>>>")
        Main.rectangle_details()

        #Triangle
        print("\033[34m<<<Triangle>>>")
        Main.triangle_details()

        # Hexagon
        print("\033[34m<<<Hexagon>>>")
        Main.hexagon_details()


Main.play()

