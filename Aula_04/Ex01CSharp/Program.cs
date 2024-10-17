class Program
{
    static void Main(string[] args)
    {
        Triangulo x = new Triangulo();
        Console.WriteLine("Informe o valor da base: ");
        x.b = double.Parse(Console.ReadLine());
        Console.WriteLine("Informe o valor da altura: ");
        x.h = double.Parse(Console.ReadLine());
        Console.WriteLine($"Área = {x.calc_area():f2}");
    }
}
