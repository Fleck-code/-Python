"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

import random

randlist = [random.randint(1, 10) for _ in range(10)]
# print(randlist)
result = list()
max = randlist[0]
for el in randlist:
    if el > max:
        result.append(el)
print(result)
