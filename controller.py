import create
import ui
import menu
import check
import search
import logger
import delete
import modol_export
#  import modol_import
import modify


def main_func():
    menu.main_menu()
    while True:
        punct_menu = check.check_main_menu()
        if punct_menu == 1:
            dict_ph = ui.gen_person()
            create.write_json(dict_ph)
        elif punct_menu == 2:
            if check.check_directory():
                all_contacts = search.read_json('phone_directory.json')
                try:
                    found_contacts = search.search_contact(all_contacts)
                    if found_contacts != []: 
                        futher_action = input('Что вы хотите сделать с найденным контактом: 1 - удалить, 2 - изменить, 3 - ничего: ')
                        if futher_action == '1': 
                            delete.delete_contact(found_contacts, all_contacts)
                        elif futher_action == '2':
                            modify.modify_contact(found_contacts, all_contacts)
                        else:
                            menu.main_menu()
                            punct_menu = check.check_main_menu()
                except:
                    print('Такого контакта нет')
        elif punct_menu == 3:           #Вывод всех контактов
            if check.check_directory(): ui.show_all_contacts(search.read_json('phone_directory.json'))
        elif punct_menu == 4:           #Изменение контакта
            if check.check_directory(): 
                all_contacts = search.read_json('phone_directory.json')
                found_contacts = search.search_contact(all_contacts)
                modify.modify_contact(found_contacts, all_contacts)
                modify.write_json_full(all_contacts)
        elif punct_menu == 5:           #Удаление контакта
            if check.check_directory(): 
                all_contacts = search.read_json('phone_directory.json')
                found_contacts = search.search_contact(all_contacts)
                delete.delete_contact(found_contacts, all_contacts)
                modify.write_json_full(all_contacts)
        elif punct_menu == 6:           #Экспорт
            if check.check_directory(): 
                modol_export.export()
        else:
            print('Работа со справочников закончена')
            break
                
        

