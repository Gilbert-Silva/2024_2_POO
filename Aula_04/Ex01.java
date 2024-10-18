import java.util.Scanner;

class Triangulo {
    public double b = 0, h = 0;
    public double calc_area() {
        return b * h / 2;
    }
}

public class Ex01
{
    public static void main(String[] args)
    {
        Triangulo x = new Triangulo();
        System.out.println("Informe o valor da base: ");
        Scanner leitor = new Scanner(System.in);
        x.b = leitor.nextDouble();
        System.out.println("Informe o valor da altura: ");
        x.h = leitor.nextDouble();
        System.out.println(String.format("Área = %.2f", x.calc_area()));
        leitor.close();
    }
}
