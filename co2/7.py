str=input("enter a string")
print("entered string is",str)
if(str.endswith ("ing")):
    str=str+"ly"
else:
    str=str+"ing"
print("the new str is",str)

