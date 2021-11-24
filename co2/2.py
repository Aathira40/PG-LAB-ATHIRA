n=int(input("enter a limit"))
a=0
b=1
c=0
i=0
print("fibonacci series")
while(i<=n):
    print(c,end=" ")
    i=i+1
    a=b
    b=c
    c=a+b
    
