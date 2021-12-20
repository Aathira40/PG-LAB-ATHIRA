class person:
    varb=10
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name,"age:",self.age)
p1=person("john",36)
p2=person("dev",35)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
p1.display()
p2.display()

print(person.varb)
print(p1.varb)
person.varb=person.varb+2
p1.varb=p1.varb+3
print(p1.varb,person.varb)

if(p1.age>p2.age):
    print(p1.name,"is elder")
else:
    print(p2.name,"is elder")
    
