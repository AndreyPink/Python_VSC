# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


# Вариант через нахождение корня квадратного уравнения
"""
import math
sum = int(input('Input Sum of numbers: '))
prod = int(input('Input Product of numbers: '))
x = abs(-sum + math.sqrt(sum ** 2 - 4 * prod)) / 2
if x % 1 != 0:
    print('Input error')
else:    
    print(f'X = {round(x)}, Y = {sum - round(x)}')
"""

# Вариант через перебор двух чисел        
sum = int(input('Input Sum of numbers: '))
prod = int(input('Input Product of numbers: '))
for i in range(1, 1001):
    for j in range(1, 1001):
        if sum == i + j and prod == i * j:
            x, y = i, j
print(f'X = {x}, Y = {y}')        


