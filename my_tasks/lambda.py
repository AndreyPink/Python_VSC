"""
my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x*2 , current_list))
print(new_list)

from functools import reduce
current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
summa = reduce((lambda x, y: x + y), current_list)
print(sum(current_list))
"""
