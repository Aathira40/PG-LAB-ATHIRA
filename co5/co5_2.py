fn = open('fil1.txt', 'r')
fn1 = open('fil2.txt', 'w')
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
    if(i%2!=0):
        fn1.write(cont[i])
    else:
        pass 
fn1.close()
fn1 = open('fil2.txt', 'r')
fn=open('fil1.txt','r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()