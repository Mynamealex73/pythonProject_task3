'''(МОДУЛЬ 1) Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]'''

numbers_list = []
numb = int(input('Enter how many numbers of elements:'))

for i in range(numb):
    number = int(input('Enter number №' + str(i + 1) + ': '))
    numbers_list.append(number)

# print(numbers_list)
numbers_list.sort()
print(numbers_list)