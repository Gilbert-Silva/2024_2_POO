package ProjetoJava.src;

import java.util.List;
import java.util.Scanner;

public class UI {

    // Método que exibe o menu e retorna a opção escolhida
    public static int menu() {
        System.out.println("Cadastro de Clientes");
        System.out.println(" 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 9 - Fim");
        System.out.print("Informe uma opção: ");
        
        Scanner scanner = new Scanner(System.in);
        int op = scanner.nextInt();
        scanner.close();
        return op;
    }

    // Método principal que controla o fluxo do menu
    public static void main(String[] args) {
        int op = 0;
        while (op != 9) {
            op = menu();
            switch (op) {
                case 1:
                    inserirCliente();
                    break;
                case 2:
                    listarClientes();
                    break;
                case 3:
                    atualizarCliente();
                    break;
                case 4:
                    excluirCliente();
                    break;
                case 9:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        }
    }

    // Método para inserir um novo cliente
    public static void inserirCliente() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe o nome: ");
        String nome = scanner.nextLine();

        System.out.print("Informe o email: ");
        String email = scanner.nextLine();

        System.out.print("Informe o fone: ");
        String fone = scanner.nextLine();

        // Instancia a classe Cliente
        Cliente cliente = new Cliente(0, nome, email, fone);

        // Chama a operação de inserir para adicionar o cliente na lista
        Clientes.inserir(cliente);

        scanner.close();
    }

    // Método para listar todos os clientes cadastrados
    public static void listarClientes() {
        List<Cliente> clientes = Clientes.listar();

        if (clientes.isEmpty()) {
            System.out.println("Nenhum cliente cadastrado.");
        } else {
            for (Cliente cliente : clientes) {
                System.out.println(cliente);
            }
        }
    }

    // Método para atualizar os dados de um cliente
    public static void atualizarCliente() {
        listarClientes();

        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe o id do cliente a ser alterado: ");
        int id = scanner.nextInt();
        scanner.nextLine();  // Consome a nova linha

        System.out.print("Informe o novo nome: ");
        String nome = scanner.nextLine();

        System.out.print("Informe o novo email: ");
        String email = scanner.nextLine();

        System.out.print("Informe o novo fone: ");
        String fone = scanner.nextLine();

        // Instancia a classe Cliente com os novos dados
        Cliente cliente = new Cliente(id, nome, email, fone);

        // Chama a operação de atualizar
        Clientes.atualizar(cliente);

        scanner.close();
    }

    // Método para excluir um cliente
    public static void excluirCliente() {
        listarClientes();

        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe o id do cliente a ser excluído: ");
        int id = scanner.nextInt();

        // Instancia a classe Cliente
        Cliente cliente = new Cliente(id, "", "", "");

        // Chama a operação de excluir
        Clientes.excluir(cliente);

        scanner.close();
    }
}
