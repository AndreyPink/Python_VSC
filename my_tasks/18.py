# Напишите программу, которая принимает текст и выводит два слова: 
#     наиболее часто встречающееся и самое длинное.

text = 'Напишите программу, которая принимает текст и и выводит два слова: наиболее часто встречающееся и самое два длинное  и.'
print(f'Longest word - "{sorted(text.split(), key= lambda x: len(x))[-1]}"')
print(f'Freq word - "{sorted(((key, value) for key, value in ({word: (text.split()).count(word) for word in text.split()}).items()), key= lambda x: x[1])[-1][0]}"')
# print(sorted([(key, value) for key, value in {(text.split()).count(word): word for word in text.split()}.items()])[-1][1])

print('********')
from collections import Counter
print(f'Longest word - "{max(text.split(), key=len)}"')
print(f'Freq word - "{Counter(text.split()).most_common()[0][0]}"')