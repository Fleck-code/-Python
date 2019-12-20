"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Sklad():
    def __init__(self, name):
        self.name = name


class Orgtechnic(Sklad):
    def __init__(self, name, model, count):
        super().__init__(name)
        self.model = model
        self.count = count
        self.my_table = {
            'name': self.name,
            'model': self.model,
            'count': self.count
        }
        self.own_name = {}
        while True:
            try:
                self.my_table['count'] = int(count)
            except ValueError:
                print('количество оргтехники должно быть числовым!')
                self.my_table['count'] = input(f'введите количество техники {name}: ')
            else:
                break

    def __str__(self):
        return str(self.my_table)

    def to_take_own(self, counts, subj):
        self.own_name.update(self.my_table)
        self.own_name['count'] = counts
        self.own_name['owner'] = subj


printers = Orgtechnic('принтер', 'brother', 3)
scaners = Orgtechnic('сканер', 'cannon', 5)
kseroks = Orgtechnic('ксерокс', 'ecosys', '4')
printers.to_take_own(1, 'AD')
print(scaners, printers, kseroks)

print(printers.own_name)

#  не успеваю доделать вовремя. Доделаю чуть позже
