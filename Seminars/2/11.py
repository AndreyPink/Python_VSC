# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# from math import sqrt
# num = int(input('Input number: '))
# if sqrt(5*(num**2)-4)%1 == 0 or sqrt(5*(num**2)+4)%1 == 0:
#     print('in fibo')
# else:
#     print('not in fibo')


num = int(input('Input number: '))
fibo = 1
fibo_minus_2 = 0
fibo_minus_1 = 1
count = 2
while fibo < num:
    fibo = fibo_minus_2 + fibo_minus_1
    count += 1
    if fibo == num: print(count)
    fibo_minus_2 = fibo_minus_1
    fibo_minus_1 = fibo
if fibo != num: print(-1)