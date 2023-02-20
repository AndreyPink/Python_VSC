# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

"""
number_watermelon = int(input('Input number of watermelon: '))
max_weight_index = 0
min_weight_index = 0
weight_list = []
for i in range(number_watermelon):
    weight_list.append(int(input(f'Input weight of {i + 1} watermelon: ')))
    if weight_list[i] > weight_list[max_weight_index]:
        max_weight_index = i
    elif weight_list[i] < weight_list[min_weight_index]:
        min_weight_index = i     
print(f'Min weight = {weight_list[min_weight_index]}, Max weight = {weight_list[max_weight_index]}')
"""

number_watermelon = int(input('Input number of watermelon: '))
weight_1 = int(input(f'Input weight of 1 watermelon: '))
max_weight = weight_1
min_weight = weight_1
for i in range(number_watermelon - 1):
    weight = int(input(f'Input weight of {i + 2} watermelon: '))
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight    
print(f'Min weight = {min_weight}, Max weight = {max_weight}')