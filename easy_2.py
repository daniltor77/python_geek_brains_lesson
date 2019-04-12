class trap:
    def __init__(self, pointA, pointB, pointC, pointD):
        self.Xa=pointA[0]
        self.Xb=pointB[0]
        self.Xc=pointC[0]
        self.Xd=pointD[0]
        self.Ya=pointA[1]
        self.Yb=pointB[1]
        self.Yc=pointC[1]
        self.Yd=pointD[1]

    def trapSqure (self):
        import math
        Xa=self.Xa
        Xb=self.Xb
        Xc=self.Xc
        Xd=self.Xd
        Ya=self.Ya
        Yb=self.Yb
        Yc=self.Yc
        Yd=self.Yd
        a=math.sqrt((Xb-Xa)**2+(Yb-Ya)**2)
        b=math.sqrt((Xc-Xb)**2+(Yc-Yb)**2)
        c=math.sqrt((Xd-Xc)**2+(Yd-Yc)**2)
        d=math.sqrt((Xa-Xd)**2+(Ya-Yd)**2)
        Sabcd=((a+b)/2)*math.sqrt(c**2-(((b-a)**2+c**2-d**2)/(2*(b-a))))
        return (Sabcd)

    def traplength (self):
        import math
        Xa=self.Xa
        Xb=self.Xb
        Xc=self.Xc
        Xd=self.Xd
        Ya=self.Ya
        Yb=self.Yb
        Yc=self.Yc
        Yd=self.Yd
        a=math.sqrt((Xb-Xa)**2+(Yb-Ya)**2)
        b=math.sqrt((Xc-Xb)**2+(Yc-Yb)**2)
        c=math.sqrt((Xd-Xc)**2+(Yd-Yc)**2)
        d=math.sqrt((Xa-Xd)**2+(Ya-Yd)**2)
        return ([a,b,c,d])

    def traperim (self):
        import math
        Xa=self.Xa
        Xb=self.Xb
        Xc=self.Xc
        Xd=self.Xd
        Ya=self.Ya
        Yb=self.Yb
        Yc=self.Yc
        Yd=self.Yd
        a=math.sqrt((Xb-Xa)**2+(Yb-Ya)**2)
        b=math.sqrt((Xc-Xb)**2+(Yc-Yb)**2)
        c=math.sqrt((Xd-Xc)**2+(Yb-Yc)**2)
        d=math.sqrt((Xa-Xd)**2+(Ya-Yd)**2)
        return (a+b+c+d)


student1=trap([3,4],[9,4],[8,6],[4,6])

print(student1.trapSqure(),' площадь')
print(student1.traperim(),' периметр')
print(student1.traplength(),' длины сторон')
