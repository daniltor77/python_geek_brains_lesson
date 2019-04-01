def fibonacci(n,m):
	fibon=[1,1]
	for i in range(1,m+1):
		fibon.append(fibon[i-1]+fibon[i])
	return (fibon[n-1:m])

m=int(input('enter m: '))
n=int(input('enter n: '))
print(fibonacci(n,m))
input()

