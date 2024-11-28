class Program
{
    static void Main(string[] args)
    {
        Triangulo x = new Triangulo();
        x.b = 10;
        x.h = 20;
        Console.WriteLine(x);
        Console.WriteLine(Triangulo.GetQtd());
        Triangulo y = new Triangulo();
        y.b = 20;
        y.h = 10;
        Console.WriteLine(y);
        Console.WriteLine(Triangulo.GetQtd());
    }


    static void Main2(string[] args)
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
