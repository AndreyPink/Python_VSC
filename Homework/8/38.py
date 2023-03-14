
def read_file(data_path): # возврат списка всех строк в файле
    with open(data_path, 'r', encoding='UTF-8') as file:
        return file.readlines()

def wright_file(data_path, data, key): # удаление данных из файла и запись новых данных
    with open(data_path, key, encoding='UTF-8') as file:
        file.write(f'\n{data}')

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

to_do = int(input('Change action:'
                      '\n1 - show info'
                      '\n2 - export info in result file'
                      '\n3 - import new record'
                      '\n4 - change info in file'
                      '\n5 - delete info in file\n: '))

if to_do != 3:
    name = input('Input First or Last name: ').lower()

if to_do == 1:
    data_file = read_file(data_path)
    print(parsing_data(data_file, name))

if to_do == 2:
    data_file = read_file(data_path)
    result_data = parsing_data(data_file, name)
    wright_file(result_path, result_data, 'w')

if to_do == 3:
    data_file = input('Input First, Last name and phone number (through a space): ')
    wright_file(data_path, data_file, 'a')

if to_do == 4:
    action = input('Input change in First, Last name and phone number (through a space): ')
    change_delete(data_path, name, action)

if to_do == 5:
    action = ''
    change_delete(data_path, name, action)
