# Нужно проверить, все ли числа в последовательности уникальны

my_list = [10, 15, 30, 35, 45, 50, 60]
# print(True if sorted(my_list) == sorted(set(my_list)) else False)
print(True if len(my_list) == len(set(my_list)) else False)