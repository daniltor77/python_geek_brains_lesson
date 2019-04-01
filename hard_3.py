# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

path=os.path.join('data','fruits.txt')
input_file=open(path,'r',encoding='UTF-8')

list_work=(list(filter(lambda x: x != '\n', input_file.readlines())))   #избавляемся от символов переноса строки в отдельныйх строках
for i in range(len(list_work)):             #избавляемся от символа переноса строки в конце строк
    list_work[i]=list_work[i].rstrip('\n')
list_work[0]=list_work[0].strip('\ufeff')


dic_out=dict.fromkeys((list(map(chr, range(ord('А'), ord('Я')+1)))),[])




for i in dic_out:    #Создаем словарь по алфавиту
    list_out=[]
    for j in range(len(list_work)):
        if list_work[j][0]==i:
            list_out.append(list_work[j])
        else:
            break
            out=j
    list_work=list_work[j:]
    dic_out[i]=list_out


for i in dic_out:
    file=open('fruits_{}.txt'.format(i),'w')
    file.write(str(dic_out[i]))
    file.close()


#print(dic_out)

input_file.close()
input()
