"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input("Введите первое число: ")
b = input('Введите второе число: ')

try:
    a = int(a)
    b = int(b)
    res = a / b
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("На ноль делить нельзя")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {res}")
