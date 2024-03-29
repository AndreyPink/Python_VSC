
def read_file(data_path): # возврат списка всех строк в файле
    with open(data_path, 'r', encoding='UTF-8') as file:
        return file.readlines()

def write_file(data_path, data, key): # удаление данных из файла и запись новых данных
    with open(data_path, key, encoding='UTF-8') as file:
        if len(data) > 3:
            file.write(f'{data}')

def parsing_data(data, name): # поиск имени в строках данных и возврат строки с именем
    my_string = ''
    for line in data:
        if name in line.lower() and len(line) > 3:
            my_string += line
    return my_string

def change_delete(data_path, name, action):
    check = True
    data_file = read_file(data_path)
    for index, line in enumerate(data_file):
        if name in line.lower() and len(line) > 3:
            data_file[index] = action
            with open(data_path, 'w', encoding='UTF-8') as file:
                for line in data_file:
                    file.write(f'{line}')
            check = False
    if check:
        print(f'Name "{name}" not found')

data_path = 'Homework/8/data.txt'
result_path = 'Homework/8/result.txt'

while True:
    to_do = int(input('Change action:'
                        '\n1 - show info'
                        '\n2 - export info in result file'
                        '\n3 - import new record'
                        '\n4 - change info in file'
                        '\n5 - delete info in file'
                        '\n6 - exit\n:'))

    if to_do != 3 and to_do != 6:
        name = input('Input Last or First name: ').lower()

    if to_do == 1:
        data_file = read_file(data_path)
        print(parsing_data(data_file, name))

    if to_do == 2:
        data_file = read_file(data_path)
        result_data = parsing_data(data_file, name)
        write_file(result_path, result_data, 'w')

    if to_do == 3:
        data_file = input('Input Last, First name and phone number (through a space): ')+'\n'
        write_file(data_path, data_file, 'a')

    if to_do == 4:
        action = input('Input change in Last, First name and phone number (through a space): ')+'\n'
        change_delete(data_path, name, action)

    if to_do == 5:
        action = ''
        change_delete(data_path, name, action)
    if to_do == 6:
        break
