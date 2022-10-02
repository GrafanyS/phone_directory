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

# top.mainloop()
from menu import *

"""
Внимание! Некоторые функции используют операторы сопоставления (match/case)
Python версии 3.9 и ниже не поддерживают операторы сопоставления
"""


def main():
    menu()


if __name__ == '__main__':
    main()
