# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

# первый этап
import random
my_list_1 = [random.randint(1000, 9999) for _ in range(5)]
my_list_2 = []
my_list_3 = []
num = input('Input number: ')

# второй этап
for value in my_list_1:
    if num in str(value):
        value = str(value).replace(num, '')
    my_list_2.append(value)

# третий этап
for value in my_list_2:
    while int(value) > 9:
        value = sum(int(elem) for elem in str(value))
    my_list_3.append(value)

# четвертый этап
my_list_4 = set(my_list_3)

print(my_list_1)
print(my_list_2)
print(my_list_3)
print(my_list_4)