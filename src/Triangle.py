from src.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.name = "triangle"

        if (self.side1 + self.side2 <= self.side3) or (self.side1 + self.side3 <= self.side2) or \
                (self.side2 + self.side3 <= self.side1):
            raise ValueError('Невозможно создать треугольник с такими сторонами: сумма двух сторон должна превышать '
                             'значение третьей стороны')

    def area(self):
        hp = self.perimeter() / 2
        return math.sqrt(hp * (hp - self.side1) * (hp - self.side2) * (hp - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def add_area(self, figure):
        return self.area() + figure.area()
