from random import randint
from math import sqrt

listIn=[]
dimen=int(input('Введите длину списка = ')) 

while len(listIn)<dimen:    # генерирум список из случайных элементов
	listIn.append(randint(-100,100))
print ('Исходный список: ',listIn)
listA=[]


for i in range(len(listIn)):		#создаем список повторяющихся элементов
	try:
		k=listIn.index(listIn[i],i+1,-1)
	except ValueError:
		continue

	listA.append(listIn[k])


for i in listA:					# Из исходного списка удаляем элементы которые есть в списке с повторами 
	while True:
		try:
			listIn.remove(i)
		except ValueError:
			break




print ('Список повторяющихся элементов: ',listA)

print ('Список неповторяющихся элементов: ',listIn)

input ()