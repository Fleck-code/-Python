# coding=utf8
"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'Программа'

    def draw(self):
        print('Запуск отрисовки:')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(self.title, 'в деле!')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(self.title, 'в деле!')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print(self.title, 'в деле!')


Stationery_1 = Stationery()
Pen_1 = Pen()
Pencil_1 = Pencil()
Handle_1 = Handle()
Stationery_1.draw()
Pen_1.draw()
Handle_1.draw()
Pencil_1.draw()
