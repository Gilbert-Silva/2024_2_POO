import java.util.Scanner;
import Aula_04.Triangulo;

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
