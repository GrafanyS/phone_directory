def delete(name, phonebook):
    """Функция удаляет заданную запись c контактом"""

    phonebook_data = read_phonebook(phonebook) #В модуле modol_import.py должна быть функция получения данных из файла в виде словаря. Название функции read_phonebook пока задано условно.

    #Ввод имени контакта для удаления
    name = input('Введите имя контакта, который хотите удалить: ')
    #проверка: существует ли данный контакт. Позднее можно проверку вынести в модуль check, и вставить сюда только функцию проверки
    if name in phonebook_data:
        #Выводим заданный контакт
        print('The contact is',name,':',phonebook_data[name])
        #Иначе выводим пользователю сообщение, что такого контакта в базе нет
    else:
        print('That contact does not exist! Return to the main menu to enter the contact')
        
    #Подтверждение, что пользователь действительно хочет удалить данный контакт
    confirm = input('Are you sure you wish to delete this contact? Yes/No: ')
    #Ввод подтверждения
    if confirm.capitalize() == 'Yes':
        #Если Yes, то удаляем контакт из базы
        del phonebook_data[name]
        write_phonebook(phonebook, phonebook_data) ##В модуле modol_export.py должна быть функция записи данных в файл в виде словаря. Название функции write_phonebook пока задано условно.
    #Иначе, возвращаемся в главное меню
    else:
        print('Return to Main Menu')
        