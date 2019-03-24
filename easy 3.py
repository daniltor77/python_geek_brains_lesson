from random import randint
listIn=[]
dimen=int(input('Введите длину списка = ')) 
i=0
while i<=dimen:
	i+=1
	listIn.append(randint(0,100))

n=0
print (listIn)

for memb in listIn:
	if (memb%2)==0:
		listIn.pop(n)
		listIn.insert(n,memb/4)
	else:
		listIn.pop(n)
		listIn.insert(n,memb*2)
	n+=1

print (listIn)
input()