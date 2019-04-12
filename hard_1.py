import os, re

class worker_name:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        self.fullname=surname+' '+name

class works_hours(worker_name):
    def __init__(self,name,surname,hours):
        super().__init__(name, surname)
        self.hours=int(hours)
        self.works_d={self.fullname:self.hours}

class Workers(worker_name):
    def __init__(self, name, surname, money, special, hours):
        super().__init__(name,surname)
        self.money=int(money)
        self.hours=int(hours)
        self.MPH=self.money/self.hours



path=os.path.join('data','workers.txt')
work=open(path,'r',encoding='UTF-8')

path=os.path.join('data','hours_of.txt')
hours=open(path,'r',encoding='UTF-8')

list_work=work.readlines()
list_hours=hours.readlines()
lst_out=[]

for i in range(1,len(list_hours)):

    actl_hours=list_hours[i].rstrip('\n')
    work1=works_hours(re.findall(r"\s*(\S+)\s*",actl_hours)[0],re.findall(r"\s*(\S+)\s*",actl_hours)[1],re.findall(r"\s*(\S+)\s*",actl_hours)[2],)
    lst_out.append(work1)


for i in range(1,len(list_work)):

    actl_hours=list_work[i].rstrip('\n')
    work1=Workers(re.findall(r"\s*(\S+)\s*",actl_hours)[0],re.findall(r"\s*(\S+)\s*",actl_hours)[1],re.findall(r"\s*(\S+)\s*",actl_hours)[2],
                      re.findall(r"\s*(\S+)\s*",actl_hours)[3],re.findall(r"\s*(\S+)\s*",actl_hours)[4])

    for obj in lst_out:
        if obj.fullname==work1.fullname:
            if work1.hours>=obj.hours:
                pay=((work1.MPH)*obj.hours)
                print('{:.<20}{:.>20.2f}'.format(work1.fullname,pay))
            else:
                pay=work1.money+(obj.hours-work1.hours)*(work1.MPH)
                print('{:.<20}{:.>20.2f}'.format(work1.fullname,pay))





work.close()

hours.close()
input()
