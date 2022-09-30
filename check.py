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