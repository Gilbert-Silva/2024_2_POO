import enum

class Estacao(enum.Enum):
  OUTONO = 1
  INVERNO = 2
  PRIMAVERA = 3
  VERAO = 4

a = Estacao.OUTONO

print(a, type(a))
print(a.name, type(a.name))
print(a.value, type(a.value))