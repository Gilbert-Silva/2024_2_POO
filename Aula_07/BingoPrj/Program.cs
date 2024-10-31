namespace BingoPrj;

class Program
{
    private static Bingo jogo;
    static void Main(string[] args)
    {
        int op = 0;
        //Bingo jogo = null;
        while (op != 9) {
            op = menu();
            if (op == 1) jogo = novo_jogo();
            if (op == 2) sortear();
            if (op == 3) sorteados(); 
        }
    }
    public static int menu() {
        Console.WriteLine("1-Novo jogo, 2-Sortear, 3-Sorteados, 9-Fim");
        Console.Write("Informe uma opção: ");
        return int.Parse(Console.ReadLine());
    }
    public static Bingo novo_jogo() {
        Console.Write("Informe o número de bolas: ");
        int n = int.Parse(Console.ReadLine());
        return new Bingo(n);
    }
    public static void sortear(){
        int n = jogo.proximo();
        if (n == -1) Console.WriteLine("Fim do Jogo");
        else Console.WriteLine(n);
    }
    public static void sorteados() {
        foreach (int k in jogo.sorteados()) Console.WriteLine(k);
    }
}
