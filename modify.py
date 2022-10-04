import json


def modify_contact(sorted_data, full_data):
    """Функция находит и изменяет заданную запись c контактом"""
    temp = []

    if len(sorted_data) > 1:
        for i in sorted_data:
            temp.append(i["id"])
        # Здесь нужно добавить проверку, что пользователь ввел только индекс из списка
        index_for_change = int(
            input(f'Введите id контакта из данного списка {temp}: '))
        if index_for_change in temp:
            field_to_change = input(
                'Что вы хотите изменить: 1 - Фамилию, 2 - Имя, 3 - номер, 4 - комментарий: ')
            if field_to_change == '1':
                surname = input("Введите новую фамилию: ")
                full_data[index_for_change]["surname"] = surname
                print(
                    f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
                return full_data
            elif field_to_change == '2':
                name = input("Введите новое имя: ")
                full_data[index_for_change]["name"] = name
                print(
                    f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
                return full_data
            elif field_to_change == '3':
                tel = input("Введите новый номер: ")
                full_data[index_for_change]["tel"] = tel
                print(
                    f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
                return full_data
            elif field_to_change == '4':
                description = input("Введите новый комментарий: ")
                full_data[index_for_change]["description"] = description
                print(
                    f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
                return full_data
        else:
            return "Вы ввели неверный номер"
    elif len(sorted_data) == 1:
        index_for_change = sorted_data[0]["id"]
        field_to_change = input(
            'Что вы хотите изменить: 1 - Фамилию, 2 - Имя, 3 - номер, 4 - комментарий: ')
        if field_to_change == '1':
            surname = input("Введите новую фамилию: ")
            full_data[index_for_change]["surname"] = surname
            print(f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
            return full_data
        elif field_to_change == '2':
            name = input("Введите новое имя: ")
            full_data[index_for_change]["name"] = name
            print(f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
            return full_data
        elif field_to_change == '3':
            tel = input("Введите новый номер: ")
            full_data[index_for_change]["tel"] = tel
            print(f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
            return full_data
        elif field_to_change == '4':
            description = input("Введите новый комментарий: ")
            full_data[index_for_change]["description"] = description
            print(f'Измененный контакт: {full_data[index_for_change]["id"]} {full_data[index_for_change]["surname"]} {full_data[index_for_change]["name"]} {full_data[index_for_change]["tel"]} {full_data[index_for_change]["description"]}')
            return full_data
    else:
        return 'Возврат в главное меню'
        
def write_json_full(data):
    with open('phone_directory.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('База данных успешно обновлена')      


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
