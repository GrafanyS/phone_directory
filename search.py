import json
from colorama import Fore, Back, Style


def search(num, i=None, surname_key=None):
    with open('phone_directory.json', 'r', incoding="UTF-8") as f:
        phone_dir: object = json.load(f)

    search_res = []
    if num == 1:
        surname_key = input(Fore.GREEN + "" 'Введите фамилия контакта: ' + Style.RESET_ALL)
        for i in phone_dir:
            if i['surname'] == surname_key:
                search_res.append(i)
        return search_res

    if num == 2:
        surname_key = input(Fore.GREEN + 'Введите фамилию контакта: ' + Style.RESET_ALL)
        for i in phone_dir:
            if i['surname'] == surname_key:
                search_res.append(i)
        return search_res

    if num == 3:
        surname_key = input(Fore.GREEN + 'Введите фамилию контакта: ' + Style.RESET_ALL)
        for i in phone_dir:
            if i['surname'] == surname_key:
                search_res.append(i)
        return search_res

    if num == 4:
        surname_key = input(Fore.GREEN + 'Введите фамилию контакта: '+ Style.RESET_ALL)
        for i in phone_dir:
            if i['surname'] == surname_key:
                search_res.append(i)
        return search_res
