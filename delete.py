import logger
from colorama import Fore, Back, Style


def delete_contact(sorted_data, full_data):
    """Функция находит и удаляет заданную запись с контактом"""
    temp = []
    if len(sorted_data) > 1:
        for item in sorted_data:
            temp.append(item["id"])
        # Здесь нужно добавить проверку, что пользователь ввел только индекс из списка
        index_for_delete = int(
            input(f'Введите id контакта из данного списка {temp}: '))
        if index_for_delete in temp:
            # Подтверждение, что пользователь действительно хочет удалить данный контакт
            confirm = input(Back.RED + 'Вы уверены, что хотите удалить данный контакт? Да/Нет: ' + Style.RESET_ALL)
            if confirm.capitalize() == 'Да':  # Ввод подтверждения
                for item in full_data:
                    if index_for_delete == item["id"]:
                        logger.delete_contact(item)
                        # Если Да, то удаляем контакт из базы
                        full_data.remove(item)
                print(Back.RED + 'Контакт удален' + Style.RESET_ALL)
                return full_data
            else:  # Иначе, возвращаемся в главное меню
                print(Fore.BLUE + 'Возврат в главное меню' + Style.RESET_ALL)
                return False
        else:
            print(Fore.RED + "Вы ввели неверный номер" + Style.RESET_ALL)
            return False
    elif len(sorted_data) == 1:
        # Подтверждение, что пользователь действительно хочет удалить данный контакт
        confirm = input(Back.RED + 'Вы уверены, что хотите удалить данный контакт? Да/Нет: ' + Style.RESET_ALL)
        if confirm.capitalize() == 'Да':  # Ввод подтверждения
            for item in full_data:
                if sorted_data[0]["id"] == item["id"]:
                    logger.delete_contact(item)
                    # Если Да, то удаляем контакт из базы
                    full_data.remove(item)
            print(Back.RED + 'Контакт удален' + Style.RESET_ALL)
            return full_data
        else:
            print(Back.YELLOW + 'Возврат в главное меню' + Style.RESET_ALL)
            return False
    else:
        print(Back.YELLOW + 'Возврат в главное меню' + Style.RESET_ALL)
        return False
