"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

import itertools
import sys

for i in itertools.count(int(sys.argv[1])):
    print(i)
    if i > int(sys.argv[1]) + 100:
        break
x = [1, 2, 3]
for i in itertools.cycle(x):
    print(i)
