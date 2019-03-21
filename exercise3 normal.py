
import math
print ('Решим уравнение вида ax^2+bx+c=0')
a=int(input('Введите  a='))
b=int(input('Введите  b='))
c=int(input('Введите  c='))
D=(b**2)-4*a*c
x1=((-b)+math.sqrt(D))/(2*a)
x2=((-b)-math.sqrt(D))/(2*a)
print ('x1= ',x1,' x2= ',x2)
input()