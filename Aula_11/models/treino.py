from datetime import datetime, timedelta
# questão 2
class Treino:
    def __init__(self, id, id_atleta, data, distancia, tempo):
        self.__id = id
        self.__id_atleta = id_atleta
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo
        if distancia <= 0: raise ValueError("Distância inválida")
    def get_id_atleta(self):
        return self.__id_atleta    
    def pace(self):
        t = self.__tempo.total_seconds()/60
        d = self.__distancia / 1000
        return t/d    
    def __str__(self):
        return f"{self.__id} - {self.__id_atleta} - {self.__data.strftime('%d/%m/%Y')} - {self.__distancia}m - {self.__tempo}"

# questão 4
class Treinos:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)
    @classmethod
    def listar(cls):
        return cls.objetos
"""
a = Treino(1, 1, datetime.now(), 5000, timedelta(minutes=30))
b = Treino(2, 1, datetime.now(), 10000, timedelta(hours=1, minutes=10))
c = Treino(2, 1, datetime.now(), 42000, timedelta(hours=2, minutes=10))
Treinos.inserir(a)
Treinos.inserir(b)
Treinos.inserir(c)
for treino in Treinos.listar(): print(treino, treino.pace())
"""