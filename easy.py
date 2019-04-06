# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("msdir -  создание директории dir_1 - dir_9")
    print("killsdir -  удаление директории dir_1 - dir_9")
    print("sdir -  показать содержание текущей директории")
    print("copth -  копирует файл программы")


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


def make_somedir():             #создаем директории от dir_1 до dir_2
    for i in range(1,9):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        dir_name='dir_{}'.format(i)
        try:
            os.mkdir(dir_path)
            print('директория {} создана'.format(dir_name))
        except FileExistsError:
            print('директория {} уже существует'.format(dir_name))


def kill_somedir():          #удаляем директории от dir_1 до dir_2
    for i in range(1,9):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        dir_name='dir_{}'.format(i)
        try:
            os.removedirs(dir_path)
            print('директория {} удалена'.format(dir_name))
        except FileExistsError:
            print('директория {} отсутствует'.format(dir_name))

        except FileNotFoundError:
            print('директория {} отсутствует'.format(dir_name))


def show_dir():             # Показываем содержание текущей директории
    dir_path = os.path.join(os.getcwd())
    try:
        print('Директория {}'.format(dir_path))
        print(os.listdir(dir_path))
    except FileExistsError:
        print('директория {} отсутствует'.format(dir_path))
    except FileNotFoundError:
        print('директория {} отсутствует'.format(dir_path))


def copy_that():            # Создаем копию текущего фаила
    dir_path = os.path.join(sys.argv[0])
    dir_path_copy=dir_path[:dir_path.find('.py')]+'-copy'+dir_path[dir_path.find('.py'):]
    try:
        shutil.copyfile(dir_path,dir_path_copy)
        print('Копия {} создана'.format(dir_path))
    except FileExistsError:
        print('Файл {} отсутствует'.format(dir_path))
    except FileNotFoundError:
        print('Файл {} отсутствует'.format(dir_path))



do = {
    "help": print_help,
    "mkdir": make_dir,
    "msdir": make_somedir,
    "killsdir": kill_somedir,
    "sdir": show_dir,
    "copth": copy_that
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

