class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Digite um texto");
        string s = Console.ReadLine();
        foreach (string k in s.Split()) Console.WriteLine(k);
                                          // Split é um método de instância
        while (!string.IsNullOrEmpty(s))  // IsNull... é um método estático é chamado com a classe
        {
            Console.WriteLine(s);
            s = Console.ReadLine();
        }

        Triangulo x = new Triangulo();
        Console.WriteLine("Informe o valor da base: ");
        x.b = double.Parse(Console.ReadLine());
        Console.WriteLine("Informe o valor da altura: ");
        x.h = double.Parse(Console.ReadLine());
        Console.WriteLine($"Área = {x.calc_area():f2}");
    }
}
