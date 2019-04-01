def sort_to_max(m):
	output=[]
	num=0
	while len(m)!=0:
		min=m[0]
		outcicl=len(m)
		i=0
		num=0
		while outcicl>i:
			if m[i]<min:
				min=m[i]
				num=i
			i+=1
		output.append(m[num])
		m.remove(m[num])
	return(output)


m=[2,10,-12,2.5,20,-11,4,4,0]

print(sort_to_max(m))
input()

