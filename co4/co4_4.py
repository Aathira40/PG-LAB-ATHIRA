class time:
 def __init__(self,hour,minute,second):
  self.__hour=hour
  self.__minute=minute
  self.__second=second

 def __add__(self,second):
   print("\nHour:",self.__hour + second.__hour)
   print("Minutes:",self.__minute + second.__minute)
   print("Seconds:",self.__second + second.__second)
 
hour1=int(input("Enter the hour:"))
minute1=int(input("Enter the minutes:"))
sec1=int(input("Enter the second:"))

obj1=time(hour1,minute1,sec1)

hour2=int(input("\nEnter the hour:"))
minute2=int(input("Enter the minutes:"))
sec2=int(input("Enter the second:"))

obj2=time(hour2,minute2,sec2)

obj1 + obj2