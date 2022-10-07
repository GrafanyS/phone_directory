# импорт необходимых библиотек
import json
from colorama import Fore, Back, Style
from db_link import *
import logger


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


def write_json(person_dict):
    try:
        with open(dbFilename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = []
    last_id = int(data[len(data) - 1]["id"])
    person_dict["id"] = last_id + 1
    data.append(person_dict)
    with open(dbFilename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    logger.create_contact(person_dict)
    print(Fore.BLUE + 'Контакт успешно добавлен\n' + Style.RESET_ALL)


if __name__ == '__main__':
    gen_person()
    write_json()
