"""
1. Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел
и строк и сохраните в переменные, выведите на экран.
"""

while True:
    param1 = input('Введите число: ')
    param2 = input("Введите еще одно число: ")
    if param1.isdigit() and param2.isdigit():
        break
    print('надо вводить числа')
while True:
    param3 = input("Введите слово: ")
    param4 = input("Введите еще одно слово: ")
    if param3.isalpha() and param3.isalpha():
        break
    print('надо вводить слова')
print(param1, param2, param3, param4)
