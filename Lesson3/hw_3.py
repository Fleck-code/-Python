"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    max = a + b
    if a + c > max:
        max = a + c
    if b + c > max:
        max = b + c
    print(max)


my_func(1, 2, 3)
