# coding=utf8
"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.is_police:
            print('полицейская машина', self.name, self.color, 'выехала')
        else:
            print(self.name, self.color, 'поехала')

    def stop(self):
        print(self.name, self.color, 'остановилась')

    def turn(self, way):
        self.way = way
        print(self.name, self.color, 'повернула', way)

    def show_speed(self, speed):
        self.speed = speed
        print('Скорость автомобиля:', self.name, self.color, speed, 'км/ч')


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self, speed):
        self.speed = speed
        print('Скорость автомобиля:', self.name, self.color, speed, 'км/ч')
        if self.speed > 60:
            print(self.name, self.color, 'TownCar - превышение скорости!', speed, 'км/ч при разрешенной 60 км/ч')


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.color = color

    def show_speed(self, speed):
        self.speed = speed
        print('Скорость автомобиля:', self.name, self.color, speed, 'км/ч')
        if self.speed > 40:
            print(self.name, self.color, 'WorkCar - превышение скорости!', speed, 'км/ч при разрешенной 40 км/ч')


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


Police = PoliceCar('lada', 'blue')
Sport = SportCar('ferrari', 'yellow')
Work = WorkCar('gaz', 'white')
Town = TownCar('kia', 'black')
Sport.go()
Sport.show_speed(140)
Work.go()
Work.turn('налево')
Work.show_speed(90)
Police.go()
Police.stop()
Work.stop()
Town.go()
Town.turn('направо')
Town.show_speed(60)
Town.stop()
