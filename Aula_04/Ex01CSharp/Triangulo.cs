class Triangulo {
    static int qtd;
    public Triangulo() {
        qtd++;
    }
    public static int GetQtd() {
        return qtd;
    } 
    public double b = 0, h = 0;
    public double calc_area() {
        return b * h / 2;
    }
    public override string ToString() {
        return $"Triângulo, base = {b:0.00}, altura = {h:0.00}";
    }
}
