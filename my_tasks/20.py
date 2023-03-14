from collections import Counter

text = 'hello'
my_dict = dict(Counter(text))
for _ in max(my_dict.values()):
    my_list = ['#' if value > 0 else ' ' for key, value in my_dict.items()]
    print(my_list)
    my_list = [(my_dict[key] = value - 1) for key, value in my_dict.items()]