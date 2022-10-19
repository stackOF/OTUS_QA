from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        self.side = side
        self.name = "square"

    @property
    def area(self):
        return self.side**2

    @property
    def perimeter(self):
        return self.side*4
