import create
import ui
import menu
import check
import search
import logger
import delete
import modol_export
import modol_import
import modify
from db_link import *
from colorama import Fore, Back, Style


def main_func():
    menu.main_menu()
    while True:
        # Выбор пункта меню
        punct_menu = check.check_search_menu()
        # Показать список пунктов меню
        if punct_menu == 0:
            menu.main_menu()
        # Добавление нового контакта
        elif punct_menu == 1:
            dict_ph = ui.gen_person()
            create.write_json(dict_ph)
        # Поиск контакта
        elif punct_menu == 2:
            if check.check_directory():  # Проверка не пустой ли справочник
                # Считавание всей базы из файла 'phone_directory.json'
                all_contacts = search.read_json(jsonFilename)
                found_contacts = search.search_contact(
                    all_contacts)  # Поиск контакта по критериям
                if found_contacts != []:  # Проверка найден ли хотя бы один контакт
                    # Выбор пункта - что дальше делаем с контактом
                    further_action = input(
                        'Что вы хотите сделать с найденным контактом:' + Fore.RED + '1 - удалить, '
                        + Fore.GREEN + '2 - изменить, ' + Fore.YELLOW + '3 - ничего: ' + Style.RESET_ALL)
                    if further_action == '1':
                        data = delete.delete_contact(
                            found_contacts, all_contacts)  # Удаление контакта
                        modify.modify_contact(data)
                    elif further_action == '2':
                        data = modify.modify_contact(
                            found_contacts, all_contacts)  # Изменение контакта
                        modify.modify_contact(data)
                    else:
                        menu.main_menu()  # Выход в главное меню
        # Вывод всех контактов
        elif punct_menu == 3:
            if check.check_directory():
                ui.show_all_contacts(search.read_json(jsonFilename))
        # Изменение контакта
        elif punct_menu == 4:
            if check.check_directory():
                all_contacts = search.read_json(jsonFilename)
                found_contacts = search.search_contact(all_contacts)
                data = modify.modify_contact(found_contacts, all_contacts)
                modify.write_json_full(data)
        # Удаление контакта
        elif punct_menu == 5:
            if check.check_directory():
                all_contacts = search.read_json(jsonFilename)
                found_contacts = search.search_contact(all_contacts)
                data = delete.delete_contact(found_contacts, all_contacts)
                modify.write_json_full(data)
        # Экспорт
        elif punct_menu == 6:
            if check.check_directory():
                modol_export.export()
        elif punct_menu == 7:
            modol_import.import_file()
        # Завершение работы
        else:
            print(Fore.YELLOW + 'Работа со справочников закончена' + Style.RESET_ALL)
            break

# main_func()
