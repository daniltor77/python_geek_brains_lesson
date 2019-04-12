class triangle:
    def __init__(self, pointA, pointB, pointC):
        self.pointA=pointA
        self.pointB=pointB
        self.pointC=pointC
    def triSqure (self):
        Xa=self.pointA[0]
        Xb=self.pointB[0]
        Xc=self.pointC[0]
        Ya=self.pointA[1]
        Yb=self.pointB[1]
        Yc=self.pointC[1]
        return (((Xb-Xa)*(Yc-Ya)-(Xc-Xa)*(Yb-Ya))/2)
    def triheight (self):
        import math
        Xa=self.pointA[0]
        Xb=self.pointB[0]
        Xc=self.pointC[0]
        Ya=self.pointA[1]
        Yb=self.pointB[1]
        Yc=self.pointC[1]
        return (((Xb-Xa)*(Yc-Ya)-(Xc-Xa)*(Yb-Ya))/(math.sqrt((Xb-Xa)**2+(Yb-Ya)**2)))
    def triperim (self):
        import math
        Xa=self.pointA[0]
        Xb=self.pointB[0]
        Xc=self.pointC[0]
        Ya=self.pointA[1]
        Yb=self.pointB[1]
        Yc=self.pointC[1]
        a=math.sqrt((Xb-Xa)**2+(Yb-Ya)**2)
        d=math.sqrt((Xc-Xa)**2+(Yc-Ya)**2)
        b=math.sqrt((Xc-Xb)**2+(Yc-Yb)**2)
        return (a+b+d)


student1=triangle([3,4],[6,4],[4,6])

print(student1.triSqure(),' площадь')
print(student1.triperim(),' периметр')
print(student1.triheight(),' высота')
