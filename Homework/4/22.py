# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random
length_list_1 = int(input('Input length 1 list: '))
length_list_2 = int(input('Input length 2 list: '))
list_1 = [random.randint(1,20) for _ in range(length_list_1)]
list_2 = [random.randint(1,20) for _ in range(length_list_2)]
print(f'First list: {list_1}')
print(f'Second list: {list_2}')
print(f'Intersection list: {sorted(set(list_1).intersection(set(list_2)))}')











# a = set([1])
# print(a)
# a.add(3)
# print(a)


# list_1 = (random.randint(1,20) for _ in range(10))
# for i in list_1:
#     print(i, end=' ')
# print()
# print(type(list_1))

# list_1 = [random.randint(1,20) for _ in range(10)]
# print(list_1)
# print(type(list_1))
