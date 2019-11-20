"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

while True:
    viruchka = input('выручка фирмы: ')
    izderzhki = input('издержки фирмы: ')
    if viruchka.isdigit() and izderzhki.isdigit():
        break
    print('введите численные значения')
viruchka = int(viruchka)
izderzhki = int(izderzhki)
pribil = viruchka - izderzhki
if viruchka > izderzhki:
    print('фирма работает в прибыль!')
    print('Рентабельность выручки: ', pribil / viruchka)
    while True:
        pers_count = input('введите количество сотрудников: ')
        if pers_count.isdigit():
            break
    pers_count = int(pers_count)
    print('прибыль фирмы в расчете на одного сотрудника: ', pribil / pers_count)
else:
    print('фирма работает в убыток!')
