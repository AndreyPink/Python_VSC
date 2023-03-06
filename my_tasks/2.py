# Напишите программу для слияния нескольких словарей в один.

# Вариант с добавлением элементов второго словаря в первый через цикл
import random
my_dict_1 = {i: random.randint(1, 10) for i in range(1, 6)}
print(my_dict_1)
my_dict_2 = {i: random.randint(1, 10) for i in range(6, 11)}
print(my_dict_2)
for key in my_dict_2:
    my_dict_1[key] = my_dict_2[key]
print(my_dict_1)

print('++++++++++++++++++++')
# Вариант с использованием dict comprehensions и функции update для генерации нового словаря из двух первоначальных
import random
my_dict_1 = {i: random.randint(1, 10) for i in range(1, 6)}
print(my_dict_1)
my_dict_2 = {i: random.randint(1, 10) for i in range(6, 11)}
print(my_dict_2)
result = {}
{result.update(elem) for elem in (my_dict_1, my_dict_2)}
print(result)
