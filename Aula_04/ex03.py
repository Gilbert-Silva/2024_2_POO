class Triangulo:
    pass

x = Triangulo()
y = Triangulo()
z = x

print(x)
print(y)
print(z)
a = 5
b = 5
print(id(x), id(y), id(z))
print(id(a), id(b))
b = 6
print(id(a), id(b))
c = None
print(id(a), id(b), id(c))


