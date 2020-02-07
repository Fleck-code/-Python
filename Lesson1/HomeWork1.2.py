"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

while True:
    secs = input('Введите время в секундах: ')
    if secs.isdigit():
        break
secs = int(secs)
minutes = int(secs / 60)
hours = int(minutes / 60)
sec_result = secs - minutes * 60
mins_result = minutes - hours * 60
print(f'{hours}:{mins_result}:{sec_result}')
