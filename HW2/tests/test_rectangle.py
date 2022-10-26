from HW2.src.Circle import Circle
from HW2.src.Square import Square
from HW2.src.Rectangle import Rectangle
from HW2.src.Triangle import Triangle
import pytest


@pytest.mark.parametrize('a,b', [(3, 4), (3.04, 4.99)])
def test_rectangle(a, b):
    rectangle = Rectangle(a, b)
    rectangle.is_correct_name_figure('rectangle', rectangle)
    rectangle.is_number_value(a, b)
    rectangle.no_invalid_values(a, b)


@pytest.mark.parametrize('a,b', [(3, 4), (3.04, 4.99)])
def test_perimeter(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.perimeter == 2 * (a + b), "Неверный расчет периметра четырехугольника"


@pytest.mark.parametrize('a,b', [(3, 4), (3.04, 4.99)])
def test_area(a, b):
    rectangle = Rectangle(a, b)
    assert rectangle.area == a * b, "Неверный расчет площади четырехугольника"


@pytest.mark.parametrize('add_figure', ['circle', 'triangle', 'square'])
def test_add_area(add_figure):
    rectangle = Rectangle(3, 4)
    if add_figure == 'circle':
        figure = Circle(5)
        result = rectangle.add_area(figure)
    elif add_figure == 'triangle':
        figure = Triangle(3, 4, 5)
        result = rectangle.add_area(figure)
    elif add_figure == 'square':
        figure = Square(4)
        result = rectangle.add_area(figure)
    else:
        raise ValueError("На сложение площадей передана некорректная геометрическая фигура")
    assert result == (rectangle.area + figure.area), "Неверный расчет суммы площадей фигур"


@pytest.mark.xfail(reason="negative tests")
@pytest.mark.parametrize('a,b', [('f', 4), (3.04, -4.99), (4.99, 0)])
def test_create_rectangle_negative(a, b):
    rectangle = Rectangle(a, b)
    rectangle.is_number_value(a, b)
    rectangle.no_invalid_values(a, b)

