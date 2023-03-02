# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b):
    # if b > 0:
    #     a += 1
    #     return sum(a, b-1)
    # else:
    #     return a
    return sum(a+1, b-1) if b > 0 else a

num_1 = int(input('Input num_1: '))    
num_2 = int(input('Input num_2: '))   
print(f'Sum numbers {num_1}+{num_2}={sum(num_1, num_2)}')