# Последовательностью Фибоначчи называется
# последовательность чисел 
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


def fibo(number, count = 2, fibo_min_1 = 1, fibo_min_2 = 0):
    if number == 0:
        return 0
    if number == 1:
        return 1
    if count == number:
        return fibo_min_1 + fibo_min_2
    else:
        return fibo(number, count + 1, fibo_min_1 + fibo_min_2, fibo_min_1)
num_fibo = int(input('Input N_fibo: '))
print(f'Fibo_{num_fibo} =', fibo(num_fibo))
    
