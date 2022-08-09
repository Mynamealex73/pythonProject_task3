'''(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно'''

enter_numbers = input("Enter numbers using ',' in 1st list: ")

numbers = enter_numbers.split(",")

enter_numbers = input("Enter numbers using ',' in 2nd list: ")

second_numbers = enter_numbers.split(",")

print(numbers)
print(second_numbers)
# копия списка

for number in numbers[:]:
    if number in second_numbers:
        numbers.remove(number)

print(numbers)
