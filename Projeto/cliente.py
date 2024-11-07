import json
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Clientes:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)
    @classmethod
    def listar(cls):
        return cls.objetos
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("clientes.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)    

    


