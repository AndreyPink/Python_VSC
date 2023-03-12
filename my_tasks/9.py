# При заданном целом числе n посчитайте n + nn + nnn

# n = 5
# print(n + n*10+n + n*100+n*10+n)

def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(5)