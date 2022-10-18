from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.name = "circle"

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def add_area(self, figure):
        return self.area() + figure.area()
