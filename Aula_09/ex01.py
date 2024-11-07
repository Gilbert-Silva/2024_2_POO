from datetime import datetime, timedelta

a = datetime(2023, 6, 1)
b = datetime(2023, 6, 1, 9, 30, 15)
c = datetime.now()
d = datetime.today()

print(a, type(a)) # 2023-06-01 00:00:00
print(b, type(b)) # 2023-06-01 09:30:15
print(c)
print(d)

f = datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")
g = datetime.strptime(input("Informe uma data: "), "%d-%m-%Y")
print(f)
print(g)
#g.day = 9
print(g.day)
print(g.month)
print(g.year)
print(g.date())
print(g.time())
print(g.weekday())
print(g.strftime("%d/%m/%Y %H:%M")) 
print(g.strftime("%A, %d/%B/%Y"))




