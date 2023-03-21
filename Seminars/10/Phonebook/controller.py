import phonebook

pb = phonebook.Phonebook('Seminars/10/Phonebook/phone.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберете пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите номер телефона: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input('Введите индекс контакта, который будем изменять: '))
            name = input('Введите имя (или Enter - оставить без изменения): ')
            phone = input('Введите номер телефона (или Enter - оставить без изменения): ')
            comment = input('Введите комментарий (или Enter - оставить без изменения): ')
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Введите индекс контакта, который хотите удалить: '))
            pb.delete(index-1)
        case 6:
            pb.save()
        case 7:
            break