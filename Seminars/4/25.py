# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

my_string = input('Input string: ').split()
my_dict = {elem: 0 for elem in set(my_string)}
for elem in my_string:
    my_dict[elem] += 1
    if my_dict[elem] == 1:
        print(elem, end=' ')
    else:
        print(f'{elem}_{my_dict[elem]-1}', end=' ')
    
