# coding=utf8
"""
2. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    dohod = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.dohod['wage'] = wage
        self.dohod['bonus'] = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self._income = self.dohod['wage'] + self.dohod['bonus']

    def get_full_name(self):
        print('Сотрудник', self.name, self.surname, self.position)

    def get_total_income(self):
        print('Доход сотрудника:', self._income)


worker_1 = Position('Иван', 'Иванов', 'монтажник', 35000, 10000)
worker_2 = Position('Петр', 'Петров', 'Директор', 100000, 50000)
worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()
