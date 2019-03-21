

num=int(input('Введите число '))
max=0
while (num//10)>0:
	cel=num-(num//10)*10
	if cel>max:
		max=cel
	num=num//10
if num>max:
	max=cel
print('Максимальное число = ',max)
input('end')