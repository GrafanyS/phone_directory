import create
import ui
import menu
import check
import search
import logger
import delete
import modol_export
import modol_import
import contact
from colorama import Fore, Back, Style


def main_func():
    while True:
        menu.main_menu()
        punct_menu = check.check_search_menu()

        if punct_menu == 1:
            dict_ph = ui.get_value()
            create.write_json(dict_ph)
            logger.create_contact(dict_ph)

        elif punct_menu == 2:
            if check.check_directory():
                menu.menu_for_search()
                punct_menu_search = check.check_search_menu()
                result_search = search.search_write_json(punct_menu_search)
                if len(result_search) != 0:
                    ui.show_contact(result_search)
                else:
                    print(
                        Fore.RED + 'Контакт с такими параметрами отсутствует.' + Style.RESET_ALL)
                if len(result_search) == 1:
                    punct_menu_act_contact = menu.action_with_contact()
                    if punct_menu_act_contact == 4:
                        exit()
                    elif punct_menu_act_contact == 3:
                        continue
                    elif punct_menu_act_contact == 2:
                        delete.delete_contact(result_search)
                        logger.delete_contact(result_search[0])
                    elif punct_menu_act_contact == 1:
                        contact.change_contact(result_search)
                        logger.change_con(result_search[0])

            else:
                continue

        elif punct_menu == 3:
            if check.check_directory():
                ui.show_all_contact()

        elif punct_menu == 4:
            modol_export.export_csv()
            logger.export_csv()

        elif punct_menu == 5:
            modol_import.import_csv()
            logger.import_csv()

        else:
            print("Спасибо за использования справочника. Ждем Вас снова")
            break


# main_func()
