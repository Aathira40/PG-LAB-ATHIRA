from graphics import rectangle
from graphics import circle
l=int(input("enter length"))
b=int(input("enter breadth"))
print("perimeter=",rectangle.perimeter(l,b))
print("area=",rectangle.area(l,b))
print()
r=int(input("enter radius"))
print("perimeter=",circle.perimeter(r))
print("area=",circle.area(r))
