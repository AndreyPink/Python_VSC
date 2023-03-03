# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
length_list = int(input('Input length of list: '))
my_range = [int(input(f'Input {i+1} border of range: ')) for i in range(2)]
my_list = [random.randint(-10, 20) for elem in range(length_list)]
index_list = [index for index in range(length_list) if (my_list[index] >= my_range[0] and my_list[index] <= my_range[1])]
print(f'My list: {my_list}')
print(f'Index list: {index_list}')



