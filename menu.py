# импорт необходимых библиотек
from colorama import Fore, Back, Style


def main_menu():
    print(Fore.BLACK + Back.GREEN +
          'Приветствуем Вас в нашем справочнике' + Style.RESET_ALL)
    print(Fore.YELLOW+'Наш справочник поддерживает следующие возможности: ' + Style.RESET_ALL)
    print('1. Записать контакт.\n'
          '2. Найти контакт\n'
          '3  Показать все контакты\n'
          '4  Изменить контакт\n'
          '5. Удалить контакт\n'
          '6. Экспорт контактов\n'
          '7. Импорт контактов\n'
          '8. Выход из программы')
    

if __name__ == '__main__': 
    main_menu()
