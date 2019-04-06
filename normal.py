2
import efunct
import os
print('Приветствие, текущая директория = ', os.getcwd())

print("Выберете необходимую функцию:")
print("1. Перейти в папку")
print("2. Просмотреть содержимое текущей папки")
print("3. Удалить папку")
print("4. Создать папку")
num=input('Введите номер необходимого действия: ')

if num=='1':
    print(efunct.chedir(input('введите название директории: ')))
if num=='2':
    print(efunct.sdir())
if num=='3':
    print(efunct.killdir(input('введите название директории: ')))
if num=='4':
    print(efunct.mkdir(input('введите название директории: ')))

input()


