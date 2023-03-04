# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10^5. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод:     Вывод:
# 300       220 284

# Решение с помощью словарей
# max_num = int(input('Input number: '))
# num_dict = {}
# friendly_dict = {}
# for num in range(1, max_num):
#     list_dev = [dev for dev in range(1, num) if num % dev == 0]
#     num_dict[num] = sum(list_dev)
# for key_1, value_1 in num_dict.items():
#     for key_2, value_2 in num_dict.items():
#         if key_1 == value_2 and value_1 == key_2 and key_1 != value_1 and key_1 not in friendly_dict.values():
#             friendly_dict[key_1] = value_1
# [print(key, value) for key, value in friendly_dict.items()]

# Решение с помощью списков
max_num = int(input('Input number: '))
num_list = []
friendly_list = []
for num in range(1, max_num):
    list_dev = [dev for dev in range(1, num) if num % dev == 0]
    num_list.append(sum(list_dev))
for i in range(1, len(num_list)):
    for j in range(1,len(num_list)):
        if i == num_list[j-1] and num_list[i-1] == j and i != num_list[i-1] and i not in friendly_list:
            friendly_list.append(i)
            friendly_list.append(num_list[i-1])
[print(friendly_list[i], friendly_list[i+1]) for i in range(0, len(friendly_list), 2)]

