from colorama import Fore, Back, Style


def main():
    print(Style.DIM + 'and in dim text')
    print(Fore.RED + 'some red text')
    print(Back.WHITE + 'and with a green background' + Fore.BLUE + 'and with a blue background')
    print(Back.GREEN + 'and with a blue background'+Style.RESET_ALL)
    print(Style.DIM + 'and in dim text')
    print(Fore.BLUE + 'and with a green background' +
          Fore.GREEN + 'and with a blue background'+Style.RESET_ALL)
    print(Style.DIM + 'and in dim text')
    # print(Style.RESET_ALL)
    print('back to normal now')
    print(Fore.RED+""+Back.WHITE+"Сделай что надо"+Style.RESET_ALL)
    print(Back.GREEN + 'Привет'+Style.RESET_ALL)
    print(Style.DIM + 'and in dim text')
    
if __name__ == '__main__':
    main()
