from datetime import datetime, timedelta

d = datetime(2024, 11, 7, 7)
print (d)

t1 = timedelta(days=1, hours=10)
t2 = timedelta(hours=1, minutes=30)
print(t1)
print(t2)
print(d+t2)
print(t2+d)
d = d + t1
print(d)
print(t1+t2)

