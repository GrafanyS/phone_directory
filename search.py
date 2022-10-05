import json
from colorama import Fore, Back, Style
from db_link import *
import check
import logger as lo


# def gen_person():
#     surname = input(Fore.GREEN + 'Введите фамилию:' + Style.RESET_ALL)
#     name = input(Fore.GREEN + 'Введите имя:' + Style.RESET_ALL)
#     tel = input(Fore.GREEN + 'Введите номер телефона:' + Style.RESET_ALL)
#     description = input(
#         Fore.GREEN + 'Дополнительная информация:' + Style.RESET_ALL)

#     person = {
#         'id': id,
#         'surname': surname,
#         'name': name,
#         'tel': tel,
#         'description': description
#     }
#     return person


def search_write_json(person_dict):
    try:
        with open(jsonFilename, "r", encoding='utf-8') as f:
            data = json.load(f)
    except ValueError:
        data = []

    # search_res = []
    # if num == 1:
    #     surname_key = input('Введите фамилию контакта: ')
    #     for i in phone_dir:
    #         if i['surname'] == surname_key:
    #             search_res.append(i)
    #     return search_res

    data.append(person_dict)

    for i in range(len(person_dict)):
        if person_dict[i] == data[0]:
            print(Fore.BLACK + Back.BLUE +
                  'Что вы хотите изменить:' + Style.RESET_ALL + '\n'
                                                                '1. id: \n'
                                                                '2. Фамилию: \n'
                                                                '3. Имя: \n'
                                                                '4. Номер телефона: \n'
                                                                '5. Описание: ')
            num = check.check_menu_ch_con()
            if num == 1:
                person_dict.pop(i)
                data[0]['id'] = input('Введите новую id: ')
                person_dict.append(data[0])
            if num == 2:
                person_dict.pop(i)
                data[1]['surname'] = input('Введите новую фамилию: ')
                person_dict.append(data[1])

            if num == 3:
                person_dict.pop(i)
                data[2]['name'] = input('Введите новое имя: ')
                person_dict.append(data[2])

            if num == 4:
                person_dict.pop(i)
                data[3]['tel'] = input('Введите телефон: ')
                person_dict.append(data[3])

            if num == 5:
                person_dict.pop(i)
                data[4]['comment'] = input('Введите новую фамилию: ')
                person_dict.append(data[4])

    with open(jsonFilename, 'w', encoding='utf-8') as file:
        json.dump(person_dict, file, indent=2, ensure_ascii=False)
    print(Fore.BLACK + "" + Back.GREEN + f'Ваш контакт успешно изменен. Переводим вас в начало меню' + Style.RESET_ALL)

    with open(jsonFilename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# def main():
#     for i in range(1):
#         write_json(gen_person())


if __name__ == 'main':
    search_write_json()
    # main()
# print(__name__)
