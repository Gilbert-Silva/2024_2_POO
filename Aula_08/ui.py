#import empresa
from empresa import Empresa
from cliente import Cliente

class UI:
    empresa = None
    def menu():
        print("1 - Nova empresa, 2 - Mostrar empresa, 3 - Inserir cliente, 4 - Listar clientes, 5 - Sociedade, 9 - Fim")
        return int(input("Informe uma opção: "))
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.nova_empresa()
            if op == 2: UI.mostrar_empresa()
            if op == 3: UI.inserir_cliente()
            if op == 4: UI.listar_clientes()
            if op == 5: UI.sociedade()
    @classmethod 
    def nova_empresa(cls):
        nome = input("Informe o nome da empresa: ")
        cls.empresa = Empresa(nome)
    @classmethod 
    def mostrar_empresa(cls):
        print(cls.empresa)
    @classmethod 
    def inserir_cliente(cls):
        nome = input("Informe o nome: ")
        cpf = input("Informe o cpf: ")
        limite = float(input("Informe o limite: "))
        cliente = Cliente(nome, cpf, limite)
        cls.empresa.inserir(cliente)
    @classmethod 
    def listar_clientes(cls):
        for cliente in cls.empresa.listar():
            print(cliente)
    @classmethod 
    def sociedade(cls):
        clientes = cls.empresa.listar()
        print("Lista de clientes")
        for i, cliente in enumerate(clientes):
            print(f"{i}: {cliente}")
        x = int(input("Informe o número do 1º cliente: "))
        y = int(input("Informe o número do 2º cliente: "))
        clientes[x].set_socio(clientes[y])

UI.main()            