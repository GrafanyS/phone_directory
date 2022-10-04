# импорт необходимых библиотек
from colorama import Fore, Back, Style
import check


def main_menu():
    print(Back.BLUE + 'Приветствуем Вас в нашем справочнике'+Style.RESET_ALL)
    print('Наш справочник поддерживает следующие возможности:\n'
          '1. Записать контакт.\n'
          '2. Найти контакт\n'
          '3. Показать все контакты\n'
          '4. Экспорт контактов\n'
          '5. Импорт контактов\n'
          '6. Выход из программы')
 

def menu_for_search():
    print('Возможен поиск по разным полям:\n'
          '1. По фамилии')


def action_with_contact():
    print('Что вы хотите сделать с контактом?:\n'
          '1. Изменить\n'
          '2. Удалить\n'
          '3. Выйти в основное меню\n'
          '4. Выйти из программы')

    return check.check_menu_act_contact()

# def menu_main():
#     main_menu()
#     menu_for_search()
#     action_with_contact()


# if __name__ == '__main__': 
#     main_menu()
