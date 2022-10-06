# импорт необходимых библиотек
import json
from colorama import Fore, Back, Style
from db_link import *


def check_search_menu():
    """
    Проверка корректности ввода пункт меню.
    """
    while True:
        try:
            num = int(
                input(Fore.BLUE + 'Введите номер пункта возможности: ' + Style.RESET_ALL))
            if 0 <= num <= 9:
                break
            else:                
                print(Fore.RED + 'Такого пункта меню нет! Попробуйте снова.' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.BLACK + Back.RED + 'Вы ввели некорректное число! Попробуйте снова.' + Style.RESET_ALL)

    return num


def check_directory():
    """
    Проверка, пустой ли справочник.
    :return:
    """
    try:
        with open(jsonFilename, 'r', encoding='utf-8') as f:
            phone_dir = json.load(f)
            if phone_dir != []:
                return True
    except ValueError:
        print(Fore.BLACK + Back.RED + 'Ваш справочник пока еще пустой!' + Style.RESET_ALL)
        return False



def check_menu_act_contact():
    while True:
        try:
            num = int(input(Fore.BLACK + Back.GREEN + 'Введите номер пункта, который хотите выполнить: '
                            + Style.RESET_ALL))

            if 0 <= num <= 4:
                break
            else:
                print(Fore.BLACK + Back.BLUE + 'Такого пункта меню нет!' + Style.RESET_ALL)
                print(Fore.BLACK + Back.GREEN + 'Такого пункта меню нет! Попробуйте снова.' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.BLACK + Back.RED + 'Вы ввели некорректное число! Попробуйте снова.' + Style.RESET_ALL)

    return num


def check_menu_ch_con():
    while True:
        try:
            num = int(input(Fore.BLACK + Back.GREEN + 'Введите номер пункта, который хотите выполнить: '
                            + Style.RESET_ALL))
            if 1 <= num <= 4:
                break
            else:
                print(Fore.BLACK + Back.BLUE + 'Такого пункта меню нет!' + Style.RESET_ALL)
                print(Fore.BLACK + Back.GREEN + 'Такого пункта меню нет! Попробуйте снова.' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.BLACK + Back.RED + 'Вы ввели некорректное число! Попробуйте снова.' + Style.RESET_ALL)

        return
