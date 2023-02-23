# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Создаем новый список
# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#            {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# new_list = []
# for elem in my_list:
#     for key in elem:
#         if elem[key] not in new_list:
#             new_list.append(elem[key])
# print(f'New list: {new_list}')

# Создаем новое множество
my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
new_list = set()
for elem in my_list:
    for key in elem:
        new_list.add(elem[key])
print(f'New list: {new_list}')