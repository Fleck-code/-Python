"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    number = input('введите целое положительное число: ')
    if number.isdigit():
        break
i = len(number)
res = number[0]
while i > 0:
    if int(number[i - 1]) > int(res):
        res = number[i - 1]
    i -= 1
print(f'самая большая цифра в числе {number}: ', res)
