
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

path=os.path.join('data','workers.txt')
work=open(path,'r',encoding='UTF-8')

path=os.path.join('data','hours_of.txt')
hours=open(path,'r',encoding='UTF-8')

list_work=work.readlines()
list_hours=hours.readlines()

dic_hours={}

for i in range(1,len(list_hours)):          # Из фаила с количеством отработанных часов получаем словарь dic_hours (имя: часы)
    name_string = list_hours[i]
    name = name_string[:list_hours[i].rfind(' ')]
    hours_fact = int(name_string[list_hours[i].rfind(' ')+1:list_hours[i].rfind('/n')])
    name=name.strip(' ')
    name.split(' ')
    name=list(filter(len, name.split(' ')))
    name=name[0]+' '+name[1]
    dic_hours[name]=hours_fact



for i in range(1,len(list_work)):           #Читаем список сотрудников и по словарю отработки считаем сколько кому должны
    list_homejo = list(filter(len, list_work[i].split(' ')))
    name=list_homejo[0]+' '+list_homejo[1]                          #Имя сотрудника
    pay=int(list_homejo[2])                                              #Зарплата
    norm_work=int(list_homejo[4][:list_homejo[4].find('/n')])                #Норма часов? ,без символа переноса строки

    if norm_work>=dic_hours[name]:
        pay=((pay/norm_work)*dic_hours[name])
        print('{:.<20}{:.>20.2f}'.format(name,pay))
    else:
        pay=pay+(dic_hours[name]-norm_work)*(pay/norm_work)
        print('{:.<20}{:.>20.2f}'.format(name,pay))



work.close()

hours.close()
input()
