# Найдите три ключа с самыми высокими значениями в словаре
# 1
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sort_list = sorted(my_dict.items(), key= lambda x: x[1])
print(*(elem[0] for elem in sort_list[-3:]))

# 2
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(*result)

