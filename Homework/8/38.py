# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


def export_data_in_file():
    check = False
    name = input('Input First or Last name: ').lower()
    with open(data_path, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            if name in line.lower():
                with open(result_path, 'w', encoding='UTF-8') as file:
                    file.write(line)
                print('Done')
                check = True
    if not check:
        print('Name not found')
                    
def show_data():
    check = False
    name = input('Input First or Last name: ').lower()
    with open(data_path, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            if name in line.lower():
                print(line)
                check = True
    if not check:
        print('Name not found')
                
def import_data_in_file():
    name = input('Input First, Last name and phone number (through a space): ')
    with open(data_path, 'a', encoding='UTF-8') as file:
        file.write(f'\n{name}')
    print('Done')
    
def import_file_in_file():
    source_path = input('Input source file path: ')
    with open(source_path, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            with open(data_path, 'a', encoding='UTF-8') as file:
                file.write(f'\n{line}')
    print('Done')
    
def change_info_in_file():
    check = False
    name = input('Input First or Last name: ').lower()
    with open(data_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        if name in line.lower():
            lines[index] = f"{input('Input change in First, Last name and phone number (through a space): ')}\n"
            with open(data_path, 'w', encoding='UTF-8') as file:
                file.writelines(lines)
            check = True
            print('Done')
    if not check:
        print('Name not found')
    
def delete_info_in_file():
    check = False
    name = input('Input First or Last name: ').lower()
    with open(data_path, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        if name in line.lower():
            lines[index] = '\n'
            with open(data_path, 'w', encoding='UTF-8') as file:
                file.writelines(lines)
            check = True
            print('Done')
    if not check:
        print('Name not found')

data_path = 'Seminars/8/data.txt'
result_path = 'Seminars/8/result.txt'

while True:
    to_do = int(input('Input action:'
                      '\n1 - show info'
                      '\n2 - export info in result file'
                      '\n3 - import info from text'
                      '\n4 - import info from file'
                      '\n5 - change info in file'
                      '\n6 - delete info in file\n: '))
    if to_do == 1:
        show_data()
        break
    elif to_do == 2:
        export_data_in_file()
        break
    elif to_do == 3:
        import_data_in_file()
        break
    elif to_do == 4:
        import_file_in_file()
        break
    elif to_do == 5:
        change_info_in_file()
        break
    elif to_do == 6:
        delete_info_in_file()
        break
    else:
        print('Wrong number')
        




            
