from random import randint
from math import sqrt

listIn=[]
dimen=int(input('Введите длину списка = ')) 
num=0
while num<dimen:
	listIn.append(randint(-100,100))
	num+=1
n=0
print (listIn)
while len(listIn)>n:
	print(listIn[n],' ',n)
	if listIn[n]<0:
		print('negative')
		listIn.pop(n)
		n-=1
	elif (sqrt(listIn[n])%1)!=0:
		print('not coren')
		listIn.pop(n)
		n-=1
	else: 
		listIn.insert(n,int(sqrt(listIn.pop(n))))
	n+=1
print (listIn)
input()
