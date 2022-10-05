import json
from colorama import Fore, Back, Style
import db_link


def write_json(person_dict):
    try:
        with open(db_link.jsonFilename, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = []

    # person_dict['id'] = len(data)
    data.append(person_dict)

    with open(db_link.jsonFilename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(Fore.BLUE + 'Контакт успешно добавлен\n' + Style.RESET_ALL)



if __name__ == '__main__':    
    write_json()
