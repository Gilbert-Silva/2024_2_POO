import math
class Retangulo:
    def __init__(self, b, h):
        self.__b = b
        self.__h = h
    def __str__(self):
        return f"Base = {self.__b}   Altura = {self.__h}"
    def calc_area(self):
        return self.__b * self.__h
    def calc_diagonal(self):
        return math.sqrt(self.__b ** 2 + self.__h**2)
        