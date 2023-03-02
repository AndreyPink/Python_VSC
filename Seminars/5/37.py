# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


import random
def create_seq(num, count = 0, my_list = ''):
    if count < num:
        return create_seq(num, count + 1, my_list + ' ' + str(random.randint(1,9)))
    print(f'Original list:{my_list}')
    return my_list[::-1]
    
number = int(input('Input length of list: '))    
print(f'Reverse list: {create_seq(number)}')

# def rev_seq(seq = '3 4'):
#     return seq[::-1]
# print(rev_seq())

