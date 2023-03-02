# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# Решение через цикл
# def check_simple_num(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return "It's not simple"
#     return "Yes, it's simple"

# number = int(input('Input number for check: '))
# print(check_simple_num(number))

# Решение рекурсивно
def check_simple_num(num, i = 2):
    if num % i == 0:
        return "It's not simple"
    elif i < num - 1:
        return check_simple_num(num, i + 1)
    else:
        return "Yes, it's simple"

number = int(input('Input number for check: '))
print(check_simple_num(number))