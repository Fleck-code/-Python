"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dic = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
i = 0
new = open('new_txt_4.txt', 'w')
with open('txt_4.txt') as f:
    for line in f:
        a = list(line.split())
        a[0] = dic[a[0]]
        i += 2
        new.writelines(a)
new.close()
