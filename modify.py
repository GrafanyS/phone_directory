import json

def modify_contact(sorted_data, full_data):
    
    """Функция находит и изменяет заданную запись c контактом"""
    temp = []  
    if len(sorted_data)>0:
        for i in sorted_data:
            temp.append(i["id"])
        index_for_change = int(input(f'Введите id контакта для удаления из данного списка {temp}: '))     #Здесь нужно добавить проверку, что пользователь ввел только индекс из списка
        if index_for_change in temp:
            confirm = input('Вы уверены, что хотите изменить данный контакт? Да/Нет: ')  # Подтверждение, что пользователь действительно хочет удалить данный контакт
            if confirm.capitalize() == 'Да':    #Ввод подтверждения
                field_to_change = input('Что вы хотите изменить: 1 - Фамилию, 2 - Имя, 3 - номер, 4 - комментарий: ')
                if field_to_change == '1':
                    surname = input("Введите новую фамилию: ")
                    full_data[index_for_change]["surname"] = surname
                    return full_data
                if field_to_change == '2':
                    name = input("Введите новое имя: ")
                    full_data[index_for_change]["name"] = name
                    return full_data
                if field_to_change == '3':
                    tel = input("Введите новый номер: ")
                    full_data[index_for_change]["tel"] = tel
                    return full_data
                if field_to_change == '4':
                    description = input("Введите новый комментарий: ")
                    full_data[index_for_change]["description"] = description
                    return full_data
            else:    #Иначе, возвращаемся в главное меню
                return 'Возврат в главное меню'
        else: 
            return "Вы ввели неверный номер"
    else:
        return 'Возврат в главное меню'  

  
# sorted_data = [
#     {
#         "id": 0,
#         "surname": "Шагал",
#         "name": "Денис",
#         "tel": "3465635",
#         "description": ""
#     },
#     {
#         "id": 2,
#         "surname": "Петров",
#         "name": "Максим",
#         "tel": "987876675",
#         "description": "знакомый"
#     },
#     {
#         "id": 6,
#         "surname": "Ренжин",
#         "name": "Василий",
#         "tel": "3465667",
#         "description": "выапвп"
#     }
# ]

# full_data = [
#     {
#         "id": 0,
#         "surname": "Шагал",
#         "name": "Денис",
#         "tel": "3465635",
#         "description": ""
#     },
#     {
#         "id": 1,
#         "surname": "Иванов",
#         "name": "Петр",
#         "tel": "3465674684",
#         "description": "друг"
#     },
#     {
#         "id": 2,
#         "surname": "Петров",
#         "name": "Максим",
#         "tel": "987876675",
#         "description": "знакомый"
#     },
#     {
#         "id": 3,
#         "surname": "Иванов",
#         "name": "Сергей",
#         "tel": "546357367",
#         "description": "кто-то"
#     },
#     {
#         "id": 4,
#         "surname": "Сидоров",
#         "name": "Иван",
#         "tel": "54656767",
#         "description": "однажды встретил на улице"
#     },
#     {
#         "id": 5,
#         "surname": "Курицын",
#         "name": "Эдуард",
#         "tel": "465356357",
#         "description": "куевкп"
#     },
#     {
#         "id": 6,
#         "surname": "Ренжин",
#         "name": "Василий",
#         "tel": "3465667",
#         "description": "выапвп"
#     },
#     {
#         "id": 7,
#         "surname": "Кочегар",
#         "name": "Михаил",
#         "tel": "5476758",
#         "description": "ывнен"
#     },
#     {
#         "id": 8,
#         "surname": "Бумагин",
#         "name": "Василий",
#         "tel": "346547",
#         "description": "фуепкеген"
#     },
#     {
#         "id": 9,
#         "surname": "Белов",
#         "name": "Анатолий",
#         "tel": "34657",
#         "description": "вафыпао"
#     }
# ]


# print(modify_contact(sorted_data, full_data))