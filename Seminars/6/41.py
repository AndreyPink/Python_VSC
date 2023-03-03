# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод:      Ввод:
# 5          5
# 1 2 3 4 5  1 5 1 5 1
# Вывод:     Вывод:
# 0          2

from random import randint
my_list = [randint(1,9) for _ in range(int(input('Input length mass: ')))]
print(f'List: {my_list}')
print(f'Count = {len([i for i in range(1, len(my_list)-1) if (my_list[i+1] < my_list[i] > my_list[i-1])])}')
