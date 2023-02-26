# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
length_mass = int(input('Input length of mass: '))
my_number = int(input('Input number for search: '))
random_mass = [random.randint(1,10) for _ in range(length_mass)]
print(f'Random mass: {random_mass}')
print(f'Number of "{my_number}" in mass = {random_mass.count(my_number)}')

