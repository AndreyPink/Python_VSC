# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree(a, b):
    if b > 1:
        return a * degree(a, b-1)
    else:
        return a

num_1 = int(input('Input num_1: '))    
num_2 = int(input('Input num_2: '))   
print(f'{num_1}^{num_2}={degree(num_1, num_2)}')

