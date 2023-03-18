import pandas as pd

# Определяем название файла csv и заголовки столбцов
filename = 'my_tasks/phonebook.csv'
headers = ['Name', 'Phone Number', 'Email']

# Создаем функцию для добавления контакта в телефонный справочник
def add_contact():
    # Запрашиваем у пользователя информацию о контакте
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")
    
    # Создаем новую запись в телефонном справочнике
    new_contact = pd.DataFrame([[name, phone_number, email]], columns=headers)
    
    # Добавляем новую запись в файл csv
    with open(filename, 'a') as f:
        new_contact.to_csv(f, header=False, index=False)
    
    print("Контакт успешно добавлен!")

# Создаем функцию для поиска контакта в телефонном справочнике
def find_contact():
    # Запрашиваем у пользователя имя контакта для поиска
    name = input("Введите имя для поиска: ")
    
    # Загружаем файл csv в DataFrame
    phonebook = pd.read_csv(filename, names=headers)
    
    # Ищем контакт в телефонном справочнике
    contact = phonebook.loc[phonebook['Name'] == name]
    
    # Выводим информацию о контакте
    if not contact.empty:
        print(contact)
    else:
        print("Контакт не найден.")

# Создаем функцию для удаления контакта из телефонного справочника
def delete_contact():
    # Запрашиваем у пользователя имя контакта для удаления
    name = input("Введите имя для удаления: ")
    
    # Загружаем файл csv в DataFrame
    phonebook = pd.read_csv(filename, names=headers)
    
    # Удаляем контакт из телефонного справочника
    phonebook = phonebook.loc[phonebook['Name'] != name]
    
    # Сохраняем изменения в файл csv
    phonebook.to_csv(filename, header=False, index=False)
    
    print("Контакт успешно удален!")

# Создаем функцию для вывода всех контактов из телефонного справочника
def show_contacts():
    # Загружаем файл csv в DataFrame
    phonebook = pd.read_csv(filename, names=headers)
    
    # Выводим все контакты из телефонного справочника
    print(phonebook)
    
def update_contact():
    name = input("Введите имя контакта, который нужно изменить: ")
    # загружаем csv-файл в DataFrame
    phonebook = pd.read_csv(filename, names=headers)
    # ищем контакт с введенным именем в DataFrame
    result = phonebook[phonebook["Name"] == name]
    # выводим результат поиска
    print(result.to_string(index=False))
    # запрашиваем новые данные для контакта
    new_name = input("Введите новое имя: ")
    new_phone = input("Введите новый телефон: ")
    new_email = input("Введите новый email: ")
    # обновляем данные контакта в DataFrame
    phonebook.loc[phonebook["Name"] == name, "Name"] = new_name
    phonebook.loc[phonebook["Name"] == name, "Phone"] = new_phone
    phonebook.loc[phonebook["Name"] == name, "Email"] = new_email
    # перезаписываем csv-файл с обновленными данными
    phonebook.to_csv(filename, header=False, index=False)
    print("Контакт успешно изменен в телефонной книге!")

# Создаем бесконечный цикл для работы с телефонным справочником
while True:
    # Выводим меню
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Показать все контакты")
    print("5. Изменить контакт")
    print("6. Выйти")
    
    # Запрашиваем у пользователя выбор действия
    choice = input("Выберите действие: ")
    
    # Выполняем выбранное действие
    if choice == '1':
        add_contact()
    elif choice == '2':
        find_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        show_contacts()
    elif choice == "5":
        update_contact()
    elif choice == '6':
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
    
