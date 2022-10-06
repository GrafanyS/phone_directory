import json
import db_link
from colorama import Fore, Back, Style


# def get_value():
#     print('Для занесения контакта в справочник заполните поочередно данные: ')
#     dict_ph = {}
#     dict_ph['id'] = input('id: ')
#     dict_ph['surname'] = input('Введите фамилию: ')
#     dict_ph['name'] = input('Введите имя: ')
#     dict_ph['tel'] = input('Введите номер: ')
#     dict_ph['description'] = input('Комментарий: ')
#     print('#' * 50)
#     return dict_ph


# def show_contact(list_res):
#     '''
#     Выводит в консоль найденные контакты
#     :param list_res:
#     :return:
#     '''
#     print('Найдены следующие контакты: ')
#     for num, i in enumerate(list_res):
#         print(
#             Fore.YELLOW + f'Контакт № {num+1}\n'
#             f'id: {i["id"]}\n'
#             f'Фамилия: {i["surname"]}\n'
#             f'Имя: {i["name"]}\n'
#             f'Телефон: {i["tel"]}\n'
#             f'Статус: {i["comment"]}\n' + Style.RESET_ALL)


# def show_all_contact():
#     '''
#     Выводит в консоль все контакты контакты
#     :param list_res:
#     :return:
#     '''

#     with open(db_link.jsonFilename, 'r', encoding='utf-8') as f:
#         phone_dir = json.load(f)
#     print('Найдены следующие контакты: ')
#     for num, i in enumerate(phone_dir):
#         print(
#             Fore.YELLOW + f'Контакт № {num+1}\n'
#             f'id: {i["id"]}\n'
#             f'Фамилия: {i["surname"]}\n'
#             f'Имя: {i["name"]}\n'
#             f'Телефон: {i["tel"]}\n'
#             f'Статус: {i["comment"]}\n' + Style.RESET_ALL)

def gen_person():
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    tel = input('Введите номер телефона:')
    description = input('Дополнительная информация:')

    person = {
        'id': 0,
        'surname': surname,
        'name': name,
        'tel': tel,
        'description': description
    }
    return person


def show_all_contacts(data):
    for item in data:
        print(
            f'{item["id"]} {item["surname"]} {item["name"]} {item["tel"]} {item["description"]}')
