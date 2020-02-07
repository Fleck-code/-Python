"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

f_count = 0
word_count = 0
with open('txt_2.txt') as f:
    for id, line in enumerate(f):
        f_count += 1
        for word in line.split():
            word_count += 1
        print(f'в {id + 1} строке:', word_count, 'слов')
        word_count = 0
    print('число строк: ', f_count)
