# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

from fractions import Fraction

def nod(a,b):
    for i in reversed(range(a+1)):
        if a % i == 0 and b % i == 0:
            a = a/i
            b = b/i
            break
    return a, b

frac1 = "0/1"
frac2 = "1/100"
n1 = int(frac1[0])
n2 = int(frac2[0])
d1 = int(frac1[2])
d2 = int(frac2[2])

if d1 != d2:
    dg = d1 * d2
    ng_sum = d1 * n2 + d2 * n1
else:
    dg = d1
    ng_sum = n1 + n2

if ng_sum > dg:
    a = nod(dg, ng_sum)[0]
    b = nod(dg, ng_sum)[1]
    print(f'Сумма дробей: {int(b)}/{int(a)}')
        
else:
    a = nod(ng_sum, dg)[0]
    b = nod(ng_sum, dg)[1]
    print(f'Сумма дробей: {int(a)}/{int(b)}')

ng_m = n1 * n2
dg = d1 * d2

if ng_m > dg:
    a = nod(dg, ng_m)[0]
    b = nod(dg, ng_m)[1]
    print(f'Произведение дробей: {int(b)}/{int(a)}')
        
else:
    a = nod(ng_m, dg)[0]
    b = nod(ng_m, dg)[1]
    print(f'Произведение дробей: {int(a)}/{int(b)}')


a = Fraction(frac1)
b = Fraction(frac2)
print(f'Сумма дробей: {a + b}')
print(f'Произведение дробей: {a * b}')


    
    




