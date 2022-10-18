from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        self.side = side
        self.name = "square"

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4

    def add_area(self, figure):
        return self.area() + figure.area()
