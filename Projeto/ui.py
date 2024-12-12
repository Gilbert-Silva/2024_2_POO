from views import View

class UI:
    # dados do usuário logado
    cliente_id = 0
    cliente_nome = ""
    
    @staticmethod
    def menu_visitante():
        print("1 - Abrir conta, 2 - Entrar no Sistema, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 1: UI.visitante_abrir_conta()
        if op == 2: UI.visitante_entrar_no_sistema()
        return op

    @staticmethod
    def menu_admin():
        print("Cadastro de Clientes")
        print("  1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir")
        print("Cadastro de Categorias")
        print("  5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Excluir")
        print("Cadastro de Produtos")
        print("  9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir, 13 - Reajustar")
        print("0 - Sair, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 0: UI.sair_do_sistema()

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
        return op

    def menu_cliente():
        print("1 - Listar Produtos, 2 - Adicionar Produto no Carrinho, 3 - Fechar Pedido, 4 - Ver Meus Pedidos")
        print("0 - Sair, 99 - Fim")
        op = int(input("\nInforme uma opção: "))
        if op == 0: UI.sair_do_sistema()

        if op == 1: UI.cliente_listar_produto()
        if op == 2: UI.cliente_adicionar_produto()
        if op == 3: UI.cliente_fechar_pedido()
        if op == 4: UI.cliente_meus_pedidos()
        return op

    @classmethod
    def main(cls):
        View.cliente_admin()
        op = 0
        while op != 99:
            if cls.cliente_id == 0:
                # usuário não está logado
                op = UI.menu_visitante()                 
            else:
                # usuário está logado, verifica se é o admin
                admin = cls.cliente_nome == "admin"
                # mensagen de bem-vindo
                print("Bem-vindo(a), " + cls.cliente_nome)
                # menu do usuário
                if admin: op = UI.menu_admin()
                else: op = UI.menu_cliente()

    @classmethod 
    def visitante_abrir_conta(cls):
        cls.cliente_inserir()

    @classmethod    
    def visitante_entrar_no_sistema(cls):
        email = input("Informe o email: ")
        senha = input("Informe a senha: ")
        obj = View.cliente_autenticar(email, senha)
        if obj == None:
            print("E-mail ou senha inválidos")
        else:
            cls.cliente_id = obj["id"]
            cls.cliente_nome = obj["nome"]
        
    @classmethod
    def sair_do_sistema(cls):
            cls.cliente_id = 0
            cls.cliente_nome = ""

    @classmethod 
    def cliente_inserir(cls):
        # Lê os dados de um cliente
        # id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")
        # instancia a classe Cliente -> objeto Cliente
        # cliente = Cliente(0, nome, email, fone)
        # chama a operação de inserir para adicionar o cliente na lista
        # Clientes.inserir(cliente)
        View.cliente_inserir(nome, email, fone, senha)
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
        senha = input("Informe a senha: ")
        # instancia a classe Cliente -> objeto Cliente
        # cliente = Cliente(id, nome, email, fone)
        # chama a operação de atualizar 
        # Clientes.atualizar(cliente)
        View.cliente_atualizar(id, nome, email, fone, senha)
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

    @classmethod
    def cliente_listar_produto(cls):
        print("\nListar Produtos\n")
        
    @classmethod
    def cliente_adicionar_produto(cls):
        print("\nAdicionar Produtos no Carrinho\n")

    @classmethod
    def cliente_fechar_pedido(cls):
        print("\nFechar Pedido\n")

    @classmethod
    def cliente_meus_pedidos(cls):
        print("\nMeus Pedidos\n")

UI.main()            