namespace ProjetoCS;
public class UI
{
    // Método que exibe o menu e retorna a opção escolhida
    public static int Menu()
    {
        Console.WriteLine("Cadastro de Clientes");
        Console.WriteLine(" 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 9 - Fim");
        Console.Write("Informe uma opção: ");
        return int.Parse(Console.ReadLine());
    }

    // Método principal que controla o fluxo do menu
    public static void Main()
    {
        int op = 0;
        while (op != 9)
        {
            op = Menu();
            switch (op)
            {
                case 1:
                    InserirCliente();
                    break;
                case 2:
                    ListarClientes();
                    break;
                case 3:
                    AtualizarCliente();
                    break;
                case 4:
                    ExcluirCliente();
                    break;
                case 9:
                    Console.WriteLine("Saindo...");
                    break;
                default:
                    Console.WriteLine("Opção inválida. Tente novamente.");
                    break;
            }
        }
    }

    // Método para inserir um novo cliente
    public static void InserirCliente()
    {
        Console.Write("Informe o nome: ");
        string nome = Console.ReadLine();
        
        Console.Write("Informe o email: ");
        string email = Console.ReadLine();
        
        Console.Write("Informe o fone: ");
        string fone = Console.ReadLine();
        
        // Instancia a classe Cliente
        Cliente cliente = new Cliente(0, nome, email, fone);
        
        // Chama a operação de inserir para adicionar o cliente na lista
        Clientes.inserir(cliente);
    }

    // Método para listar todos os clientes cadastrados
    public static void ListarClientes()
    {
        var clientes = Clientes.listar();
        
        if (clientes.Count == 0)
        {
            Console.WriteLine("Nenhum cliente cadastrado.");
        }
        else
        {
            foreach (var cliente in clientes)
            {
                Console.WriteLine(cliente);
            }
        }
    }

    // Método para atualizar os dados de um cliente
    public static void AtualizarCliente()
    {
        ListarClientes();
        
        Console.Write("Informe o id do cliente a ser alterado: ");
        int id = int.Parse(Console.ReadLine());
        
        Console.Write("Informe o novo nome: ");
        string nome = Console.ReadLine();
        
        Console.Write("Informe o novo email: ");
        string email = Console.ReadLine();
        
        Console.Write("Informe o novo fone: ");
        string fone = Console.ReadLine();
        
        // Instancia a classe Cliente com os novos dados
        Cliente cliente = new Cliente(id, nome, email, fone);
        
        // Chama a operação de atualizar
        Clientes.atualizar(cliente);
    }

    // Método para excluir um cliente
    public static void ExcluirCliente()
    {
        ListarClientes();
        
        Console.Write("Informe o id do cliente a ser excluído: ");
        int id = int.Parse(Console.ReadLine());
        
        // Instancia a classe Cliente
        Cliente cliente = new Cliente(id, "", "", "");
        
        // Chama a operação de excluir
        Clientes.excluir(cliente);
    }
}
