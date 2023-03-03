# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод:       Вывод:
# 1 2 3 2 3   2

from random import randint
my_list = [randint(1,9) for _ in range(int(input('Input length mass: ')))]
check_list = {elem: my_list.count(elem)//2 for elem in my_list if my_list.count(elem)//2 > 0}
print(f'Sorted original list: {sorted(my_list)}')
print(f'Check list: {check_list}')
print(f'Amount of pair: {sum(check_list.values())}')
