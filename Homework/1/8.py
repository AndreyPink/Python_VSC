# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input('Введите кол-во долек по горизонтали: '))
# m = int(input('Введите кол-во долек по вертикали: '))
# k = int(input('Введите желаемое кол-во долек: '))
# if k >= n and k / n == round(k / n) or k >= m and k / m == round(k / m):
#     print('YES')
# else:
#     print('NO')
    
n = int(input('Введите кол-во долек по горизонтали: '))
m = int(input('Введите кол-во долек по вертикали: '))
k = int(input('Введите желаемое кол-во долек: '))
if k % n == 0 and k <= m * n or k % m == 0 and k <= m * n:
    print('YES')
else:
    print('NO')