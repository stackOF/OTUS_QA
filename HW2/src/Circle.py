from HW2.src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.name = "circle"

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self):
        return 2 * math.pi * self.radius
