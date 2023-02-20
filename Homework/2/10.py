# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

number_coins = int(input('Input number of coins: '))
side_1_count = 0
side_0_count = 0
for i in range(number_coins):
    side = int(input(f'Input side of {i + 1} coin (1 or 0): '))
    if side == 1:
        side_1_count += 1
    else:
        side_0_count += 1
if side_1_count < side_0_count:
    print(f'Min revers = {side_1_count}')
else:
    print(f'Min revers = {side_0_count}')
