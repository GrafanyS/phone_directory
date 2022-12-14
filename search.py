import json
from logger import *
from colorama import Fore, Back, Style
from db_link import *


def read_json(file):
    try:
        with open(dbFilename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except ValueError:
        print(Back.RED + 'В базе еще нет ни одного контакта :(' + Style.RESET_ALL)
        ValueError_logger()


def search_contact(data):
    try:
        name = input(Fore.BLUE +
                     'Введите имя контакта, номер телефона или комментарий: ' + Style.RESET_ALL)
        found_contacts = []
        temp = {1: "surname", 2: "name", 3: "tel", 4: "description"}
        for index, contact in enumerate(data):
            if name.lower() in contact["surname"].lower() or name.lower() in contact["name"].lower() \
                    or name.lower() in contact["tel"].lower() or name.lower() in contact["description"].lower():
                found_contacts.append(contact)
                # Выводим заданный контакт
                print(
                    f'Найден контакт: {contact["id"]} {contact["surname"]} {contact["name"]} {contact["tel"]} '
                    f'{contact["description"]}')
        if found_contacts != []:
            return found_contacts
        else:
            print(Fore.RED + 'Такого контакта нет в базе.' + Style.RESET_ALL)
            return found_contacts
    except ValueError:
        print(Fore.RED + 'В базе такого контакта нет' + Style.RESET_ALL)
        ValueError_logger()


if __name__ == '__main__':
    search_contact()
