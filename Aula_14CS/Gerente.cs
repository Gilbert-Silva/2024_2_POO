public class Gerente : Funcionario
{
    private double gratificacao; // Atributo privado

    // Construtor
    public Gerente(string nome, double salarioBase, double gratificacao) 
        : base(nome, salarioBase) // Chama o construtor da classe base (Funcionario)
    {
        this.gratificacao = gratificacao;
    }

    // Sobrescrita do método GetSalario para incluir a gratificação
    public override double GetSalario()
    {
        return base.GetSalario() + this.gratificacao;
    }
}