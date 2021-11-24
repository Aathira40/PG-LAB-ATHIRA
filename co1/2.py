c=int(input("enter current year"))
f=int(input("enter final year"))
if(c<f):
    print("leap year:",end=" ")
for i in range(c,f):
    if(i%4==0 and i%100!=0):   
        print(i,end=" ")
