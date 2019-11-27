"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {
    '1': 'зима',
    '2': 'зима',
    '3': 'весна',
    '4': 'весна',
    '5': 'весна',
    '6': 'лето',
    '7': 'лето',
    '8': 'лето',
    '9': 'осень',
    '10': 'осень',
    '11': 'осень',
    '12': 'зима'
}
month = input('введите номер месяца (1-12): ')
if month == '1' or month == '2' or month == '12':
    print(seasons_list[0])
elif month == '3' or month == '4' or month == '5':
    print(seasons_list[1])
elif month == '6' or month == '7' or month == '8':
    print(seasons_list[2])
elif month == '9' or month == '10' or month == '11':
    print(seasons_list[3])
else:
    print('Вы ввели некорректное значение')
    exit()
print(seasons_dict[month])
