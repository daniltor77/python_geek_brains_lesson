
def delitel(n,m):   # Находим общий делитель
    if n<m:
        max=m
        min=n
    else:
        max=n
        min=m
    for i in range(2,max):
        if (max%i)==0 and (min%i)==0:
            return(i)
            break
    return(0)

str1=input("Введите простые дроби для склыдывания, в формате. 5/6 + 4/7: ")

n1=int(str1[:str1.find('/')])
n2=int(str1[str1.find('/')+1:str1.find('+')])
str1=str1[str1.find('+')+1:]
n3=int(str1[:str1.find('/')])
n4=int(str1[str1.find('/')+1:])

fac1=n4     # Множитель первой дроби
fac2=n2     # Множитель второй дроби
n1=n1*fac1
n2=n2*fac1
n3=n3*fac2
deno=n1+n3  # Знаменатель
numer=n2    # Числитель
integ=deno//numer
deno=deno%numer

num_del=delitel(deno,numer)

if num_del!=0:
    deno=int(deno/num_del)
    numer=int(numer/num_del)

if deno==0:
    output=integ
else:
    output=str(integ)+' '+str(deno)+'/'+str(numer)

print(output)




# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
