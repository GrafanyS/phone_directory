from colorama import Fore, Back, Style, Blue

print(Fore.YELLOW + 'some red text')
print(Back.BLACK + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print(Blue.YELLOW+'Такого пункта меню нет! Попробуйте снова.')
def check_main_menu():
    while True:
        try:
            num = int(input('Введите номер пункта, который хотите выполнить: '))
            if 0 <= num <= 3: break
            else:
                print('Такого пункта меню нет!')
                print("\033[31m {}\033[0m".format('Такого пункта меню нет! Попробуйте снова.'))
                continue
        except ValueError:
            print("\033[31m {}\033[0m".format('Вы ввели некорректное число! Попробуйте снова.'))

    return num