import numbers


class Figure:
    def __init__(self, name):
        self.name = name

    def no_invalid_values(self, *args):
        for i in args:
            assert i > 0, 'Сторона/радиус фигуры не может быть меньше или равно нулю'

    def is_number_value(self, *args):
        for i in args:
            assert isinstance(i, numbers.Number), 'Сторона/радиус фигуры должно быть только числом'

    def is_correct_name_figure(self, name, figure):
        assert figure.name == name, 'Название фигуры некорректное/не задано'
