def my_round(number, ndigits):
        ndigits+=1
        lastnumb=int(number*10**ndigits)
        if (lastnumb%10)>=5:
                output=lastnumb - lastnumb%10
                output=output+10
        else:
                output=lastnumb - lastnumb%10
        output=output/10**ndigits
        return (output)

n=float(input("enter numder: "))
nd=int(input("enter ndigits: "))
print(my_round(n,nd))


