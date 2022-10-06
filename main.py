# импорт необходимых библиотек
import controller
from logger import main_logger


def main():
    controller.main_func()
    main_logger()

if __name__ == '__main__':
    main()
    main_logger()
