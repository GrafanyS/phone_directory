import json
import check


def change_contact(data):
    with open('data_base.json', 'r') as f:
        phone_dir = json.load(f)

    for i in range(len(phone_dir)):
        if phone_dir[i] == data[0]:
            print('Что вы хотите изменить:\n'
                  '1. Фамилию.\n'
                  '2. Имя\n'
                  '3. Номер телефона\n'
                  '4. Описание')
            num = check.check_menu_ch_con()
            if num == 1:
                phone_dir.pop(i)
                data[0]['surname'] = input('Введите новую фамилию: ')
                phone_dir.append(data[0])

            if num == 2:
                phone_dir.pop(i)
                data[1]['name'] = input('Введите новое имя: ')
                phone_dir.append(data[1])

            if num == 3:
                phone_dir.pop(i)
                data[2]['tel'] = input('Введите телефон: ')
                phone_dir.append(data[2])

            if num == 4:
                phone_dir.pop(i)
                data[3]['comment'] = input('Введите новую фамилию: ')
                phone_dir.append(data[3])

    with open('data_base.json', 'w') as file:
        json.dump(phone_dir, file, indent=2)
    print('\033[30m\033[42m\033[4m {}\033[0m'.format('Ваш контакт успешно изменен. Переводим '
                                                     'вас в начало меню'))
