import json
from colorama import Fore, Back, Style
import db_link

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
        data = json.load(open(db_link.jsonFilename))
    except ValueError:
        data = []

    data.append(person_dict)

    with open(db_link.jsonFilename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# def main():
#     for i in range(1):
#         write_json(gen_person())


if __name__ == 'main':
    search_write_json()
    # main()
# print(__name__)
