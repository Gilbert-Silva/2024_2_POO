import java.util.Scanner;

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
        System.out.println(String.format("Area = %.2f", x.calc_area()));
        leitor.close();
    }
}
