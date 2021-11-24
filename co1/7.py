a=[1,2,3,4,5]
b=[1,8,7,5,6]
s=int(0)
z=int(0)
l1=len(a)
l2=len(b)
if(l1==l2):
    print("they are of same length")
else:
    print("they are not")
for i in range(0,len(a) and len(b)):
        s=s+a[i]
        z=z+b[i]
if(s==z):
            print("it sums to same value")
else:
          print("different value")
l=[]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(b[j]==a[i]):
            l.append(a[i] and b[j])
        else:   
            print(l)
            

