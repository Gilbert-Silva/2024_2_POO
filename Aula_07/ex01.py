x = [1, 2, 3, 4]
print(x)
print(*x)
print(type(x))
y = x
z = x[:]
print(id(x), id(y), id(z))
y.append(5)
print(x)
print(y)
print(z)
print(x[-1])



