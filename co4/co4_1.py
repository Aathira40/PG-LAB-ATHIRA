class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print("area=",a)
        return(a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print("perimeter=",p)
        return(p)
p1=rectangle(4,2)
b=p1.area()
p1.perimeter()

p2=rectangle(5,2)
c=p2.area()
p2.perimeter()

if(b>c):
    print(b,"is greater")
else:
    print(c,"is greater")
