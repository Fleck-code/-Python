"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random

sum = 0
with open('txt_5.txt', 'w') as f:
    a = [random.randint(1, 100) for _ in range(20)]
    f.writelines(' '.join(map(str, a)))
    for i in a:
        sum = sum + int(i)
    print('сумма чисел:', sum)
