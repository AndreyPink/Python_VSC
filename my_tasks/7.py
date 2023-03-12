# Вы принимаете от пользователя последовательность чисел, разделённых запятой. 
# Составьте список и кортеж с этими числами.

my_string = '1,2,3,4,5'
my_list = list(map(lambda x: int(x), my_string.split(',')))
my_tuple = tuple(map(lambda x: int(x), my_string.split(',')))
print(my_list)
print(my_tuple)