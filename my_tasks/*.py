numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]
print(*more_numbers, sep=', ')


date_info = {'year': "2020", 'month': "01", 'day': "01"}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)

numbers = [2, 1, 3, 4, 7]
a, b, *other, last = numbers
print(*other)

def palindrom(sequence):
    return [*sequence, *reversed(sequence)]
print(*palindrom('123'))

