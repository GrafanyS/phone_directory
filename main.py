# импорт необходимых библиотек
from colorama import Fore, Back, Style
import check
import controller


def main() -> object:
    print(Back.BLUE + 'Приветствуем Вас в нашем справочнике' + Style.RESET_ALL)
    print('Наш справочник поддерживает следующие возможности:\n'
          '1. Записать контакт.\n'
          '2. Найти контакт\n'
          '3. Показать все контакты\n'
          '4. Экспорт контактов\n'
          '5. Импорт контактов\n'
          '6. Выход из программы')

if __name__ == '__main__':
    main()
