from collections import Counter

text = 'hellohfyfkgkhjlhllkuiyyuo8uo'
my_dict = dict(Counter(text))
print(*my_dict.keys())
for _ in range(max(my_dict.values())):
    my_list = ['#' if value > 0 else ' ' for key, value in my_dict.items()]
    print(*my_list)
    for key, value in my_dict.items():
        my_dict[key] = value - 1
        
        
    # my_list = [(my_dict[key] = value - 1) for key, value in my_dict.items()]