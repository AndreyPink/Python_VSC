# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random
list = [random.randint(0,10) for i in range(10)]
print(f'Original list: {list}')
dif_list = []
for elem in list:
    if elem  not in dif_list:
        dif_list.append(elem)
print(f'List of different numbers: {dif_list}')
print(f'Sum of different numbers: {len(dif_list)}')


