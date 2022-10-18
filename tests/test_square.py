from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle
import pytest
from random import randrange


@pytest.mark.parametrize('a', [2, 4.04])
def test_square(a):
    square = Square(a)
    square.is_correct_name_figure('square', square)
    square.is_number_value(a)
    square.no_invalid_values(a)


@pytest.mark.parametrize('a', [0, 5, 3.67])
def test_perimeter(a):
    square = Square(a)
    assert square.perimeter() == 4 * a, "Неверный расчет периметра квадрата"


@pytest.mark.parametrize('a', [0, 5, 3.67])
def test_area(a):
    square = Square(a)
    assert square.area() == a ** 2, "Неверный расчет площади квадрата"


@pytest.mark.parametrize('add_figure', ['triangle', 'rectangle', 'circle'])
def test_add_area(add_figure):
    square = Square(randrange(1, 10))
    if add_figure == 'triangle':
        figure = Triangle(3, 4, 5)
        result = square.add_area(figure)
    elif add_figure == 'rectangle':
        figure = Rectangle(2, 4)
        result = square.add_area(figure)
    elif add_figure == 'circle':
        figure = Circle(4)
        result = square.add_area(figure)
    else:
        raise ValueError("На сложение площадей передана некорректная геометрическая фигура")
    assert result == (square.area() + figure.area()), "Неверный расчет суммы площадей фигур"


@pytest.mark.xfail(reason="negative tests")
@pytest.mark.parametrize('a', [-2, 's13', '^8'])
def test_create_square_negative(a):
    square = Square(a)
    square.is_number_value(a)
    square.no_invalid_values(a)
