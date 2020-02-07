"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def func(var1, var2):
    if var2 == 0:
        var3 = 'делить на ноль нельзя'
    else:
        var3 = var1 // var2
    return var3


while True:
    a = input('введите первую переменную\n')
    b = input('введите вторую переменную\n')
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        break
    else:
        print('надо вводить числа')

result = func(a, b)
print(f'{a} / {b} = ', result)
