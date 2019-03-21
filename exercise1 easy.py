
num=int(input('Введите число '))
while (num//10)>0:
	print (num-(num//10)*10)
	num=num//10
print (num)
input('end')