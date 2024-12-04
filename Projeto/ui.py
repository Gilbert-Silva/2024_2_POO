from views import View

class UI:
    @staticmethod
    def menu():
        print("\nCadastro de Clientes")
        print("  1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
        print("\nCadastro de Categorias")
        print("  5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir")
        print("\nCadastro de Produtos")
        print("  9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir, 13 - Reajustar")
        print("\n99-Fim")
        return int(input("Informe uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 99:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()

            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()

            if op == 9:  UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
            if op == 13: UI.produto_reajustar()

    @classmethod 
    def cliente_inserir(cls):
        # Lê os dados de um cliente
        # id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        # instancia a classe Cliente -> objeto Cliente
        # cliente = Cliente(0, nome, email, fone)
        # chama a operação de inserir para adicionar o cliente na lista
        # Clientes.inserir(cliente)
        View.cliente_inserir(nome, email, fone)
    @classmethod 
    def cliente_listar(cls):
        # recupera e percorre a lista de clientes
        #clientes = Clientes.listar()
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:    
            for cliente in clientes: print(cliente)
    @classmethod 
    def cliente_atualizar(cls):
        cls.cliente_listar()
        # Lê o id do cliente a ser atualizado
        id = int(input("Informe o id do cliente a ser alterado: "))
        # Lê os novos dados do cliente
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo email: ")
        fone = input("Informe o novo fone: ")
        # instancia a classe Cliente -> objeto Cliente
        # cliente = Cliente(id, nome, email, fone)
        # chama a operação de atualizar 
        # Clientes.atualizar(cliente)
        View.cliente_atualizar(id, nome, email, fone)
    @classmethod 
    def cliente_excluir(cls):
        cls.cliente_listar()
        # Lê o id do cliente a ser excluído
        id = int(input("Informe o id do cliente a ser excluído: "))
        # instancia a classe Cliente -> objeto Cliente
        # cliente = Cliente(id, "", "", "")
        # chama a operação de excluir 
        # Clientes.excluir(cliente)
        View.cliente_excluir(id)


    @classmethod 
    def categoria_inserir(cls):
        desc = input("Informe a descrição: ")
        View.categoria_inserir(desc)
    @classmethod 
    def categoria_listar(cls):
        objetos = View.categoria_listar()
        if len(objetos) == 0:
            print("Nenhuma categoria cadastrada")
        else:    
            for obj in objetos: print(obj)
    @classmethod 
    def categoria_atualizar(cls):
        cls.categoria_listar()
        id = int(input("Informe o id da categoria a ser alterada: "))
        desc = input("Informe a nova descrição: ")
        View.categoria_atualizar(id, desc)
    @classmethod 
    def categoria_excluir(cls):
        cls.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluída: "))
        View.categoria_excluir(id)


    @classmethod 
    def produto_inserir(cls):
        desc = input("Informe a descrição: ")
        prc = float(input("Informe o preço: "))
        est = int(input("Informe o estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o id da categoria: "))
        View.produto_inserir(desc, prc, est, id_categoria)
    @classmethod 
    def produto_listar(cls):
        objetos = View.produto_listar()
        if len(objetos) == 0:
            print("Nenhum produto cadastrado")
        else:    
            for obj in objetos: 
                id_categoria = obj.id_categoria
                categoria = View.categoria_listar_id(id_categoria)
                print(f"{obj} - {categoria.descricao}")
    @classmethod 
    def produto_atualizar(cls):
        cls.produto_listar()
        id = int(input("Informe o id do produto a ser alterado: "))
        desc = input("Informe a nova descrição: ")
        prc = float(input("Informe o novo preço: "))
        est = int(input("Informe o novo estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Informe o id da categoria: "))
        View.produto_atualizar(id, desc, prc, est, id_categoria)
    @classmethod 
    def produto_excluir(cls):
        cls.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        View.produto_excluir(id)
    @classmethod 
    def produto_reajustar(cls):
        reajuste = float(input("Informe o percentual de reajuste em %: "))
        View.produto_reajustar(reajuste/100)

UI.main()            