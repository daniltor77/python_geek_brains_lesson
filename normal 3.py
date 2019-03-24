from random import randint
from math import sqrt

listIn=[]
dimen=int(input('Введите длину списка = ')) 
num=0
while num<dimen:
	listIn.append(randint(-100,100))
	num+=1

print (listIn)
input ()