"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

while True:
    n = input('Введите число от 1 до 9: ')
    if n.isdigit() and len(n) == 1:
        break
p = n + n
s = n + n + n
result = int(n) + int(p) + int(s)
print(f'{n} + {p} + {s} =', result)
