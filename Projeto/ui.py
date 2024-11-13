from cliente import Cliente, Clientes

class UI:
    def menu():
        print("Cadastro de Clientes")
        print("  1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 9 - Fim")
        return int(input("Informe uma opção: "))
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir_cliente()
            if op == 2: UI.listar_clientes()
            if op == 3: UI.atualizar_cliente()
            if op == 4: UI.excluir_cliente()
    @classmethod 
    def inserir_cliente(cls):
        # Lê os dados de um cliente
        # id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        # instancia a classe Cliente -> objeto Cliente
        cliente = Cliente(0, nome, email, fone)
        # chama a operação de inserir para adicionar o cliente na lista
        Clientes.inserir(cliente)
    @classmethod 
    def listar_clientes(cls):
        # recupera e percorre a lista de clientes
        clientes = Clientes.listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:    
            for cliente in clientes: print(cliente)
    @classmethod 
    def atualizar_cliente(cls):
        cls.listar_clientes()
        # Lê o id do cliente a ser atualizado
        id = int(input("Informe o id do cliente a ser alterado: "))
        # Lê os novos dados do cliente
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo email: ")
        fone = input("Informe o novo fone: ")
        # instancia a classe Cliente -> objeto Cliente
        cliente = Cliente(id, nome, email, fone)
        # chama a operação de atualizar 
        Clientes.atualizar(cliente)
    @classmethod 
    def excluir_cliente(cls):
        cls.listar_clientes()
        # Lê o id do cliente a ser excluído
        id = int(input("Informe o id do cliente a ser excluído: "))
        # instancia a classe Cliente -> objeto Cliente
        cliente = Cliente(id, "", "", "")
        # chama a operação de excluir 
        Clientes.excluir(cliente)

UI.main()            