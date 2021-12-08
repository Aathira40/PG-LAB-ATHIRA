import operator
d={'anu':10,'manu':20,'sana':23,'rahul':'13'}
print("the original",d)
sdk=(d.items(),key=operator.itemgetter(1))
print('dictionary in ascending',sdk)
sdk=(d.items(),key=operator.itemgetter(1),reverse=True)
print('dictionary in descending',sdk)
