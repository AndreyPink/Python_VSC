# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
import random
list_1 = [random.randint(1,9) for _ in range(10)]
list_2 = [random.randint(1,9) for _ in range(10)]
print(list_1)
print(list_2)
print(*(elem for elem in list_1 if elem not in list_2))


# set_1 = set(['White', 'Black', 'Red'])
# set_2 = set(['Red', 'Green'])
# print(set_1 - set_2)
