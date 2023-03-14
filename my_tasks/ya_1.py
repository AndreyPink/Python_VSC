# отобразить гистограмму по кол-ву символов в веденном тексте 

from collections import Counter

current_text = 'Hello, world!'
text = filter(lambda x: x != ' ', current_text)
my_string = ''
result_string = ''
full_list = []
my_dict = dict(Counter(text))

for _ in range(max(my_dict.values())):
    my_list = ['#' if value > 0 else ' ' for key, value in my_dict.items()]
    for key, value in my_dict.items():
        my_dict[key] = value - 1
    full_list.append(my_list)    
    
for my_list in reversed(full_list):
    for i in my_list:
        my_string += i + ' '
    result_string += my_string +'\n'
    my_string = ''
        
print(result_string)
print(*my_dict.keys())
        