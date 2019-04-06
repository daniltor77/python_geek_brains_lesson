# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cd <dir_name> - смена текущей директории ")
    print("rm <fail_name> -  удаление фаила")
    print("ls -  показать содержание текущей директории")
    print("cp <fail_name> -  копирует  файл")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def kill_f():          #удаляем директории от dir_1 до dir_2
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        if 'y'==input('Realy? y/n').lower():
            os.remove(dir_path)
            print('Файл {} удален'.format(dir_name))
        else:
            print('good boy')
    except FileExistsError:
        print('Файл {} отсутствует'.format(dir_name))

    except FileNotFoundError:
        print('Файл {} отсутствует'.format(dir_name))


def show_dir():             # Показываем содержание текущей директории
    dir_path = os.path.join(os.getcwd())
    try:
        print('Директория {}'.format(dir_path))
        print(os.listdir(dir_path))
    except FileExistsError:
        print('директория {} отсутствует'.format(dir_path))
    except FileNotFoundError:
        print('директория {} отсутствует'.format(dir_path))


def copy():            # Создаем копию текущего фаила
    dir_path = os.path.join(os.getcwd(),dir_name)
    dir_path_copy=dir_path[:dir_path.find('.py')]+'-copy'+dir_path[dir_path.find('.py'):]
    try:
        shutil.copyfile(dir_path,dir_path_copy)
        print('Копия {} создана'.format(dir_path))
    except FileExistsError:
        print('Файл {} отсутствует'.format(dir_path))
    except FileNotFoundError:
        print('Файл {} отсутствует'.format(dir_path))


def chedir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print('текущая директория {}'.format(dir_path))
    except FileExistsError:
        print('невозможно перейти в директорию {}'.format(dir_name))






do = {
    "help": print_help,
    "mkdir": make_dir,
    "cd": chedir,
    "rm": kill_f,
    "ls": show_dir,
    "cp": copy
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

