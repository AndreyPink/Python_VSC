from collections import Counter

text = 'hello'

new_string = ''
for i in range(len(text)-1):
    new_string += text[i:]
for i in range(len(text)-1):
    new_string += text[:-i]
new_string += text
print(dict(Counter(new_string)))


# for i in range(len(text)):
#     for j in range(i+1):
#         new_string += text[j:]
        
        
        

