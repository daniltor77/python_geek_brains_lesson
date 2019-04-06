# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys


def help():
    print(".help() - получение справки")
    print(".mkdir(<dir_name>) - создание директории")
    print(".sdir() -  показать содержание текущей директории")
    print(".killdir(<dir_name>) -  удаление директории")
    print(".chedir(<dir_name>) -  смена текущей директории")


def mkdir(dir_name):
    if not dir_name:
        return("Необходимо указать имя директории вторым параметром")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        return ('директория {} создана'.format(dir_name))
    except FileExistsError:
        return ('директория {} уже существует'.format(dir_name))





def killdir(dir_name):          #удаляем директории от dir_1 до dir_2
        dir_path = os.path.join(os.getcwd(),dir_name)
        try:
            os.removedirs(dir_path)
            return('директория {} удалена'.format(dir_name))
        except FileExistsError:
            return('директория {} отсутствует'.format(dir_name))

        except FileNotFoundError:
            return('директория {} отсутствует'.format(dir_name))


def sdir():             # Показываем содержание текущей директории
    dir_path = os.path.join(os.getcwd())
    try:
        return ('Директория {}, содержит {}'.format(dir_path,os.listdir(dir_path)))
    except FileExistsError:
        return ('директория {} отсутствует'.format(dir_path))
    except FileNotFoundError:
        return ('директория {} отсутствует'.format(dir_path))



