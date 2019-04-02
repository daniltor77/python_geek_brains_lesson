

inp=input("Введите уравнение в виде y=kx+b: ")
x=float(input("Ведите x: "))

k=int(inp[inp.find('=')+1:inp.find('x')])
b=float(inp[inp.find('+')+1:])

print ('y = ',k*x+b)

input()