import json

def delete_contact(phonebook_data):
    
    """Функция находит и удаляет заданную запись c контактом"""

    with open('phone_directory.json, 'r', encoding='utf-8') as f:
        phonebook_data = json.load(f)

    phonebook_data = (phonebook) #В модуле modol_import.py должна быть функция получения данных из файла в виде словаря. Название функции read_phonebook пока задано условно.
    try:
        search_item = int(input('Для поиска контакта для удаления введите 1 (если поиск по фамилии), 2 (если поиск по имени): '))
        if 0 < search_item < 3:
            name = input('Введите имя контакта, который хотите удалить: ')    #Ввод имени контакта для удаления
            #проверка: существует ли данный контакт. Позднее можно проверку вынести в модуль check, и вставить сюда только функцию проверки
            index_del = []
            temp = {1:"surname", 2:"name"}   
            for index, dict in enumerate(phonebook_data):
                while name.lower() == dict[temp[search_item]].lower():
                    index_del.append(index)    
                    print(f'Найден контакт {index}:', dict)    #Выводим заданный контакт
                    break
            if index_del != []:    
                if len(index_del)>1:
                    user_index = int(input(f'Выберите запись для удаления {index_del}: '))     #Здесь нужно добавить проверку, что пользователь ввел только индекс из списка
                    confirm = input('Вы уверены, что хотите удалить данный контакт? Да/Нет: ')  # Подтверждение, что пользователь действительно хочет удалить данный контакт
                    if confirm.capitalize() == 'Да':    #Ввод подтверждения
                        del phonebook_data[user_index]    #Если Да, то удаляем контакт из базы
                    else:    #Иначе, возвращаемся в главное меню
                        return 'Возврат в главное меню'
                else:
                    confirm = input('Вы уверены, что хотите удалить данный контакт? Да/Нет: ')
                    if confirm.capitalize() == 'Да':    
                        del phonebook_data[index_del[0]]
                    else:
                            return 'Возврат в главное меню'
                return(phonebook_data)  
                # write_phonebook(phonebook, phonebook_data) ##В модуле modol_export.py должна быть функция записи данных в файл в виде словаря. Название функции write_phonebook пока задано условно.
            else:    #Иначе выводим пользователю сообщение, что такого контакта в базе нет
                return 'Контакт не существует!'
        else:
            print('Вы ввели некорректное значение')
    except:
        print('Вы ввели не число')
  
my_phonebook = [{"surname": "Иванов",
                "name": "Иван",
                "tel": "799968723",
                "description": "бла бла бла"},
                {"surname": "Петров",
                "name": "Петр",
                "tel": "755568723",
                "description": "бла бла бла"},
                {"surname": "Павлов",
                "name": "Павел",
                "tel": "744468723",
                "description": "бла бла бла"},
                {"surname": "Смирнов",
                "name": "Иван",
                "tel": "744468723",
                "description": "бла бла бла"}]
                

print(delete_contact(my_phonebook))