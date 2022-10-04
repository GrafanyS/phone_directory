import json
import logger

def delete_contact(sorted_data, full_data):
    
    """Функция находит и удаляет заданную запись c контактом"""
    temp = []  
    if len(sorted_data)>1:
        for item in sorted_data:
            temp.append(item["id"])
        index_for_delete = int(input(f'Введите id контакта из данного списка {temp}: '))     #Здесь нужно добавить проверку, что пользователь ввел только индекс из списка
        if index_for_delete in temp:
            confirm = input('Вы уверены, что хотите удалить данный контакт? Да/Нет: ')  # Подтверждение, что пользователь действительно хочет удалить данный контакт
            if confirm.capitalize() == 'Да':    #Ввод подтверждения
                for item in full_data:
                    if index_for_delete == item["id"]:
                        logger.delete_contact(item)
                        full_data.remove(item)    #Если Да, то удаляем контакт из базы
                print('Контакт удален')
                return full_data
            else:    #Иначе, возвращаемся в главное меню
                return 'Возврат в главное меню'
        else: 
            return "Вы ввели неверный номер"
    elif len(sorted_data) == 1:
        confirm = input('Вы уверены, что хотите удалить данный контакт? Да/Нет: ')  # Подтверждение, что пользователь действительно хочет удалить данный контакт
        if confirm.capitalize() == 'Да':    #Ввод подтверждения
            for item in full_data:
                    if sorted_data[0]["id"] == item["id"]:
                        logger.delete_contact(item)
                        full_data.remove(item)    #Если Да, то удаляем контакт из базы
            print('Контакт удален')
            return full_data
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
#     
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


# print(delete_contact(sorted_data, full_data))