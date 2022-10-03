
import json
from colorama import Fore, Back, Style


def check_main_menu():
    while True:
        try:
            num = int(input(Fore.BLACK + "" + Back.GREEN + 'Введите номер пункта, который хотите выполнить: '
                            + Style.RESET_ALL))
            if 0 <= num <= 6:
                break
            else:
                print(Fore.BLACK + "" + Back.BLUE + 'Такого пункта меню нет!' + Style.RESET_ALL)
                print(Fore.BLACK + "" + Back.GREEN + 'Такого пункта меню нет! Попробуйте снова.' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.BLACK + "" + Back.RED + 'Вы ввели некорректное число! Попробуйте снова.' + Style.RESET_ALL)

    return num


def check_search_menu():
    while True:
        try:
            num = int(
                input(Fore.BLACK + "" + Back.GREEN + 'Введите номер пункта, по которому вы хотите найти контакт: '
                      + Style.RESET_ALL))
            if 0 <= num <= 1:
                break
            else:
                print(Fore.BLACK + "" + Back.BLUE + 'Такого пункта меню нет!' + Style.RESET_ALL)
                print(Fore.BLACK + "" + Back.GREEN + 'Такого пункта меню нет! Попробуйте снова.' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.BLACK + "" + Back.RED + 'Вы ввели некорректное число! Попробуйте снова.' + Style.RESET_ALL)

    return num


def check_directory():
    """
    Проверка, пустой ли справочник.
    :return:
    """
    try:
        with open('phone_directory.json', 'r') as f:
            phone_dir = json.load(f)
            return True
    except ValueError:
        print(Fore.BLACK + "" + Back.RED + 'Ваш справочник пока еще пустой!' + Style.RESET_ALL)
        return False


def check_menu_act_contact():
    while True:
        try:
            num = int(input(Fore.BLACK + "" + Back.GREEN + 'Введите номер пункта, который хотите выполнить: '
                            + Style.RESET_ALL))
            if 0 <= num <= 4:
                break
            else:
                print(Fore.BLACK + "" + Back.BLUE + 'Такого пункта меню нет!' + Style.RESET_ALL)
                print(Fore.BLACK + "" + Back.GREEN + 'Такого пункта меню нет! Попробуйте снова.' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.BLACK + "" + Back.RED + 'Вы ввели некорректное число! Попробуйте снова.' + Style.RESET_ALL)

    return num


def check_menu_ch_con():
    while True:
        try:
            num = int(input(Fore.BLACK + "" + Back.GREEN + 'Введите номер пункта, который хотите выполнить: '
                            + Style.RESET_ALL))
            if 1 <= num <= 4:
                break
            else:
                print(Fore.BLACK + "" + Back.BLUE + 'Такого пункта меню нет!' + Style.RESET_ALL)
                print(Fore.BLACK + "" + Back.GREEN + 'Такого пункта меню нет! Попробуйте снова.' + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.BLACK + "" + Back.RED + 'Вы ввели некорректное число! Попробуйте снова.' + Style.RESET_ALL)

        return
