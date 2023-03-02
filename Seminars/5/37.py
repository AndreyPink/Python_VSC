# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


# import random
# def print_list(num, count = 0, my_list = ''):
#     if count < num:
#         return print_list(num, count + 1, my_list + ' ' + str(random.randint(1,9)))
#     print(f'Original list:{my_list}')
#     return my_list[::-1]
    
# number = int(input('Input length of list: '))    
# print(f'Reverse list: {print_list(number)}')

import random
def print_list(num, count = 0, my_list = ''):
    if count < num:
        return print_list(num, count + 1, my_list + ' ' + str(random.randint(1,9)))
    print(f'Original list:{my_list}')
    return my_list[::-1]
    
number = int(input('Input length of list: '))    
print(f'Reverse list: {print_list(number)}')