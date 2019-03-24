inputList=['яблоко','банан','киви','арбуз']
"""
max=0
for i in inputList:
	if len(i)>max:
		max=len(i)
num=1

for i in inputList:
	print('{}. {:>max}'.format(num,i))
	num+=1
input()

почемуто мтод .format не понимает переменную max 
ему нужно обязательно число, возможно это както решить?
"""
num=1
for i in inputList:
	print('{}. {:>6}'.format(num,i))
	num+=1
input()