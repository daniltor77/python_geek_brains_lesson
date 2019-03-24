import math

#n=int(input('Введите номер комнаты: '))
n=int(input())

k=1  # размерность массива
i=1  # номер старшего элемента в массиве

while i<n:
	k=k+1
	i=i+k**2


numberKstr=int(((k*(k+1))/2)) 		 # номер верхней строки массива k*k
narray=(n-(i-k**2))  		         # номер элемента в массиве

strArr=math.ceil(narray/k)		  		 # номер строки в массиве
colArr=(narray-(strArr-1)*k)              	 # порядковый номер слева на этаже
numberstr=int((((k-1)*k)/2))+strArr	     # абсолютный номер строки

#print('i= ', i,' k= ',k,' Kstring= ',numberKstr,' strArr= ',strArr,' narray',narray)
#print('номер строки = ',numberstr,' порядковый номер слева на этаже = ',colArr)
print(numberstr,' ',colArr)
input ()
