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


def main_func():
    while True:
        menu.main_menu()
        unit_menu = check.check_main_menu()

        if unit_menu == 1:
            dict_ph = ui.get_value()
            create.create(dict_ph)
            logger.create_contact(dict_ph)

        elif unit_menu == 2:
            if check.check_directory():
                menu.menu_for_search()
                unit_menu_search = check.check_search_menu()
                result_search = search.search(unit_menu_search)
                if len(result_search) != 0:
                    ui.show_contact(result_search)
                else:
                    print('Контакт с такими параметрами отсутствует.')
                if len(result_search) == 1:
                    unit_menu_act_contact = menu.action_with_contact()
                    if unit_menu_act_contact == 4:
                        exit()
                    if unit_menu_act_contact == 3:
                        continue
                    if unit_menu_act_contact == 2:
                        delete.delete_contact(result_search)
                        logger.delete_contact(result_search[0])
                    if unit_menu_act_contact == 1:
                        contact.change_contact(result_search)
                        logger.change_con(result_search[0])

            else:
                continue

        elif unit_menu == 3:
            if check.check_directory():
                ui.show_all_contact()

        elif unit_menu == 4:
            modol_export.export()
            logger.export_csv()

        elif unit_menu == 5:
            modol_import.import_csv()
            logger.import_csv()

        else:
            print("Спасибо за использования справочника. Ждем Вас снова")
            break
