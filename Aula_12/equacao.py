import math

class Equacao:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        if a == 0: raise ValueError("Coeficiente a inválido")
    def delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c 
    def x1(self):
        if self.delta() >= 0:
            return (-self.__b - math.sqrt(self.delta())) / (2 * self.__a)
        return None
    def x2(self):
        if self.delta() >= 0:
            return (-self.__b + math.sqrt(self.delta())) / (2 * self.__a)
        return None
    def y(self, x):
        return self.__a * x * x + self.__b * x + self.__c    
    def xplano(self): # valor de x no mínimo ou no máximo
        return -self.__b / (2 * self.__a)

eq = Equacao(1, 0, -4)
print(eq.delta()) 
print(eq.x1())
print(eq.x2())
print(eq.y(-3))
print(eq.y(-2))
print(eq.y(-1))
print(eq.y(0))
print(eq.y(1))
print(eq.y(2))
print(eq.y(3))



 
