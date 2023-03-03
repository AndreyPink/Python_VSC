# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод:
# 3 3 2 12

from random import randint
list_1 = [randint(1,20) for _ in range(int(input('Input length 1 mass: ')))]
list_2 = [randint(1,20) for _ in range(int(input('Input length 2 mass: ')))]
print(f'Mass_1: {list_1}\nMass_2: {list_2}')
print(f'New mass: {[elem for elem in list_1 if elem not in list_2]}')