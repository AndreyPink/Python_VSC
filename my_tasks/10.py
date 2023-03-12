# Напишите программу, которая выводит чётные числа из заданного списка 
# и останавливается, если встречает число 237

my_list = [1, 2, 3, 237, 4, 5, 6, 7, 8]
print(*[dig for dig in my_list[:my_list.index(237)] if dig%2 == 0] if 237 in my_list \
  else [dig for dig in my_list if dig%2 == 0])

