# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

number = int(input('Input number: '))
shift = int(input('Input shift: '))
list = [int(i) for i in range(1, number + 1)]
print(f'Original list: {list}')
new_list = []
for i in range(shift, number):
    new_list.append(list[i])
for i in range(shift):
    new_list.append(list[i])
print(f'New list: {new_list}')
