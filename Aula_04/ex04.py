class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2    

x = Triangulo()  
x.b = 5
x.h = 8
print(x.b, x.h)
y = Triangulo()
y.b = 10
y.h = 20
print(y.b, y.h)
z = y
z.b = 15
z.h = 30
print(y.b, y.h)

print(x.b * x.h / 2) # Área de x
print(y.b * y.h / 2) # Área de y

print(x.calc_area()) # Área de x - Triangulo.calc_area(x)
print(y.calc_area()) # Área de y - Triangulo.calc_area(y)





