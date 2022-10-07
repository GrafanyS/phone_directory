# импорт необходимых библиотек
from concurrent.futures.thread import _worker
from datetime import datetime as dt
import logging
from db_link import *
# from loguru import logger


# import time


logger = logging.getLogger(__name__)


def create_contact(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Create new contact;\n')


def delete_contact(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Delete contact;\n')


def export_csv():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Export all contact in .csv;\n')


def export_json():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Export all contact in .json;\n')


def export_txt():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Export all contact in .txt\n')


def import_txt():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Import all contact from .txt\n')


def import_json():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Import all contact from .json\n')


def import_csv():
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time}; Import all contact from .csv;\n')


def change_con(data):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open(LOG, 'a', encoding='utf-8') as file:
        file.write(
            f'{time} : {data}; Contact change;new contact;\n')


def ValueError_logger():
    logging.basicConfig(
        filename=LOG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    logging.warning('ValueError')


def Started_logger():
    logging.basicConfig(
        filename=LOG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    logging.info('Started')
    

def Finished_logger():
    logging.basicConfig(
        filename=LOG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    logging.info('Finished')
    # logger=logging.getLogger()
    # logger.debug('Starting logger')
    # logger.add(LOG, format="format="{time:'%d-%b-%y %H:%M:%S'} | {level} | {message}", level="DEBUG", rotation="10KB", compression="zip")
    
    # logger.debug("Starting")
    # for _ in range(10):
    #     logger.debug("Произошло что-то (DEBUG)")
    #     logger.error("Произошло что-то (ERROR)")
    #     logger.info("Произошло что-то (INFO)")

# @logger.catch
# def logger_main():
#     ...   

# start = time.perf_counter()
# change_con(LOG)
# import_csv(LOG)
# finish = time.perf_counter()
# print(f"Преобразование строк успешно завершено в {finish - start:0.4f} секунд")
# info_logger()
