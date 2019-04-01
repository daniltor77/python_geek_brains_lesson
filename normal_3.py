def my_filter(func,list_m):
	output=[]
	for i in range(len(m)):
		if func(list_m[i]):
			output.append(list_m[i])
	return (output)




m=['2','','-12','2.5','','-11','4','','0']

print(my_filter(len,m))

k=lambda x: x>5

m=[2,10,-10,8,2,0,14]

print(my_filter(k,m))

input()
