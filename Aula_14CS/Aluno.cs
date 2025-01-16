public class Aluno : IPessoa, IComparable
{
    private string nome; // Atributo privado
    private DateTime nascimento;

    public Aluno(string nome, DateTime nascimento)
    {
        this.nome = nome;
        this.nascimento = nascimento;
    }
    public string GetNome() {
        return this.nome;
    }
    public DateTime GetNascimento() {
        return this.nascimento;
    }
    public int CompareTo(object outro) {
        
    }
 }    

