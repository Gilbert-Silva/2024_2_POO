class Cliente:
    def __init__(self, nome, cpf, limite):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = None
        if nome == "": raise ValueError("Nome inválido")
        if cpf == "": raise ValueError("Cpf inválido")
        if limite < 0: raise ValueError("Limite inválido")
    def set_socio(self, c):
        # self é um cliente, c é um cliente
        if self == c: raise ValueError("Não pode ser sócio dele mesmo")

        # x é sócio atual de self: pode ser None ou não
        x = self.__socio
        # x deixa de ter como sócio self
        if x != None: x.__socio = None

        # y é o sócio atual de c: pode ser None ou não
        y = c.__socio
        # y deixa de ter como sócio c
        if y != None: y.__socio = None

        self.__socio = c
        c.__socio = self
    def get_limite(self):
        if self.__socio == None: return self.__limite
        else: return self.__limite + self.__socio.__limite
    def __str__(self):
        s = f"{self.__nome} - {self.__cpf} - " 
        s += f"Limite individual = {self.__limite} - "
        s += f"Limite total = {self.get_limite()} "
        if self.__socio != None: s += f"Sócio = {self.__socio.__nome}"
        return s    
