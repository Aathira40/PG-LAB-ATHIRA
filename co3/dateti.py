import datetime
t=datetime.time(12,54,20,11)
print(t)
print("hour",t.hour)
print("minute",t.minute)
print("seond",t.second)
print("microsecond",t.microsecond)
print()
d=datetime.date.today()
print(d)
print("year",d.year)
print("month",d.month)
print("day",d.day)
print()
d1=datetime.date.today()
print(d1)
td=datetime.timedelta(days=3)
print(td)
d2=d1+td
print(d2)
print()
dt=datetime.datetime.combine(d,t)
print(dt)
