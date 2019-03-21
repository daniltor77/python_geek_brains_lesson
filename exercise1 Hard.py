num=int(input('Начнем с этого = '))
while True:
	if (num==num**2)and(num==num*2)and(num>999999):
		break
	num=num+1
	print(num)
print("Вот оно",num)
input()
