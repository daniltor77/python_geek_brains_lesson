import random, os

# выдаем по элементно список последовательных чисел, в случайном порядке
class randgen:
    def __init__(self,start,limit):
        self.limit=limit
        self.counter=0
        self.start=start
        self.randlist=[i for i in range(start,limit+1)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter<len(self.randlist):
            self.out=self.randlist.pop(random.randint(self.start,len(self.randlist)-1))
            return self.out
        else:
            raise StopIteration

# получаем сортированный список случайных числел от star до end заданной длины
def sortlist (start,end,length):
    s_list=randgen(start , end)
    list_number=[next(s_list) for _ in range(length)]
    list_number.sort()
    return (list_number)

# удаляем из списка жертва элемениы списка маньяк
def dellist (jertv,maniak):
    maniak.reverse()
    for i in maniak:
        jertv.pop(i)
    return jertv

# создаем случайную карточку
def give_card ():
    cardrnd = [['' for _ in range(9)]for _ in range(4)]

    chei=0
    list_number=sortlist(1,90,15)  # (список №1) список всех чисел в карточке
    for i in cardrnd:
        number_cel = sortlist(0,8,5)    # (список №2) номера клеток в которые мы впишем числа в строке
        number_listnumber = sortlist(0,len(list_number)-1,5)      # номера чисел из списка №1 которые мы запишем в строку на позиции списка №2
        chej=0

        for j in number_cel:
            cardrnd[chei][j]=list_number[number_listnumber[chej]]
            chej+=1
        chei+=1

        list_number=dellist(list_number,number_listnumber)
        if len(list_number)==0:
            break
    return cardrnd

# коректная печать карточки
def printList(card):
    for i in range(len(card)):
        string=''
        for j in range(len(card[i])):
            if card[i][j]=='':
                string=string+'   '
            else:
                if len(str(card[i][j]))==1:
                    string=string+str(card[i][j])+'  '
                else:
                    string=string+str(card[i][j])+' '
        print(string)

card1=give_card()
card2=give_card()


userpoint=0
gamepoint=0
s_barrel=randgen(1,90)

clear = lambda: os.system('cls')
clear()
for i in range(1,90):
    endgame=True
    barrel=next(s_barrel)
    print('Новый бочонок: {} (осталось {})'.format(barrel,90-i))
    print('{:*^26}'.format('Ваша карточка'))
    printList(card1)
    print('{:*^26}'.format('Карточка компьютера'))
    printList(card2)
    answer=(input('Зачеркнуть цифру? (y/n)')).lower()


    for j in range(len(card1)):
        for k in range(len(card1[j])):
            if barrel==card1[j][k]:
                card1[j][k]='-'
                endgame=False
                userpoint+=1

    if answer=='y' and endgame:
        print('Вы проиграли!')
        break

    if answer=='n' and not(endgame):
        print('Вы проиграли!')
        break

    for j in range(len(card2)):
        for k in range(len(card2[j])):
            if barrel==card2[j][k]:
                card2[j][k]='-'
                gamepoint+=1

    if gamepoint>=15:
        print('Компьютер победил!')
        break
    if userpoint>=15:
        print('Вы выйграли!')
        break

    clear()

input()
