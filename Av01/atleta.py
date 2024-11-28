from datetime import datetime
# questão 1
class Atleta:
    def __init__(self, id, nome, nascimento):
        self.__id = id
        self.__nome = nome
        self.__nascimento = nascimento
        if nome == "": raise ValueError("Nome inválido")
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__nascimento.strftime('%d/%m/%Y')}"

# questão 3
class Atletas:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)
    @classmethod
    def listar(cls):
        return cls.objetos
"""
a = Atleta(1, "Teste1", datetime.now())
b = Atleta(2, "Teste2", datetime.now())
Atletas.inserir(a)
Atletas.inserir(b)
for atleta in Atletas.listar(): print(atleta)
"""

