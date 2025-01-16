using System;

public class Funcionario
{
    private string nome; // Atributo privado
    protected double salarioBase; // Atributo protegido

    // Construtor
    public Funcionario(string nome, double salarioBase)
    {
        this.nome = nome;
        this.salarioBase = salarioBase;
    }

    // Método para obter o nome
    public string GetNome()
    {
        return this.nome;
    }

    // Método para obter o salário base
    public virtual double GetSalario()
    {
        return this.salarioBase;
    }

    // Sobrescrita do método ToString() para fornecer uma representação da classe
    public override string ToString()
    {
        return $"{this.nome}, {this.GetSalario()}";
    }
}
