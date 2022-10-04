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
  
my_phonebook = [
    {
        "id": 0,
        "surname": "Шагал",
        "name": "Денис",
        "tel": "3465635",
        "description": ""
    },
    {
        "id": 1,
        "surname": "Иванов",
        "name": "Петр",
        "tel": "3465674684",
        "description": "друг"
    },
    {
        "id": 2,
        "surname": "Петров",
        "name": "Максим",
        "tel": "987876675",
        "description": "знакомый"
    },
    {
        "id": 3,
        "surname": "Иванов",
        "name": "Сергей",
        "tel": "546357367",
        "description": "кто-то"
    },
    {
        "id": 4,
        "surname": "Сидоров",
        "name": "Иван",
        "tel": "54656767",
        "description": "однажды встретил на улице"
    },
    {
        "id": 5,
        "surname": "Курицын",
        "name": "Эдуард",
        "tel": "465356357",
        "description": "куевкп"
    },
    {
        "id": 6,
        "surname": "Ренжин",
        "name": "Василий",
        "tel": "3465667",
        "description": "выапвп"
    },
    {
        "id": 7,
        "surname": "Кочегар",
        "name": "Михаил",
        "tel": "5476758",
        "description": "ывнен"
    }
]
                

print(delete_contact(my_phonebook))