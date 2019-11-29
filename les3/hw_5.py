"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

list = list()
end = True  # проверка на контрольный символ завершения программы
summa = 0


def func_sum(*args):
    global summa
    for itm in args:
        itm = int(itm)
        summa += itm
    return summa


while end:
    next_add = input('введите числа через пробел\n Чтобы закончить программу, введите "!"')
    if next_add in '!':  # если пользователь ввел !
        print('итоговая сумма: ', summa)
        end = False
    elif len(next_add.split('!')) > 1:  # если пользователь ввел числа и !
        last_str = next_add.split('!')
        list = last_str[0].split(' ')
        func_sum(*list)
        print('итоговая сумма: ', summa)
        end = False
    elif len(next_add.split(' ')) == 0:  # если пользователь ввел одно число и все
        list.append(next_add)
        func_sum(*list)
        print('Ваша промежуточная сумма: ', summa)
    else:  # все остальные случаи
        list = next_add.split(' ')
        try:  # проверка числа ли ввел пользователь
            for itm in list:
                itm = int(itm)
        except ValueError as e:
            print('ошибка ввода')
            continue
        func_sum(*list)
        print('Ваша промежуточная сумма: ', summa)
    list.clear()
