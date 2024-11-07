class Empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__clientes = []
        if nome == "": raise ValueError("Nome inválido")
    def inserir(self, c):
        self.__clientes.append(c)
    def listar(self):
        return self.__clientes
    def __str__(self):
        return f"Empresa {self.__nome} tem {len(self.__clientes)} cliente(s)"

