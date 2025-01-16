using System.Collections.Generic;

interface IPessoa {
    string GetNome();
    DateTime GetNascimento();
}

class Relatorio {
    public static void imprimir_aniversariantes(List<IPessoa> pessoas, int mes)
    {
        Console.WriteLine($"Aniversariantes do mês {mes}");
        foreach (IPessoa p in pessoas)
            if (p.GetNascimento().Month == mes)
                Console.WriteLine($"{p.GetNome()} - {p.GetNascimento().Day}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        List<IPessoa> pessoas = new List<IPessoa>();
        pessoas.Add(new Aluno("Ícaro", DateTime.Parse("2020-10-5")));
        pessoas.Add(new Aluno("Emanuelly", DateTime.Parse("2020-11-10")));
        pessoas.Add(new Aluno("Gustavo", DateTime.Parse("2020-10-15")));
        Relatorio.imprimir_aniversariantes(pessoas, 10);

        List<int> x = new List<int> { 5, 10, 8, 3, 12 };  // x [5, 10, 8, 3, 2]
        x.Sort();
        foreach (int i in x) Console.WriteLine(i);

        List<string> y = new List<string> { "Ícaro", "Emanuelly", "Gustavo"};
        y.Sort();
        foreach(string s in y) Console.WriteLine(s);

        pessoas.Sort();
        foreach(IPessoa p in pessoas) Console.WriteLine(p.GetNome());


    }

    static void Main2(string[] args)
    {
        // Criando instâncias das classes Funcionario e Gerente
        Funcionario x = new Funcionario("José Maria", 5000);
        //Gerente y = new Gerente("Maria José", 5000, 3000);
        //Funcionario y = new Gerente("Maria José", 5000, 3000);
        object y = new Gerente("Maria José", 5000, 3000);

        // Imprimindo os resultados
        Console.WriteLine(x.GetNome()); // Nome do funcionário
        Console.WriteLine(x.GetSalario()); // Salário do funcionário
        Console.WriteLine(x); // Representação em string do funcionário
        Console.WriteLine(x.GetType()); // Tipo de x
        Console.WriteLine(x is object); // Verifica se x é uma instância de object
        Console.WriteLine(x is Funcionario); // Verifica se x é uma instância de Funcionario
        Console.WriteLine(x is Gerente); // Verifica se x é uma instância de Gerente

        //Console.WriteLine(y.GetNome()); // Nome do gerente
        //Console.WriteLine(y.GetSalario()); // Salário do gerente
        Console.WriteLine(y); // Representação em string do gerente
        Console.WriteLine(y.GetType()); // Tipo de y
        Console.WriteLine(y is object); // Verifica se y é uma instância de object
        Console.WriteLine(y is Funcionario); // Verifica se y é uma instância de Funcionario
        Console.WriteLine(y is Gerente); // Verifica se y é uma instância de Gerente
    }
}
