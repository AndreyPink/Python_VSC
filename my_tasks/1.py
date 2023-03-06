# Отсортируйте словарь по значению в порядке возрастания и убывания.

# Вариант с использованием двух циклов
import random
my_dict = {i: random.randint(1, 10) for i in range(1, 10)}
sorted_dict_up = {}
for value in sorted(my_dict.values()):
    for key in my_dict.keys():
        if my_dict[key] == value:
            sorted_dict_up[key] = value
sorted_dict_down = {}
for value in sorted(my_dict.values(), reverse=True):
    for key in my_dict.keys():
        if my_dict[key] == value:
            sorted_dict_down[key] = value
print(my_dict)
print(sorted_dict_up)
print(sorted_dict_down)

print('++++++++++++++++++++')
# Вариант с использованием функционала sorted и лямбда функции
import random
my_dict = {i: random.randint(1, 10) for i in range(1, 10)}
sorted_dict_up = dict(sorted(my_dict.items(), key=lambda x: x[1]))
sorted_dict_down = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(my_dict)
print(sorted_dict_up)
print(sorted_dict_down)

print('++++++++++++++++++++')
# Вариант с использованием функционала sorted и функции operator.itemgetter 
import random
import operator
my_dict = {i: random.randint(1, 10) for i in range(1, 10)}
sorted_dict_up = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
sorted_dict_down = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))
print(my_dict)
print(sorted_dict_up)
print(sorted_dict_down)