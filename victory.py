'''(МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ,
но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова'''

'''data = '09.03.2009'
day, month, year = data.split('.')
print(days[day], months[month], year, 'года')'''

import random
famous_persons = ['king', 'winston', 'gevara', 'chaplin', 'gagarin', 'pyshkin', 'einstein', 'tesla', 'tolstoi',
                  'mandela']
result = random.sample(famous_persons, 5)
print(result)

months = {
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '11': 'ноября'
}

days = {
    '09': 'девятое',
    '10': 'десятое',
    '14': 'четырнадцатое',
    '16': 'шестнадцатое',
    '18': 'восемнадцатое',
    '21': 'двацать первое',
    '26': 'двацать шестое',
    '28': 'двацать восьмое',
    '30': 'тридцатое'
}


sum_a = 0
sum_b = 0
answer = None

while answer !='нет':
    for i in result:
        if i == 'king':
            king_born = input("Введите дату рождения Стивина Кинга в формате 'dd.mm.yyyy': ")
            if king_born == '21.09.1947':
                sum_a += 1
            else:
                sum_b += 1
                data = '21.09.1947'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'winston':
            winston_born = input("Введите дату рождения Уинстона Черчеля в формате 'dd.mm.yyyy': ")
            if winston_born == '30.11.1847':
                sum_a += 1
            else:
                sum_b += 1
                data = '30.11.1847'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'gevara':
            gevara_born = input("Введите дату рождения Че Гевары в формате 'dd.mm.yyyy': ")
            if gevara_born == '14.06.1928':
                sum_a += 1
            else:
                sum_b += 1
                data = '14.06.1928'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'chaplin':
            chaplin_born = input("Введите дату рождения Чарли Чаплина в формате 'dd.mm.yyyy': ")
            if chaplin_born == '16.04.1889':
                sum_a += 1
            else:
                sum_b += 1
                data = '16.04.1889'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'gagarin':
            gagarin_born = input("Введите дату рождения Ю.А. Гагарина в формате 'dd.mm.yyyy': ")
            if gagarin_born == '09.03.1934':
                sum_a += 1
            else:
                sum_b += 1
                data = '09.03.1934'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'pyshkin':
            pyshkin_born = input("Введите дату рождения А.С. Пушкина в формате 'dd.mm.yyyy': ")
            if pyshkin_born == '26.05.1799':
                sum_a += 1
            else:
                sum_b += 1
                data = '26.05.1799'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'einstein':
            einstein_born = input("Введите дату рождения Альберта Эйштейна в формате 'dd.mm.yyyy': ")
            if einstein_born == '14.03.1879':
                sum_a += 1
            else:
                sum_b += 1
                data = '14.03.1879'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'tesla':
            tesla_born = input("Введите дату рождения Николы Тесла в формате 'dd.mm.yyyy': ")
            if tesla_born == '10.07.1856':
                sum_a += 1
            else:
                sum_b += 1
                data = '10.07.1856'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'tolstoi':
            tolstoi_born = input("Введите дату рождения Л.Н. Толстого в формате 'dd.mm.yyyy': ")
            if tolstoi_born == '28.08.1828':
                sum_a += 1
            else:
                sum_b += 1
                data = '28.08.1828'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')
        elif i == 'mandela':
            mandela_born = input("Введите дату рождения Нельсана Манделы в формате 'dd.mm.yyyy': ")
            if mandela_born == '18.07.1918':
                sum_a += 1
            else:
                sum_b += 1
                data = '18.07.1918'
                day, month, year = data.split('.')
                print('Правильная дата рождения - ', days[day], months[month], year, 'года')

    proc_a = (sum_a * 100) / 5
    proc_b = (sum_b * 100) / 5

    print('Колличество правильных ответов: ', sum_a)
    print('Колличество неправильных ответов: ', sum_b)
    print('Процент правильных ответов: ', proc_a, '%')
    print('Процент неправильных ответов: ', proc_b, '%')

    answer = input('Хотите начать игру сначала (да/нет)?: ')



