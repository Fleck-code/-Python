# coding=utf8
"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    def __init__(self, _length, _width):
        self._Length = _length
        self._width = _width
        result = _length * _width * 25 * 5 / 1000
        print(f'{_length}м*{_width}м*25кг*5см =', int(result), 'т')


asphalt = Road(20, 5000)
