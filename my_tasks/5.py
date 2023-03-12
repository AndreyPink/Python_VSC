# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза,
# которые одинаково читаются слева направо и справа налево.

text = input('Input string: ')
def is_poly(my_string):
    return "It's poly" if my_string == my_string[::-1] else 'Not poly'
print(is_poly(text))