namespace Ex01;

class Program
{
    static void Main(string[] args)
    {
        Triangulo x = new Triangulo();
        Console.WriteLine("Informe o valor da base do triângulo: ");
        x.set_base(double.Parse(Console.ReadLine()));
        Console.WriteLine("Informe o valor da altura do triângulo: ");
        x.set_altura(double.Parse(Console.ReadLine()));
        Console.WriteLine($"Base = {x.get_base()}, Altura = {x.get_altura()}");
        Console.WriteLine($"Área = {x.calc_area()}");
        Console.ReadKey();
    }
}

class Triangulo {
    private double b, h;
    public Triangulo() {
        this.b = 0;
        this.h = 0;
    }    
    public void set_base(double v) {
        if (v > 0) b = v; 
        else throw new ArgumentOutOfRangeException("a base do triângulo não pode ser negativa");
    }    
    public void set_altura(double v) {
        if (v > 0) h = v; 
        else throw new ArgumentOutOfRangeException("a altura do triângulo não pode ser negativa");
    }
    public double get_base() {
        return b;
    }    
    public double get_altura() {
        return h;
    }    
    public double calc_area() {
       return b * h / 2; 
    }        
}
