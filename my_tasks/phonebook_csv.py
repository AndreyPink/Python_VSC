import pandas as pd

path_csv = 'my_tasks/phonebook.csv'
# df = pd.DataFrame({'Names': ['Иванов Иван', 'Петров Петр', 'Васильев Василий'],
#  'Phones': [111, 222, 333]})
# df.to_csv(path_csv, index= False)


# path_csv = 'https://drive.google.com/file/d/1DL6M6nZMXhAYvDJMai-_G6zXlK7aFCnf/view?usp=share_link'
# path_xlsx = 'https://github.com/AndreyPink/Python_VSC/blob/main/Homework/9/phonebook.xlsx'
# path_xlsx = 'my_tasks/phonebook.xlsx'
# path_csv = 'my_tasks/phonebook.csv'
file = pd.read_csv(path_csv)

#изменение индексов на название
# df = df.set_index('Last_name')

# запись в файл
# df.to_excel(path_xlsx)

# df.to_excel(path_xlsx, index=False)


# поиск по имени или фамилии (варианты)
# print(df[(df['Last_name'] == name) | (df['First_name'] == name)])
# print(df[df['Last_name'] == name])
# print(df[df.Last_name == name])

# добавление нового контакта
# new_contact = input('Введите Фамилию, Имя и телефон (через пробел): ').split()
# df.loc[len(df.index )] = new_contact


# удаление контакта

# df.drop(labels= [3], axis=0, inplace=True) #по индексу (если они сохранены)
# df.drop(['Пинк'], axis=0, inplace= True) # по названию


while True:
    to_do = int(input('\nChange action:'
                        '\n1 - show book'
                        '\n2 - find contact'
                        '\n3 - import new record'
                        '\n4 - change info in file'
                        '\n5 - delete info in file'
                        '\n6 - exit\n:'))


    if to_do == 1:
        print(file)

    if to_do == 2:
        name = input('Input Last or First name: ')
        for index, elem in enumerate(file['Names']):
            if name in elem.lower():
                print(file.loc[index])

    if to_do == 3:
        new_contact_name = input('Введите Фамилию и  Имя (через пробел): ')
        new_contact_phone = input('Введите номер телефона: ')
        file.loc[len(file.index )] = new_contact_name #!!!!!!!!!
        file.to_csv(path_csv, index=False)

    if to_do == 4:
        print(file)
        num = int(input('Введите номер контакта для изменения: '))
        file.drop(labels= [num], axis=0, inplace=True)
        new_contact_name = input('Введите Фамилию и  Имя (через пробел): ')
        new_contact_phone = input('Введите номер телефона: ')
        new_contact = new_contact_name+','+new_contact_phone #!!!!!!!!
        file.loc[len(file.index )].replace = new_contact
        file.to_csv(path_csv, index=False)

    if to_do == 5:
        print(file)
        num = int(input('Введите номер контакта для удаления: '))
        file.drop(labels= [num], axis=0, inplace=True)
        file.to_csv(path_csv, index=False)

    if to_do == 6:
        break
