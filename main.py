# from tkinter import *

# top = Tk()
# top.geometry("400x250")

# surname = Label(top, text="Surname", fg="blue").place(x=30, y=30)
# name = Label(top, text="Name", fg="blue").place(x=30, y=60)
# tel = Label(top, text="Tel", fg="blue").place(x=30, y=90)
# comment = Label(top, text="Description", fg="blue").place(x=30, y=120)
# e1 = Entry(top).place(x=120, y=30)
# e2 = Entry(top).place(x = 120, y = 60)
# e3 = Entry(top).place(x = 120, y = 90)
# e4 = Entry(top).place(x = 120, y = 120)
# submit = Button(top, text="Submit", fg="blue").place(x=120, y=150)
from colorama import Fore, Back, Style
import check


def main_menu():
    print(Back.BLUE + 'Приветствуем Вас в нашем справочнике' + Style.RESET_ALL)
    print('Наш справочник поддерживает следующие возможности:\n'
          '1. Записать контакт.\n'
          '2. Найти контакт\n'
          '3. Показать все контакты\n'
          '4. Экспорт контактов\n'
          '5. Импорт контактов\n'
          '6. Выход из программы')


if name == 'main':
    main_menu()