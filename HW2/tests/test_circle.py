from HW2.src.Circle import Circle
from HW2.src.Square import Square
from HW2.src.Rectangle import Rectangle
from HW2.src.Triangle import Triangle
import pytest
from random import randrange
import math


@pytest.mark.parametrize('rad', [2, 4.04])
def test_circle(rad):
    circle = Circle(rad)
    circle.is_correct_name_figure('circle', circle)
    circle.is_number_value(rad)
    circle.no_invalid_values(rad)


@pytest.mark.parametrize('rad', [0, 5, 3.67])
def test_circumference(rad):
    circle = Circle(rad)
    assert circle.circumference == 2 * math.pi * rad, "Неверный расчет длины окружности"


@pytest.mark.parametrize('rad', [0, 5, 3.67])
def test_area(rad):
    circle = Circle(rad)
    assert circle.area == math.pi * (rad ** 2), "Неверный расчет площади круга"


@pytest.mark.parametrize('add_figure', ['triangle', 'rectangle', 'square'])
def test_add_area(add_figure):
    circle = Circle(randrange(1, 10))
    if add_figure == 'triangle':
        figure = Triangle(3, 4, 5)
        result = circle.add_area(figure)
    elif add_figure == 'rectangle':
        figure = Rectangle(2, 4)
        result = circle.add_area(figure)
    elif add_figure == 'square':
        figure = Square(4)
        result = circle.add_area(figure)
    else:
        raise ValueError("На сложение площадей передана некорректная геометрическая фигура")
    assert result == circle.area + figure.area, "Неверный расчет суммы площадей фигур"


@pytest.mark.xfail(reason="negative tests")
@pytest.mark.parametrize('rad', [-2, 'rad13', '^&'])
def test_create_circle_negative(rad):
    circle = Circle(rad)
    circle.is_number_value(rad)
    circle.no_invalid_values(rad)
