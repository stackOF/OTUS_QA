from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.name = "rectangle"

    def area(self):
        return self.side1*self.side2

    def perimeter(self):
        return 2*(self.side1+self.side2)

    def add_area(self, figure):
        return self.area() + figure.area()
