from HW2.src.Circle import Circle
from HW2.src.Square import Square
from HW2.src.Rectangle import Rectangle
from HW2.src.Triangle import Triangle
import pytest
import math


@pytest.mark.parametrize('a,b,c', [(3, 4, 5), (3.04, 4.99, 7.3)])
def test_triangle(a, b, c):
    triangle = Triangle(a, b, c)
    triangle.is_correct_name_figure('triangle', triangle)
    triangle.is_number_value(a, b, c)
    triangle.no_invalid_values(a, b, c)


@pytest.mark.parametrize('a,b,c', [(3, 4, 5), (3.04, 4.99, 7.3)])
def test_perimeter(a, b, c):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter == (a + b + c), "Неверный расчет периметра треугольника"


@pytest.mark.parametrize('a,b,c', [(3, 4, 5), (3.04, 4.99, 7.3)])
def test_area(a, b, c):
    triangle = Triangle(a, b, c)
    hp = (a+b+c)/2
    assert triangle.area == math.sqrt(hp * (hp - a) * (hp - b) * (hp - c)), "Неверный расчет площади треугольника"


@pytest.mark.parametrize('add_figure', ['circle', 'rectangle', 'square'])
def test_add_area(add_figure):
    triangle = Triangle(3, 4, 5)
    if add_figure == 'circle':
        figure = Circle(5)
        result = triangle.add_area(figure)
    elif add_figure == 'rectangle':
        figure = Rectangle(2, 4)
        result = triangle.add_area(figure)
    elif add_figure == 'square':
        figure = Square(4)
        result = triangle.add_area(figure)
    else:
        raise ValueError("На сложение площадей передана некорректная геометрическая фигура")
    assert result == triangle.area + figure.area, "Неверный расчет суммы площадей фигур"


@pytest.mark.xfail(reason="negative tests")
@pytest.mark.parametrize('a,b,c', [('f', 4, 5), (3.04, -4.99, 7.3), (3.04, 4.99, '.')])
def test_create_triangle_negative(a, b, c):
    triangle = Triangle(a, b, c)
    triangle.is_number_value(a, b, c)
    triangle.no_invalid_values(a, b, c)
