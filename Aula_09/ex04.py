import enum

class Dia(enum.IntFlag):
  Domingo = 1
  Segunda = 2
  Terca = 4
  Quarta = 8
  Quinta = 16
  Sexta = 32
  Sabado = 64

a = Dia.Quarta
print(a, type(a))
print(a.name, type(a.name))
print(a.value, type(a.value))

b = Dia.Quarta | Dia.Quinta
print(b)

